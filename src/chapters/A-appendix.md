> Source: [Hugging Face handbook](https://huggingface.co/spaces/huggingface/moe-blogpost/blob/ef70726e6f8b99d74298a16a4894340f288a58c2/app/src/content/chapters/A-appendix.mdx), revision `ef70726e6f8b99d74298a16a4894340f288a58c2`.


<a id="s-a"></a>

## Appendix

<a id="s-a-1"></a>

### A.1 Monitoring in detail

This appendix gives the commands and calculations behind chapter 3's Watch callouts. Router statistics describe the distribution of work, routing traces retain individual expert selections, and activation dumps show what the experts produce. Run-level logs put those measurements alongside loss, timing and memory.

The recipes target [Megatron](https://github.com/NVIDIA/Megatron-LM) commit `d6316eb45`. Keep the configuration and rank layout with each capture: they determine how local expert ids, token positions and routing scores should be interpreted. Collect traces and activations in short diagnostic runs, separately from throughput measurements.

**Code**

**[`router.py#L691-L700`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/router.py#L691-L700) (aux loss, one slot per layer)**

```
layer_number = self._get_metric_layer_number()

get_moe_metrics_tracker().record(
    aux_loss_name,
    aux_loss / aux_loss_coeff,
    layer_number,
    num_layers,
    reduce_group=reduce_group,
    needs_dp_avg=needs_dp_avg,
)
```

**[`router.py#L805-L811`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/router.py#L805-L811) (z-loss, one slot per layer)**

```
get_moe_metrics_tracker().record(
    "z_loss",
    z_loss / moe_z_loss_coeff,
    layer_number,
    num_layers,
    avg_group=self.tp_dp_cp_group,
)
```

**[`moe_logging.py#L392-L404`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/moe_logging.py#L392-L404) (per-layer scalars)**

```
for name in metric_names:
    if name not in self._metrics:
        continue

    values = self._metrics[name].values.float() * loss_scale
    is_sparse = percentiles is not None and name in percentiles
    for i, val in enumerate(values.tolist()):
        if is_sparse and val == 0:
            continue
        if writer is not None:
            writer.add_scalar(f"moe/{name}_layer_{i}", val, iteration)
        if wandb_writer is not None:
            wandb_writer.log({f"moe/{name}_layer_{i}": val}, iteration)
```

**[`router_trace.py#L217-L221`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/router_trace.py#L217-L221) (hook on every router)**

```
for chunk in model:
    unwrapped = unwrap_model(chunk)
    for module_name, module in unwrapped.named_modules():
        if isinstance(module, TopKRouter):
            handle = module.register_forward_hook(self.make_hook(module_name))
```

**[`router_trace.py#L353-L365`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/router_trace.py#L353-L365) (routing map to top-k ids)**

```
if second.dtype == torch.bool:
    topk = getattr(module, "topk", None)
    if topk is None:
        return
    num_tokens = second.shape[0]
    _, expert_idx = second.nonzero(as_tuple=True)
    if expert_idx.numel() != num_tokens * topk:
        return
    top_indices = expert_idx.view(num_tokens, topk)
else:
    top_indices = second

top_indices_cpu = top_indices.detach().to("cpu", torch.int32, non_blocking=True)
```

**[`router_trace.py#L383-L395`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/router_trace.py#L383-L395) (logits recomputed, saved bf16)**

```
if self.capture_logits:
    hs_for_gating = self._extract_hidden_state(inputs, num_tokens)
    gating_fn = getattr(module, "gating", None)
    if hs_for_gating is not None and callable(gating_fn):
        try:
            with torch.no_grad():
                logits = gating_fn(hs_for_gating)
            if isinstance(logits, tuple):
                logits = logits[0]
        except Exception:
            logits = None
        if torch.is_tensor(logits) and logits.shape[0] == num_tokens:
            logits_cpu = logits.detach().to("cpu", dtype=torch.bfloat16).contiguous()
```

**[`training.py#L5387-L5393`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/training/training.py#L5387-L5393) (params norm)**

```
if _should_compute_params_norm(args, iteration, is_first_iteration):
    # Cross-rank param L2 norm (--log-params-norm): a full-model reduction
    # + all-reduce that BLOCKS the training loop -- exposed goodput cost
    # (~1.5s cold on the first iteration, ~10ms steady). Kept as a real
    # cost span (it stalls the critical path), unlike passive monitors.
    with _otel_managed_span('step', 'megatron.train.params_norm', is_goodput_span=True):
        params_norm = calc_params_l2_norm(model, pg_collection=pg_collection)
```

**[`clip_grads.py#L282-L288`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/optimizer/clip_grads.py#L282-L288) (zeros in the gradient)**

```
if grad_not_none and is_not_shared and is_not_tp_duplicate and is_not_gtp_duplicate:
    grad_obj = getattr(param, grad_attr)
    data_parallel_group = get_data_parallel_group_if_dtensor(grad_obj, data_parallel_group)
    grad = to_local_if_dtensor(grad_obj).detach()
    num_zeros = grad.numel() - torch.count_nonzero(grad)
    num_zeros -= _gtp_pad_zero_count(param, grad)  # exclude structural GTP padding
    total_num_zeros = num_zeros + total_num_zeros
```

**[`qk_clip.py#L30-L40`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/optimizer/qk_clip.py#L30-L40) (max attention logit)**

```
torch.distributed.all_reduce(
    transformer_layer.self_attention.core_attention.current_max_attn_logits,
    op=torch.distributed.ReduceOp.MAX,
    group=parallel_state.get_data_parallel_group(with_context_parallel=True),
)
log_max_attention_logit = max(
    log_max_attention_logit,
    torch.max(
        transformer_layer.self_attention.core_attention.current_max_attn_logits
    ).item(),
)
```

**[`param_and_grad_buffer.py#L396-L406`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/distributed/param_and_grad_buffer.py#L396-L406) (NaN grad stops the run)**

```
grad_norm = self.buckets[i].grad_data.norm(p=2)
# check for NaN, Inf and unexpectedly large grads
if check_for_nan_or_inf:
    rerun_state_machine.validate_result(
        result=grad_norm,
        rejection_func=torch.isnan,
        message=f"found NaN in local grad norm for bucket #{i} "
        f"in backward pass before data-parallel communication collective",
        tolerance=0.001,  # 0.1% tolerance to account for non-deterministic FA backward
        fatal=True,
    )
```

Our scripts: [`router_watch.py`](https://gist.github.com/nmntz/5de952d686f66d7bce5bce8cba9d7139#file-router_watch-py) reads token counts and routing traces and checks fp32 flips on a live router, [`expert_watch.py`](https://gist.github.com/nmntz/5de952d686f66d7bce5bce8cba9d7139#file-expert_watch-py) reads activation dumps, and [`expert_watch_hooks.py`](https://gist.github.com/nmntz/5de952d686f66d7bce5bce8cba9d7139#file-expert_watch_hooks-py) samples a live forward; their commands and capture recipes appear beside the relevant metric in the prose.

<a id="s-a-1-router-stats"></a>

#### Router stats

##### Per-layer losses

Enable `--moe-per-layer-logging` with the [Trackio](https://huggingface.co/docs/trackio) launcher from [2.4](2-setup-and-your-first-run.md#s-2-4) to record the auxiliary loss and z-loss for each layer. Megatron logs the losses enabled in the configuration, with their coefficients divided out. A run using expert bias for balancing can still report a sequence-wise auxiliary loss or z-loss when those losses are enabled.

The auxiliary loss can read 1 with flat probabilities even when token counts are uneven ([3.3](3-anatomy-of-moe-training.md#s-3-3)), so use token counts to measure load directly. Z-loss describes the scale of the logits: the square root of its logged value gives the RMS of logsumexp across tokens.

##### Expert counts and MaxVio

To save the number of tokens processed by each local expert, add these flags to the training command:

```
--save run/ \
--moe-grouped-gemm \
--save-tokens-per-expert-interval 100
```

The hook on the grouped linear layers writes `run/tokens_per_expert/rank*.jsonl`. Each record identifies an iteration and layer, with a `tpe` list containing a count vector for each captured micro-batch. Decoder layers and MTP layers have separate identities. The vectors describe local expert loads after dispatch ([`activation_logging.py`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/training/activation_logging.py)).

For an expert count vector c, MaxVio measures the busiest expert's excess load relative to the mean[52](A-appendix.md#ref-2408.15664) [evidence](../citation-evidence.md#lossfree-maxvio):

```
MaxVio = max(c) / mean(c) - 1
```

For example, counts `[2, 2, 4, 0]` have a mean of 2 and MaxVio of 1: the busiest expert receives twice the average load. The zero-count expert contributes to that mean and must remain in the calculation. An even load gives 0; an all-zero vector has undefined MaxVio.

Choose the aggregation scope before computing the metric:

- **Micro-batch:** join the local expert vectors across one expert-parallel (EP) group, in global expert-id order.
- **Global batch:** sum each expert's counts over micro-batches and independent data replicas, then compute MaxVio from the resulting vector.
- **Sequence:** use individual routing selections and sequence boundaries, as described under Routing diagnostics.

Averaging micro-batch MaxVio values does not give global-batch MaxVio. Experts can be unevenly loaded within each micro-batch yet balanced over the batch ([3.3](3-anatomy-of-moe-training.md#s-3-3)). The aggregation must also preserve layer identity: keep pipeline stages and MTP depths separate. [Interleaved pipeline](https://huggingface.co/spaces/nanotron/ultrascale-playbook?section=interleaving_stages) chunks reuse local layer ids, and the saved records do not distinguish them ([`activation_logging.py#L131-L134`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/training/activation_logging.py#L131-L134)), so disable interleaving for the capture. [Activation recomputation](https://huggingface.co/spaces/nanotron/ultrascale-playbook?section=activation_recomputation) can duplicate hook calls, so capture without recomputation or retain identifiers for the original forwards.

The [`router_watch.py`](https://gist.github.com/nmntz/5de952d686f66d7bce5bce8cba9d7139#file-router_watch-py) reader joins count files using an explicit map from rank to global expert ids. For two ranks holding four experts, save `{"0": [0, 1], "1": [2, 3]}` as `experts.json`, then run:

```
python3 scripts/router_watch.py counts run/tokens_per_expert \
    --num-experts 4 --ranks 0 1 \
    --expert-map experts.json --pool-ranks
```

`--pool-ranks` declares that the selected files contain independent work for the same layer, with tensor-parallel duplicates removed. For per-micro-batch measurements, retain the identities needed to match captured forwards across ranks.

##### Load per rank

Sum the counts of the experts placed on each EP rank, then compare the busiest rank with the mean. Read this alongside expert MaxVio: several busy experts placed on the same GPU can concentrate work there ([3.3](3-anatomy-of-moe-training.md#s-3-3), [3.7](3-anatomy-of-moe-training.md#s-3-7)).

With capacity limits or padding enabled, grouped GEMM counts describe the work after those operations. To measure the original demand, use the router's unpadded assignments.

<a id="s-a-1-routing-diagnostics"></a>

#### Routing diagnostics

##### Capturing expert selections

For a short capture, add the following flags to the training command, replacing `trace_steps` with the number of iterations to capture:

```
--moe-routing-trace-path trace/ \
--moe-routing-trace-max-training-iters trace_steps \
--cuda-graph-impl none
```

The hook records selected expert ids before dispatch. Add `--moe-routing-trace-capture-logits` to save the logits file, or `--moe-routing-trace-capture-hidden-states --moe-routing-trace-dump-weights` to save hidden states and router weights. These captures write to disk, and the Python hooks require eager execution.

Expert ids follow the routing map's order, so sort by reconstructed weight when a metric needs the leading expert. Dropping can cause an entire record to be skipped. Treat such a gap as a missing observation ([`router_trace.py`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/router_trace.py)).

##### Counts and MaxVio from a trace

The selected expert ids also give token counts and MaxVio, without a logits capture. To read these for one rank with 64 experts:

```
python3 scripts/router_watch.py trace trace/ --num-experts 64 --ranks 0
```

Each `trace_call` record contains `counts` and `maxvio` for one captured call. The `rank_captured_step` records sum those counts within each layer, rank and step, then compute MaxVio from the sum. These summaries cover the captured tokens; a global-batch measurement requires all of its original forwards and independent replicas, with tensor-parallel duplicates removed. Use the aggregation rules under Expert counts and MaxVio when joining captures. Records skipped because of dropped assignments remain missing from these totals.

##### Per-sequence balance

Per-sequence balance requires the sequence membership of each token row. For complete, unpartitioned inputs laid out as `[sequence, batch, hidden]`, with batch size B, row `s * B + b` belongs to sequence b. Pass `--sequence-length S --batch-size B` to the trace reader only when that layout holds.

Within each sequence, count assignments to each expert, including experts with zero assignments, then compute MaxVio from that vector. Summarize the per-sequence values by layer.

For packed sequences, replace the fixed-length layout with the actual sequence boundaries. Context or [sequence parallelism](https://huggingface.co/spaces/nanotron/ultrascale-playbook?section=sequence_parallelism) also requires token positions to join the pieces across ranks. Following a token across observations requires its identity as well, since the same row number at two training steps generally refers to different tokens.

##### Mixture weights

The logits file supports an approximate reconstruction of the weights applied to the selected experts. The hook recomputes these logits and stores them in bf16. Preserve the recorded selections, and use the run's score function, normalization and routed scaling factor when reconstructing the weights.

For a softmax capture with 64 experts and a scaling factor of 1:

```
python3 scripts/router_watch.py trace trace/ \
    --num-experts 64 --ranks 0 --score softmax --scale 1
```

Add `--pre-softmax` if the run applied softmax over all experts before selection. Otherwise, softmax applies over the selected logits. For sigmoid and sqrt(softplus), use the run's normalization of the selected scores. Expert bias affects selection; keep it out of the mixture weights.

Let w denote the final selected weights, including the scaling factor, and let q be w divided by its sum. Compute each metric per token before summarizing it by layer:

- **Largest weight:** `max(w)` is the largest multiplier on an expert output. Use `max(q)` to compare concentration across different scaling factors.
- **Selected-weight entropy:** `-sum(q * log(q))` ranges from 0 to `log(k)` and increases as the k selected weights become more equal. At top-1 it is 0\.
- **Max1/Max2:** the largest weight divided by the second largest. Values near 1 indicate similar leading weights; the ratio is undefined at top-1.
- **Estimated mixture RMS:** `sqrt(sum(q*q))` estimates mixture RMS relative to one expert when expert outputs have equal RMS and are uncorrelated ([3.1](3-anatomy-of-moe-training.md#s-3-1)). Using w includes the routed scaling factor.
- **Top-k probability mass:** for pre-softmax routing, sum the selected full-softmax probabilities before scaling. Raw sigmoid and sqrt(softplus) scores have a different interpretation because they are not probabilities over all experts.

For illustration, selected weights `[0.75, 0.25]` give a largest weight of 0.75, Max1/Max2 of 3 and entropy of about 0.562, using natural logarithms.

##### Nodes reached per token

To measure communication fan-out, map the selected expert ids to their destination nodes and count the distinct nodes for each token. Report the mean and maximum by layer ([3.7](3-anatomy-of-moe-training.md#s-3-7)).

Pass `--node-map nodes.json` to the trace reader. The file maps global expert ids to node names, for example `{"0": "node-a", "1": "node-a", "2": "node-b"}`. For replicated experts, capture the destination actually chosen by the dispatcher. Counting remote nodes also requires the token's source node so it can be excluded.

Converting fan-out to bytes requires the hidden width, dtype and dispatcher's copy policy: one copy per expert and one copy per destination node give different traffic volumes.

##### Dropped assignments

With a capacity limit, measure drops from the router's final routing map. For N valid tokens and K surviving assignments:

```
dropped_fraction = 1 - K / (N * topk)
```

This counts lost token-expert assignments. A token may retain some of its experts. Exclude masked tokens and rows added for quantized GEMMs from the calculation. Use a live hook for this measurement, since the saved trace can skip records containing drops. The [`ExpertWatch`](https://gist.github.com/nmntz/5de952d686f66d7bce5bce8cba9d7139#file-expert_watch_hooks-py) helper captures this map; its setup and supported configurations appear under Shared and routed contributions.

##### Precision flips

The fp32 flip rate measures how often the selected expert set changes when the router calculation uses fp32. Both calculations must use the same forward's inputs, weights, biases and selection rules. Compare sets so that a change in ordering alone does not count as a flip.

For plain token-choice routing, [`install_fp32_flip_hook`](https://gist.github.com/nmntz/5de952d686f66d7bce5bce8cba9d7139#file-router_watch-py) performs this comparison on the live state. Attach it to the chosen MoE layer's router for one eager forward. Replace `moe_layer`, `model` and `tokens` with the objects in the training harness:

```
import torch
from scripts.router_watch import install_fp32_flip_hook

previous_tf32 = torch.backends.cuda.matmul.allow_tf32
handle = install_fp32_flip_hook(moe_layer.router, emit=print)
try:
    torch.backends.cuda.matmul.allow_tf32 = False
    output = model(tokens)
finally:
    handle.remove()
    torch.backends.cuda.matmul.allow_tf32 = previous_tf32
```

Disabling TF32 gives the reference matrix multiplication fp32 precision. The hook compares selected expert sets on a bounded sample of valid tokens. Its docstring lists the supported settings; routing transformations outside those settings are rejected. Run with CUDA graphs disabled and outside timed measurements.

Both calculations start from the live input's existing precision. The result isolates a routing disagreement at that input precision; assessing its effect on loss requires a separate experiment ([3.1](3-anatomy-of-moe-training.md#s-3-1)).

For offline comparisons, retain the exact state and gating input of the captured forward, including jitter. The built-in weight dump snapshots each router on its first observed call, so it does not track subsequent updates to weights and balancing biases. Hidden states and recomputed logits are stored in bf16, and the snapshot omits the router's linear bias, if present. Reconstructions from these files should therefore be labeled approximate, with the capture step and missing state specified.

<a id="s-a-1-expert-activations"></a>

#### Expert activations

##### Capturing activations

Add `--save run/ --save-activations-interval 100` to capture inputs and outputs of supported linear modules, including grouped expert token counts. Each module's entry is overwritten on its next captured call, leaving the last captured micro-batch. The hook copies tensors to CPU on captured calls, so use a sparse interval and a short diagnostic run with CUDA graphs and activation recomputation disabled.

##### Per-expert output norms

The native dump's `experts.linear_fc2/output0` contains rows for the local experts. Split those rows using the module's `input1` token counts, convert to fp32, and calculate the L2 norm of each token's output vector. The mean of those norms describes the expert's output magnitude. Dividing each norm by the square root of the output width gives token RMS, useful for comparisons across widths.

The [`expert_watch.py`](https://gist.github.com/nmntz/5de952d686f66d7bce5bce8cba9d7139#file-expert_watch-py) reader performs these calculations. In an environment with PyTorch, run:

```
python3 scripts/expert_watch.py \
    --unpadded --expert-tp-size 1 activations.pth
```

These options assert that the captured rows contain no padding and expert tensor parallelism is 1\. The reader reports each expert's token count, norm sum and mean norm. It also reports the largest and smallest mean norms relative to the median among experts that received tokens ([3.4](3-anatomy-of-moe-training.md#s-3-4), [3.6](3-anatomy-of-moe-training.md#s-3-6)).

An empty expert has no mean output norm, so the reader lists empty experts separately. The ratios are also undefined when the median is zero. Taking the norm of all an expert's rows concatenated would mix output magnitude with token count; averaging the per-token norms keeps those measurements separate.

The median used for these ratios covers the experts in one file. For a layer-wide comparison, join the EP shards before computing the median. Repeated observations can be merged by summing each expert's `sum_l2` and `rows`, then dividing to obtain its mean. With expert tensor parallelism above 1, first combine the partial output vectors; their individual norms cannot be added to recover the full vector's norm. Exclude padding rows from these calculations.

Grouped fc2 outputs can already include routing weights, depending on where the implementation applies them. A small norm can therefore reflect a small routing weight. Keep the point where weights are applied fixed across comparisons, and examine the mixture weights alongside the norms.

For live sampling, `ExpertWatch` reports the same per-expert norm statistics in its `routed_experts` output, including `local_max_to_median` and `local_min_to_median`. These ratios cover the local experts; join their statistics across EP ranks before computing a layer-wide median. The setup under Shared and routed contributions collects these statistics during the same forward.

##### Latent up-projection

To inspect the latent up-projection, read `fc2_latent_proj/output0` and compare its input and output RMS ([3.4](3-anatomy-of-moe-training.md#s-3-4)). RMS accounts for the difference between latent width and model width. With `--moe-use-norm-before-up-proj`, also sample before the normalization to locate where the growth begins.

##### Shared and routed contributions

To compare the two branches, capture the shared output after its optional sigmoid gate and the routed output after unpermutation and combination. Include the latent up-projection when present. For each token, compute `norm(shared) / norm(routed)`, keeping zero denominators separate. This ratio compares branch magnitudes; the vectors can still reinforce or cancel one another when added.

The raw fc2 dumps occur earlier: shared fc2 is before the gate, and routed fc2 is before combination. For a live sample at the required points, attach [`ExpertWatch`](https://gist.github.com/nmntz/5de952d686f66d7bce5bce8cba9d7139#file-expert_watch_hooks-py) around one diagnostic forward:

```
from scripts.expert_watch_hooks import ExpertWatch

with ExpertWatch(moe_layer, emit=print):
    output = model(tokens)
```

This helper supports eager execution with the all-to-all dispatcher, tensor and expert-tensor parallel sizes of 1, and shared-expert overlap disabled. The sample must be unpadded, with quantization and expert padding disabled. Keep the hooks scoped to the diagnostic forward, as shown above, and save the JSON output per rank with the step and micro-batch identity.

For a standard MoE, the helper recovers the routed branch by subtracting the post-gate shared output from the total. The subtraction retains rounding error from the original addition, so a small routed contribution beside a large shared one calls for direct capture before addition. For a latent MoE, the helper captures the up-projection's output directly. Branch summaries include padding positions, which is why this comparison requires an unpadded sample.

To check the hooks on CPU before attaching them, run `python -m unittest scripts.test_router_watch scripts.test_expert_watch`.

<a id="s-a-1-run-health"></a>

#### Run health

##### Loss and gradient signals

Keep LM loss and gradient norm beside the router and expert measurements. The following flags add run-level signals:

- `--log-throughput`: training throughput.
- `--log-params-norm`: parameter norm.
- `--log-num-zeros-in-grad`: number of zero entries across model gradients.
- `--log-max-attention-logit`: largest attention logit; requires [Transformer Engine](https://github.com/NVIDIA/TransformerEngine) 2.9 or later.

To investigate expert-specific underflow ([3.7](3-anatomy-of-moe-training.md#s-3-7)), count exact zeros in expert weight gradients after accumulation and before the optimizer update. Compare this expert-specific count with a BF16 run of the same configuration.

NaN checking is enabled by default. A detected NaN stops the step and invokes rerun handling ([3.6](3-anatomy-of-moe-training.md#s-3-6)); `--no-check-for-nan-in-loss-and-grad` disables the check.

##### Timing and memory

Add `--timing-log-level 2 --timing-log-option all` for per-rank forward and backward timings. Group ranks by pipeline stage to locate a slow stage, including one holding MTP ([3.6](3-anatomy-of-moe-training.md#s-3-6)). Then profile that stage using the tools in [3.7](3-anatomy-of-moe-training.md#s-3-7).

Compare the same warmed-up interval across runs. For peak memory, reset CUDA peak statistics at the interval's start and read `torch.cuda.max_memory_allocated()` on each rank at its end. Take the maximum across ranks to report the highest peak allocated memory.

<a id="s-a-2"></a>

### A.2 Debugging index

Chapter 3 went setting by setting, from a flag to what it does to the run. When a run misbehaves you travel the other way: you see a symptom on the dashboard and need the config behind it. This appendix is that reverse index, one row per symptom, each pointing back to the part of the post that explains it.

Before you blame a setting, though, rule out the stack itself with the two checks at the end of [2.5](2-setup-and-your-first-run.md#s-2-5).

<a id="s-a-2-read-the-index"></a>

#### Read the index

Each row carries a tag, the symptom with the first signal that moves, and the section to read. The tags sort runs by how they fail: `slow`, `OOM`, `blows up`, `learns badly`, and `won't start` for runs that stop before their first iteration. Find your tag, then the signal that moved first, and the row tells you where to go; the map in the introduction draws all of these rows but one, the `global_aux_loss` setting, which has no signal to start from.

**Debugging index, 42 symptoms**

| Tag | Symptom | Read |
| --- | --- | --- |
| `slow` | throughput drop | [3.3](3-anatomy-of-moe-training.md#s-3-3), [3.7](3-anatomy-of-moe-training.md#s-3-7) profiling |
| `slow` | half the single-node step is all-to-all | [3.3](3-anatomy-of-moe-training.md#s-3-3) balance first, then [3.7](3-anatomy-of-moe-training.md#s-3-7) overlap |
| `slow` | aux loss near 1 but one GPU slow | [3.3 Cost of imbalance](3-anatomy-of-moe-training.md#s-3-3-cost-of-imbalance) (the aux loss equals 1 for flat router probabilities whatever the load; read MaxVio) |
| `slow`, `learns badly` | loss-free bias run still unbalanced after many steps | [3.3 Loss-free bias](3-anatomy-of-moe-training.md#s-3-3-loss-free-bias) (fixed step lags; quantile balancing) |
| `slow`, `learns badly` | a few experts overloaded only in the first layers | [3.2](3-anatomy-of-moe-training.md#s-3-2) hash layers, [3.5 Dense layers](3-anatomy-of-moe-training.md#s-3-5-dense-layers) |
| `slow` | each token's all-to-all reaches every node | [3.7 Interconnect](3-anatomy-of-moe-training.md#s-3-7-interconnect) and group-limited routing |
| `slow` | throughput drops after moving to more, smaller experts | [3.4](3-anatomy-of-moe-training.md#s-3-4) count and size |
| `slow`, `OOM` | step much slower after turning on MTP, or OOM with more layers under pipeline parallelism | [3.6 MTP](3-anatomy-of-moe-training.md#s-3-6-mtp) |
| `slow` | all-to-all exposed in the profile | [3.5 Block wiring](3-anatomy-of-moe-training.md#s-3-5-block-wiring), [3.7 Overlap](3-anatomy-of-moe-training.md#s-3-7-overlap) |
| `slow` | multi-node about 25x slower on our EP16 proxy and the NCCL log says 'Using network Socket' | [3.7 Interconnect](3-anatomy-of-moe-training.md#s-3-7-interconnect) |
| `slow` | step slower after moving to `global_aux_loss` | [3.3 Scope](3-anatomy-of-moe-training.md#s-3-3-scope) |
| `slow` | under quantile balancing, MaxVio per global batch low but per micro-batch high | [3.3 Quantile](3-anatomy-of-moe-training.md#s-3-3-quantile) |
| `slow` | step slower with `--moe-latent-size` | [3.4 Latent MoE](3-anatomy-of-moe-training.md#s-3-4-latent-moe), from the two d × ℓ projections and smaller expert GEMMs ([3.4](3-anatomy-of-moe-training.md#s-3-4)); the throughput LatentMoE reports is serving, 12% lower at concurrency 1 |
| `slow` | slower inference after adding a shared expert on top of the routed top-k | [3.4 Shared experts](3-anatomy-of-moe-training.md#s-3-4-shared-experts) |
| `slow` | full recompute still on | [3.7 Memory](3-anatomy-of-moe-training.md#s-3-7-memory) |
| `slow` | TFLOP/s still short after balance, overlap and fusions | [3.7 Precision](3-anatomy-of-moe-training.md#s-3-7-precision) |
| `OOM` | OOM on one rank | [3.3](3-anatomy-of-moe-training.md#s-3-3) (imbalance), [3.7](3-anatomy-of-moe-training.md#s-3-7) memory |
| `OOM` | peak memory looks fine but one rank OOMs | [3.7](3-anatomy-of-moe-training.md#s-3-7) memory (Megatron logs data-parallel rank 0 only) |
| `blows up` | a NaN with nothing moving before it (grad norm, params norm, z-loss flat) | [3.6](3-anatomy-of-moe-training.md#s-3-6) stability (no warning; the rerun on another GPU tells a faulty GPU from a reproducible NaN) |
| `blows up` | exit code 16 twice on one node | [3.6](3-anatomy-of-moe-training.md#s-3-6) stability (the rerun needs a different GPU) |
| `blows up` | Muon run diverges in the first steps | [3.6](3-anatomy-of-moe-training.md#s-3-6) optimizer (update scale, `--muon-extra-scale-factor`) |
| `blows up` | z-loss or router logits climbing before a spike | [3.1](3-anatomy-of-moe-training.md#s-3-1) precision (a flat z-loss before a NaN points to [3.6](3-anatomy-of-moe-training.md#s-3-6) stability instead) |
| `blows up` | expert output norms growing, or their max-to-median ratio climbing before a spike | [3.4](3-anatomy-of-moe-training.md#s-3-4) activation (clamp) |
| `blows up` | exploding activations or a spike with a latent MoE | [3.4](3-anatomy-of-moe-training.md#s-3-4) latent (norm before the up-projection) |
| `blows up` | grad norm and load-balancing loss jump a few iterations before a NaN | [3.6](3-anatomy-of-moe-training.md#s-3-6) stability, [3.3](3-anatomy-of-moe-training.md#s-3-3). Our 7B-A1B |
| `blows up` | loss spikes under Muon that resuming from a nearby checkpoint often avoids | [3.6](3-anatomy-of-moe-training.md#s-3-6) optimizer (orthogonalization in bf16) |
| `learns badly` | RL reward stalls or collapses while the train-inference probability gap grows | 4 RL routing |
| `learns badly` | loss flat but MaxVio or an expert's output norm drifting from the layer median (collapse, dead or rogue expert) | [3.6](3-anatomy-of-moe-training.md#s-3-6) stability, [3.3](3-anatomy-of-moe-training.md#s-3-3) |
| `learns badly` | top-k weights all equal (flat gate) | [3.1](3-anatomy-of-moe-training.md#s-3-1) sharpness |
| `learns badly` | dead experts with an aux loss on | [3.3 Aux loss](3-anatomy-of-moe-training.md#s-3-3-aux-loss) (coefficient too small) |
| `learns badly` | `global_aux_loss` with more than 256 micro-batches per global batch | [3.3 Scope](3-anatomy-of-moe-training.md#s-3-3-scope) Flags (bf16 counter) |
| `learns badly`, `blows up` | routing collapse or divergence in the first MoE layers | [3.5 Dense layers](3-anatomy-of-moe-training.md#s-3-5-dense-layers) |
| `learns badly` | a capacity factor is set and the loss lags the dropless run | [3.7 Capacity and replicas](3-anatomy-of-moe-training.md#s-3-7-capacity-and-replicas) (drops are not logged |
| `learns badly` | experts collapse layer by layer under Muon | [3.6](3-anatomy-of-moe-training.md#s-3-6) optimizer |
| `learns badly` | with `--moe-router-pre-softmax` (top-k weights not renormalized), loss above a renormalized run | [3.1 Output scale](3-anatomy-of-moe-training.md#s-3-1-output-scale) |
| `learns badly` | experts that do not specialize by domain | [3.3 Scope](3-anatomy-of-moe-training.md#s-3-3-scope) |
| `learns badly` | LM loss rising with the aux coefficient | [3.3 Aux loss](3-anatomy-of-moe-training.md#s-3-3-aux-loss) |
| `learns badly` | loss no longer improving as experts get smaller | [3.4 Count and size](3-anatomy-of-moe-training.md#s-3-4-count-and-size) |
| `learns badly` | a model trained with expert choice routing differently at inference | [3.2 Who selects](3-anatomy-of-moe-training.md#s-3-2-who-selects) |
| `learns badly` | an upcycled MoE that learns slowly after its head start | [3.6 Upcycling](3-anatomy-of-moe-training.md#s-3-6-upcycling) |
| `won't start` | `--moe-use-upcycling` fails with "unexpected keyword argument 'model'" or a missing `pre_mlp_layernorm` key | [3.6](3-anatomy-of-moe-training.md#s-3-6) upcycling (two upstream bugs) |
| `won't start` | assert about full recomputation after turning on `--overlap-moe-expert-parallel-comm` | [3.7](3-anatomy-of-moe-training.md#s-3-7) overlap and memory |

The signal matters more than the symptom, because the same symptom can have causes in different parts. Before each of our NaNs, the signal we were watching (the grad norm, the params norm or the z-loss) stayed flat, and the one we traced was born in the backward pass of the grouped expert GEMM. For such a NaN, Megatron's rerun on another GPU tells a faulty GPU from a NaN that the data or the model really produced ([3.6 Stability](3-anatomy-of-moe-training.md#s-3-6-stability)). A slow step with an aux loss near 1 sends you to MaxVio instead: [Megatron](https://github.com/NVIDIA/Megatron-LM)'s aux loss [equals 1](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/moe_utils.py#L147-L150) whenever the router's probabilities are flat, whatever the load, so a single overloaded GPU can hide behind it ([3.3 Cost of imbalance](3-anatomy-of-moe-training.md#s-3-3-cost-of-imbalance)).

<a id="references"></a>

<a id="ref-2605.27605"></a>1. Julien Abadji, Marah Abdin, Connor Adams, Eric Alcaide, Mustafa Altun et al. (2026). [Laguna M.1/XS.2 Technical Report](https://arxiv.org/abs/2605.27605). arXiv:2605.27605.
<a id="ref-2604.12163"></a>2. Chandan Akiti, Ajay Modukuri, Murali Nandan Nagarapu, Gunavardhan Akiti, Haozhe Liu (2026). [Nucleus-Image: Sparse MoE for Image Generation](https://arxiv.org/abs/2604.12163). arXiv:2604.12163.
<a id="ref-2404.05019"></a>3. Weilin Cai, Juyong Jiang, Le Qin, Junwei Cui, Sunghun Kim et al. (2024). [Shortcut-connected Expert Parallelism for Accelerating Mixture-of-Experts](https://arxiv.org/abs/2404.05019). arXiv:2404.05019.
<a id="ref-doc-4"></a>4. Jonathan Chang. [Causal Routing Bias for Aux-Loss-Free MoE Training](https://jonathanc.net/blog/causal-routing-bias). blog.
<a id="ref-2605.27358"></a>5. Yanbei Chen, Hanxian Huang, Ernie Chang, Jacob Szwejbka, Digant Desai et al. (2026). [MobileMoE: Scaling On-Device Mixture of Experts](https://arxiv.org/abs/2605.27358). arXiv:2605.27358.
<a id="ref-2609.04575"></a>6. Xing Chen, Hengshuai Yao (2026). [Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/abs/2609.04575). arXiv:2609.04575.
<a id="ref-2204.09179"></a>7. Zewen Chi, Li Dong, Shaohan Huang, Damai Dai, Shuming Ma et al. (2022). [On the Representation Collapse of Sparse Mixture of Experts](https://arxiv.org/abs/2204.09179). arXiv:2204.09179.
<a id="ref-2202.01169"></a>8. Aidan Clark, Diego de las Casas, Aurelia Guy, Arthur Mensch, Michela Paganini et al. (2022). [Unified Scaling Laws for Routed Language Models](https://arxiv.org/abs/2202.01169). arXiv:2202.01169.
<a id="ref-2602.04870"></a>9. Chenwei Cui, Rockwell Jackson, Benjamin Joseph Herrera, Ana María Tárano, Hannah Kerner (2026). [Multi-Head LatentMoE and Head Parallel: Communication-Efficient and Deterministic MoE Parallelism](https://arxiv.org/abs/2602.04870). arXiv:2602.04870.
<a id="ref-2401.06066"></a>10. Damai Dai, Chengqi Deng, Chenggang Zhao, R. X. Xu, Huazuo Gao et al. (2024). [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066). arXiv:2401.06066.
<a id="ref-doc-1"></a>11. DeepSeek-AI. [DeepSeek V4.1 Flash 大规模推理部署实践 (the DeepInfer release post)](https://zhuanlan.zhihu.com/p/2095560295930508953). Zhihu.
<a id="ref-doc-2"></a>12. DeepSeek-AI. [DeepSeek V4.1 Flash Inference Deployment Q\&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md). GitHub, deepseek-ai/DeepInfer.
<a id="ref-doc-3"></a>13. DeepSeek-AI. [DeepInfer](https://github.com/deepseek-ai/DeepInfer). GitHub.
<a id="ref-2405.04434"></a>14. DeepSeek-AI, Aixin Liu, Bei Feng, Bin Wang, Bingxuan Wang et al. (2024). [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434). arXiv:2405.04434.
<a id="ref-2412.19437"></a>15. DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang et al. (2024). [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437). arXiv:2412.19437.
<a id="ref-2606.19348"></a>16. DeepSeek-AI, Anyi Xu, Bangcai Lin, Bing Xue, Bingxuan Wang et al. (2026). [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348). arXiv:2606.19348.
<a id="ref-2609.19969"></a>17. DeepSeek-AI, Anyi Xu, B. Li, Bangcai Lin, Bing Xue et al. (2026). [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969). arXiv:2609.19969.
<a id="ref-2511.11505"></a>18. Yonatan Dukler, Guihong Li, Deval Shah, Jiang Liu, Vikram Appia et al. (2025). [FarSkip-Collective: Unhobbling Blocking Communication in Mixture of Experts Models](https://arxiv.org/abs/2511.11505). arXiv:2511.11505.
<a id="ref-2601.18089"></a>19. Venmugil Elango, Nidhi Bhatia, Roger Waleffe, Rasoul Shafipour, Tomer Asida et al. (2026). [LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts](https://arxiv.org/abs/2601.18089). arXiv:2601.18089.
<a id="ref-doc-0"></a>20. Hugging Face (2025). [The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/).
<a id="ref-2101.03961"></a>21. William Fedus, Barret Zoph, Noam Shazeer (2021). [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961). arXiv:2101.03961.
<a id="ref-2211.15841"></a>22. Trevor Gale, Deepak Narayanan, Cliff Young, Matei Zaharia (2022). [MegaBlocks: Efficient Sparse Training with Mixture-of-Experts](https://arxiv.org/abs/2211.15841). arXiv:2211.15841.
<a id="ref-2602.15763"></a>23. GLM-5-Team, Aohan Zeng, Xin Lv, Zhenyu Hou, Zhengxiao Du et al. (2026). [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763). arXiv:2602.15763.
<a id="ref-2509.21892"></a>24. Naibin Gu, Zhenyu Zhang, Yuchen Feng, Yilong Chen, Peng Fu et al. (2025). [Elastic MoE: Unlocking the Inference-Time Scalability of Mixture-of-Experts](https://arxiv.org/abs/2509.21892). arXiv:2509.21892.
<a id="ref-2609.13058"></a>25. Hongyi He, Zhenghao Lin, Xiao Liu, Peng Cheng, Yan Lu et al. (2026). [Expert-Space Exploration in MoE Reinforcement Learning](https://arxiv.org/abs/2609.13058). arXiv:2609.13058.
<a id="ref-2203.15556"></a>26. Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai et al. (2022). [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556). arXiv:2203.15556.
<a id="ref-2512.16248"></a>27. Qingguo Hu, Zhenghao Lin, Ziyue Yang, Yucheng Ding, Xiao Liu et al. (2025). [Sigma-MoE-Tiny Technical Report](https://arxiv.org/abs/2512.16248). arXiv:2512.16248.
<a id="ref-2602.10604"></a>28. Ailin Huang, Ang Li, Aobo Kong, Bin Wang, Binxing Jiao et al. (2026). [Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters](https://arxiv.org/abs/2602.10604). arXiv:2602.10604.
<a id="ref-2605.25704"></a>29. Peijie Jiang, Yuqi Feng, Cunyin Peng, Qian Zhao, Jia Liu et al. (2026). [PowLU: An Activation Function for Stable Pre-Training of LLMs](https://arxiv.org/abs/2605.25704). arXiv:2605.25704.
<a id="ref-2609.39137"></a>30. Peng Jin, Zihan Qiu, Zekun Wang, Bo Zheng, Yang Xu et al. (2026). [ID Balancing: Stable Training of Extremely Sparse MoE via PID-Based Load Control](https://arxiv.org/abs/2609.39137). arXiv:2609.39137.
<a id="ref-2605.31268"></a>31. Marko Kojic, Ivan Bondyrev, Aral de Moor, Joseph Shtok, Petr Borovlev et al. (2026). [Mellum2 Technical Report](https://arxiv.org/abs/2605.31268). arXiv:2605.31268.
<a id="ref-2212.05055"></a>32. Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp, Carlos Riquelme Ruiz, Basil Mustafa et al. (2022). [Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints](https://arxiv.org/abs/2212.05055). arXiv:2212.05055.
<a id="ref-2506.02890"></a>33. Jakub Krajewski, Marcin Chochowski, Daniel Korzekwa (2025). [Scaling Fine-Grained MoE Beyond 50B Parameters: Empirical Evaluation and Practical Insights](https://arxiv.org/abs/2506.02890). arXiv:2506.02890.
<a id="ref-doc-12"></a>34. AWS Labs. [awsome-distributed-ai, NCCL test recipes](https://github.com/awslabs/awsome-distributed-ai/tree/main/micro-benchmarks/nccl-tests). GitHub.
<a id="ref-2605.18106"></a>35. Tim Tsz-Kit Lau, Weijie Su (2026). [Symmetry-Compatible Principle for Optimizer Design: Embeddings, LM Heads, SwiGLU MLPs, and MoE Routers](https://arxiv.org/abs/2605.18106). arXiv:2605.18106.
<a id="ref-2605.11689"></a>36. Margaret Li, Sneha Kudugunta, Danielle Rothermel, Luke Zettlemoyer (2026). [Slicing and Dicing: Configuring Optimal Mixtures of Experts](https://arxiv.org/abs/2605.11689). arXiv:2605.11689.
<a id="ref-2601.08215"></a>37. Seng Pei Liew, Kenta Shinzato, Yuyang Dong (2026). [Towards Principled Design of Mixture-of-Experts Language Models under Memory and Inference Constraints](https://arxiv.org/abs/2601.08215). arXiv:2601.08215.
<a id="ref-2608.09119"></a>38. Junghwan Lim, Joon Son Chung, Sungmin Lee, Wai Ting Cheung, Gihun Cho et al. (2026). [Motif 3: Technical Report](https://arxiv.org/abs/2608.09119). arXiv:2608.09119.
<a id="ref-2502.16982"></a>39. Jingyuan Liu, Jianlin Su, Xingcheng Yao, Zhejun Jiang, Guokun Lai et al. (2025). [Muon is Scalable for LLM Training](https://arxiv.org/abs/2502.16982). arXiv:2502.16982.
<a id="ref-2609.00791"></a>40. Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra, Yonatan Dukler, Gowtham Ramesh et al. (2026). [Instella-MoE Technical Report](https://arxiv.org/abs/2609.00791). arXiv:2609.00791.
<a id="ref-2510.11370"></a>41. Wenhan Ma, Hailin Zhang, Liang Zhao, Yifan Song, Yudong Wang et al. (2025). [Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370). arXiv:2510.11370.
<a id="ref-2409.02060"></a>42. Niklas Muennighoff, Luca Soldaini, Dirk Groeneveld, Kyle Lo, Jacob Morrison et al. (2024). [OLMoE: Open Mixture-of-Experts Language Models](https://arxiv.org/abs/2409.02060). arXiv:2409.02060.
<a id="ref-2609.28053"></a>43. Pit Neitemeier, Jiaze Li, Alessio Serra, Philipp Scholl, Sohir Maskey (2026). [Exact Quantile Balancing and Load-Error Injection for Mixture-of-Experts](https://arxiv.org/abs/2609.28053). arXiv:2609.28053.
<a id="ref-doc-10"></a>44. NVIDIA. [enroot](https://github.com/NVIDIA/enroot). GitHub.
<a id="ref-doc-11"></a>45. NVIDIA. [nccl-tests](https://github.com/NVIDIA/nccl-tests). GitHub.
<a id="ref-doc-6"></a>46. NVIDIA. [Megatron-LM PR #1913, feat(moe): Fine-grained activation offloading](https://github.com/NVIDIA/Megatron-LM/pull/1913). GitHub.
<a id="ref-doc-7"></a>47. NVIDIA. [DCGM Diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html). DCGM documentation.
<a id="ref-doc-9"></a>48. NVIDIA. [pyxis](https://github.com/NVIDIA/pyxis). GitHub.
<a id="ref-2509.25149"></a>49. NVIDIA, Felix Abecassis, Anjulie Agrusa, Dong Ahn, Jonah Alben et al. (2025). [Pretraining Large Language Models with NVFP4](https://arxiv.org/abs/2509.25149). arXiv:2509.25149.
<a id="ref-2604.12374"></a>50. NVIDIA, Aakshita Chandiramani, Aaron Blakeman, Abdullahi Olaoye, Abhibha Gupta et al. (2026). [Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2604.12374). arXiv:2604.12374.
<a id="ref-2606.15007"></a>51. NVIDIA, Aaron Blakeman, Aaron Thomas, Aastha Jhunjhunwala, Abhibha Gupta et al. (2026). [Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2606.15007). arXiv:2606.15007.
<a id="ref-2508.10925"></a>52. OpenAI, Sandhini Agarwal, Lama Ahmad, Jason Ai, Sam Altman et al. (2025). [gpt-oss-120b \& gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925). arXiv:2508.10925.
<a id="ref-2601.07022"></a>53. Sungrae Park, Sanghoon Kim, Jungho Cho, Gyoungjin Gim, Dawoon Jung et al. (2026). [Solar Open Technical Report](https://arxiv.org/abs/2601.07022). arXiv:2601.07022.
<a id="ref-2501.11873"></a>54. Zihan Qiu, Zeyu Huang, Bo Zheng, Kaiyue Wen, Zekun Wang et al. (2025). [Demons in the Detail: On Implementing Load Balancing Loss for Training Specialized Mixture-of-Expert Models](https://arxiv.org/abs/2501.11873). arXiv:2501.11873.
<a id="ref-2608.04502"></a>55. Chengyu Qiu, Xiao Fu, Fengcun Li, Yulei Qian, Yuchen Xie et al. (2026). [AFD-Ledger: Deployment Provisioning for Attention--FFN Disaggregation](https://arxiv.org/abs/2608.04502). arXiv:2608.04502.
<a id="ref-2608.30320"></a>56. Zihan Qiu, Zekun Wang, Xiao Li, Yanpeng Li, Yang Xu et al. (2026). [On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability](https://arxiv.org/abs/2608.30320). arXiv:2608.30320.
<a id="ref-2106.04426"></a>57. Stephen Roller, Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston (2021). [Hash Layers For Large Sparse Models](https://arxiv.org/abs/2106.04426). arXiv:2106.04426.
<a id="ref-2608.10605"></a>58. Soumajyoti Sarkar, Yuxin Tang, Sheng Zha (2026). [Compute-Optimal Is Not Cluster-Optimal: Systems-Aware Scaling for Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.10605). arXiv:2608.10605.
<a id="ref-1701.06538"></a>59. Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le et al. (2017). [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538). arXiv:1701.06538.
<a id="ref-doc-8"></a>60. StepFun. [Inside Step 5 Preview](https://platform.stepfun.ai/blog/inside-step-5-preview). blog.
<a id="ref-2507.19427"></a>61. StepFun, Bin Wang, Bojun Wang, Changyi Wan, Guanzhe Huang et al. (2025). [Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding](https://arxiv.org/abs/2507.19427). arXiv:2507.19427.
<a id="ref-2409.12210"></a>62. Manxi Sun, Wei Liu, Jian Luan, Pengzhi Gao, Bin Wang (2024). [Mixture of Diverse Size Experts](https://arxiv.org/abs/2409.12210). arXiv:2409.12210.
<a id="ref-2603.11535"></a>63. Hanchi Sun, Yixin Liu, Yonghui Wu, Lichao Sun (2026). [Expert Threshold Routing for Autoregressive Language Modeling with Dynamic Computation Allocation and Load Balancing](https://arxiv.org/abs/2603.11535). arXiv:2603.11535.
<a id="ref-2505.04519"></a>64. Yehui Tang, Yichun Yin, Yaoyuan Wang, Hang Zhou, Yu Pan et al. (2025). [Pangu Ultra MoE: How to Train Your Big MoE on Ascend NPUs](https://arxiv.org/abs/2505.04519). arXiv:2505.04519.
<a id="ref-2505.21411"></a>65. Yehui Tang, Xiaosong Li, Fangcheng Liu, Wei Guo, Hang Zhou et al. (2025). [Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity](https://arxiv.org/abs/2505.21411). arXiv:2505.21411.
<a id="ref-doc-5"></a>66. Kimi Team. [Kimi K3 tech report](https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf). GitHub, MoonshotAI/Kimi-K3.
<a id="ref-2509.01322"></a>67. Meituan LongCat Team, Bayan, Bei Li, Bingye Lei, Bo Wang et al. (2025). [LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322). arXiv:2509.01322.
<a id="ref-2510.22115"></a>68. Ling Team, Ang Li, Ben Liu, Binbin Hu, Bing Li et al. (2025). [Every Activation Boosted: Scaling General Reasoner to 1 Trillion Open Language Foundation](https://arxiv.org/abs/2510.22115). arXiv:2510.22115.
<a id="ref-2607.24653"></a>69. Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, M. C. et al. (2026). [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653). arXiv:2607.24653.
<a id="ref-2610.11959"></a>70. Xiaomi LLM-Core Team, Zongming Qiao, Ziyue Hua, Zirui Ou, Zihao Yue et al. (2026). [MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://arxiv.org/abs/2610.11959). arXiv:2610.11959.
<a id="ref-2507.17702"></a>71. Changxin Tian, Kunlong Chen, Jia Liu, Ziqi Liu, Zhiqiang Zhang et al. (2025). [Towards Greater Leverage: Scaling Laws for Efficient Mixture-of-Experts Language Models](https://arxiv.org/abs/2507.17702). arXiv:2507.17702.
<a id="ref-2412.09952"></a>72. Aditya Vavre, Ethan He, Dennis Liu, Zijie Yan, June Yang et al. (2024). [Llama 3 Meets MoE: Efficient Upcycling](https://arxiv.org/abs/2412.09952). arXiv:2412.09952.
<a id="ref-2408.10681"></a>73. An Wang, Xingwu Sun, Ruobing Xie, Shuaipeng Li, Jiaqi Zhu et al. (2024). [HMoE: Heterogeneous Mixture of Experts for Language Modeling](https://arxiv.org/abs/2408.10681). arXiv:2408.10681.
<a id="ref-2408.15664"></a>74. Lean Wang, Huazuo Gao, Chenggang Zhao, Xu Sun, Damai Dai (2024). [Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664). arXiv:2408.15664.
<a id="ref-2602.04705"></a>75. Haifeng Wang, Hua Wu, Tian Wu, Yu Sun, Jing Liu et al. (2026). [ERNIE 5.0 Technical Report](https://arxiv.org/abs/2602.04705). arXiv:2602.04705.
<a id="ref-2406.06563"></a>76. Tianwen Wei, Bo Zhu, Liang Zhao, Cheng Cheng, Biye Li et al. (2024). [Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models](https://arxiv.org/abs/2406.06563). arXiv:2406.06563.
<a id="ref-2508.07785"></a>77. Haoyuan Wu, Haoxing Chen, Xiaodong Chen, Zhanchao Zhou, Tieyuan Chen et al. (2025). [Grove MoE: Towards Efficient and Superior MoE LLMs with Adjugate Experts](https://arxiv.org/abs/2508.07785). arXiv:2508.07785.
<a id="ref-2608.27874"></a>78. Weicheng Xue, Bingqiang Wang, Li Yuan, Huihui Zhou, Yonghong Tian (2026). [TerraceMoE: A Cost Model for Hierarchical MoE All-to-All Communication](https://arxiv.org/abs/2608.27874). arXiv:2608.27874.
<a id="ref-2603.07685"></a>79. Zijie Yan, Hongxiao Bai, Xin Yao, Dennis Liu, Tong Liu et al. (2026). [Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685). arXiv:2603.07685.
<a id="ref-2505.09388"></a>80. An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui et al. (2025). [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388). arXiv:2505.09388.
<a id="ref-2601.14327"></a>81. YuanLab.ai, Shawn Wu, Jiangang Luo, Darcy Chen, Sean Wang et al. (2026). [Yuan3.0 Ultra: A Trillion-Parameter Enterprise-Oriented MoE LLM](https://arxiv.org/abs/2601.14327). arXiv:2601.14327.
<a id="ref-2603.02731"></a>82. Wuyue Zhang, Chongdong Huang, Chunbo You, Cheng Gu, Fengjuan Wang et al. (2026). [Practical FP4 Training for Large-Scale MoE Models on Hopper GPUs](https://arxiv.org/abs/2603.02731). arXiv:2603.02731.
<a id="ref-2507.18071"></a>83. Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu et al. (2025). [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071). arXiv:2507.18071.
<a id="ref-2512.01374"></a>84. Chujie Zheng, Kai Dang, Bowen Yu, Mingze Li, Huiqiang Jiang et al. (2025). [Stabilizing Reinforcement Learning with LLMs: Formulation and Practices](https://arxiv.org/abs/2512.01374). arXiv:2512.01374.
<a id="ref-2202.09368"></a>85. Yanqi Zhou, Tao Lei, Hanxiao Liu, Nan Du, Yanping Huang et al. (2022). [Mixture-of-Experts with Expert Choice Routing](https://arxiv.org/abs/2202.09368). arXiv:2202.09368.
<a id="ref-2504.02263"></a>86. Ruidong Zhu, Ziheng Jiang, Chao Jin, Peng Wu, Cesar A. Stuardo et al. (2025). [MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism](https://arxiv.org/abs/2504.02263). arXiv:2504.02263.
<a id="ref-2607.15810"></a>87. Zhengyang Zhuge, Hao Yu, Xin Wang, Zheng Li, Yizhong Cao et al. (2026). [QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810). arXiv:2607.15810.
<a id="ref-2411.03884"></a>88. Zhijian Zhuo, Ya Wang, Yutao Zeng, Xiaoqing Li, Xun Zhou et al. (2024). [Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://arxiv.org/abs/2411.03884). arXiv:2411.03884.
<a id="ref-2202.08906"></a>89. Barret Zoph, Irwan Bello, Sameer Kumar, Nan Du, Yanping Huang et al. (2022). [ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906). arXiv:2202.08906.

### Code, configs and data

<a id="ref-src-cfg-moe-every"></a>1. An MoE in every layer, [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B/blob/ad44e777bcd18fa416d9da3bd8f70d33ebb85d39/config.json).
<a id="ref-src-trinity-centered"></a>2. Arcee AI, 2026, *Arcee Trinity Large Technical Report*, arXiv:2602.17004, §2.3.
<a id="ref-src-aa-open-top"></a>3. Artificial Analysis Intelligence Index v5.0.1, [open-weights models](https://artificialanalysis.ai/models/open-source).
<a id="ref-src-engram-s23"></a>4. Cheng et al., 2026, *Conditional Memory via Scalable Lookup*, arXiv:2601.07372, §2.2 (suffix N-grams of canonical token ids, retrieved by hashing into embedding tables) and §2.3.
<a id="ref-src-lexi-gate"></a>5. Chitty-Venkata, Madireddy, Emani and Vishwanath, 2025, *LExI: Layer-Adaptive Active Experts for Efficient MoE Model Inference*, arXiv:2509.02753.
<a id="ref-src-parallel-block"></a>6. [`CohereLabs/North-Mini-Code-1.0`](https://huggingface.co/CohereLabs/North-Mini-Code-1.0/blob/d11e61a842617a22dc328552fa5bb86231ee4f37/config.json).
<a id="ref-src-datatrove-skip"></a>7. datatrove, `src/datatrove/executor/base.py` [L30](https://github.com/huggingface/datatrove/blob/2c895af7a95010a96fa53e2dc77cc0ce92799e3f/src/datatrove/executor/base.py#L30).
<a id="ref-src-v32-keep-routing"></a>8. DeepSeek-AI, 2025, *DeepSeek-V3.2*, arXiv:2512.02556.
<a id="ref-src-deepep-readme"></a>9. DeepSeek-AI, DeepEP README at tag v1.2.1.
<a id="ref-src-cfg-dsv3"></a>10. DeepSeek-V3 [`config.json`](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/e815299b0bcbac849fa540c768ef21845365c9eb/config.json).
<a id="ref-src-cfg-v4flash-rs"></a>11. DeepSeek-V4-Flash [`config.json`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/60d8d70770c6776ff598c94bb586a859a38244f1/config.json).
<a id="ref-src-dsv4-gate-code"></a>12. DeepSeek-V4-Pro Hub `inference/model.py`, `Gate` ([L546](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/b5968e9190ef611bbf34a7229255be88a0e937c1/inference/model.py#L546)).
<a id="ref-src-hub-dsv4pro-route"></a>13. DeepSeek-V4-Pro's own inference code, [`model.py#L556`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/b5968e9190ef611bbf34a7229255be88a0e937c1/inference/model.py#L556) (hash routing when `layer_id < n_hash_layers`).
<a id="ref-src-hub-v41-engram"></a>14. DeepSeek-V4.1-Flash on the Hub (rev 314113f), [`inference/engram.py#L90`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/314113f8a7dadb388215396ba5fbee2c610a04d6/inference/engram.py#L90).
<a id="ref-src-hub-dsv41"></a>15. DeepSeek-V4.1-Flash's own inference code, [`model.py#L811`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/2cba9e42aa026125f3ed06c6d98c1db82f7ca027/inference/model.py#L811) (router GEMM in fp32, divided by `gate_temp`, 1.0 by default).
<a id="ref-src-emo-init"></a>16. EMO, 2026, arXiv:2605.13247, §3.3.
<a id="ref-src-expup-copy"></a>17. Expert Upcycling, 2026, arXiv:2604.19835, Definition 3.1.
<a id="ref-src-expup-drop"></a>18. Expert Upcycling, arXiv:2604.19835, App. D, Tables 9 and 11\.
<a id="ref-src-shape-glm53"></a>19. GLM-5.3 publisher [`config.json`](https://huggingface.co/zai-org/GLM-5.3/blob/main/config.json).
<a id="ref-src-grok2-parallel"></a>20. Grok 2, [`config.json`](https://huggingface.co/xai-org/grok-2/blob/main/config.json).
<a id="ref-src-grok2-softcap"></a>21. Grok 2, [`config.json`](https://huggingface.co/xai-org/grok-2/blob/daf4395a80ad177386cfe39641b64fc12b1d70ed/config.json).
<a id="ref-src-hf-jobs-hardware"></a>22. `hf jobs hardware`.
<a id="ref-src-cfg-swiglu"></a>23. `hidden_act: silu` with gated experts in [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/e815299b0bcbac849fa540c768ef21845365c9eb/config.json).
<a id="ref-src-lowbit-all-cfg"></a>24. Hub config.json `quantization_config`, [`Qwen/Qwen3-30B-A3B-GPTQ-Int4`](https://huggingface.co/Qwen/Qwen3-30B-A3B-GPTQ-Int4/blob/9b534e4318b7ebc3c961a839f13eb18b1833f441/config.json).
<a id="ref-src-lowbit-experts-cfg"></a>25. Hub config.json `quantization_config`, [`Zyphra/ZAYA1-8B-MXFP4-Experts`](https://huggingface.co/Zyphra/ZAYA1-8B-MXFP4-Experts/blob/d8602cda89e0f5f8ff268593778f4f27c8cbfe65/config.json).
<a id="ref-src-hub-gated"></a>26. Hugging Face Hub API, [`api/models/meta-llama/Llama-3.2-1B`](https://huggingface.co/api/models/meta-llama/Llama-3.2-1B).
<a id="ref-src-hf-jobs-pricing"></a>27. Hugging Face, [Jobs, Pricing and Billing](https://huggingface.co/docs/hub/jobs-pricing).
<a id="ref-src-hf-jobs-guide"></a>28. Hugging Face, [Run and manage Jobs](https://huggingface.co/docs/huggingface_hub/en/guides/jobs).
<a id="ref-src-interns1pro-s21"></a>29. Intern-S1-Pro, 2026, *Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale*, arXiv:2603.25040, §2.1 Group Routing.
<a id="ref-src-cfg-k3"></a>30. Kimi K3 [`config.json`](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/config.json).
<a id="ref-src-hub-kimi-k3"></a>31. Kimi K3's repo code, [`modeling_kimi_linear.py#L707-L712`](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/modeling_kimi_linear.py#L707-L712) (router GEMM in fp32, sigmoid).
<a id="ref-src-hub-kimi-k3-route"></a>32. Kimi K3's repo code, [`modeling_kimi_linear.py#L724`](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/modeling_kimi_linear.py#L724).
<a id="ref-src-k25-mask"></a>33. Kimi Team, 2026, *Kimi K2.5: Visual Agentic Intelligence*, arXiv:2602.02276.
<a id="ref-src-kimivl-bias"></a>34. Kimi-VL-A3B-Instruct publisher [`config.json`](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct/blob/main/config.json).
<a id="ref-src-kexaone-peak"></a>35. LG AI Research, 2026, *K-EXAONE 2.0 Technical Report*, arXiv:2608.04505, §2.2 Training stability.
<a id="ref-src-kexaone-grow"></a>36. LG AI Research, 2026, *K-EXAONE 2.0 Technical Report*, arXiv:2608.04505, §2.2.
<a id="ref-src-longcat-ngram-f2"></a>37. Liu et al. (Meituan LongCat), 2026, *Scaling Embeddings Outperforms Scaling Experts in Language Models*, arXiv:2601.21204, Fig. 2 and §3.2.1, 280M active parameters, 300B tokens.
<a id="ref-src-flashlite-ngram"></a>38. Liu et al. (Meituan LongCat), 2026, *Scaling Embeddings Outperforms Scaling Experts in Language Models*, arXiv:2601.21204, §6, [`config.json`](https://huggingface.co/meituan-longcat/LongCat-Flash-Lite/blob/b62b68827ead0b7fef3ba98b57f18484acaaec06/config.json).
<a id="ref-src-shape-mimo26"></a>39. MiMo-V2.6-Pro-RL publisher [`config.json`](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/config.json), text configuration.
<a id="ref-src-hub-mimo26"></a>40. MiMo-V2.6-Pro-RL's repo code, [`modeling_mimo_v2.py#L155`](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/modeling_mimo_v2.py#L155) (router GEMM in fp32).
<a id="ref-src-cfg-mistral-large3"></a>41. `mistralai/Mistral-Large-3-675B-Instruct-2512` [`params.json`](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512/blob/383ffea2c7d60dfd44ca960e8e691709d4fdb9cd/params.json).
<a id="ref-src-cfg-mixtral"></a>42. `mistralai/Mixtral-8x7B-v0.1` [`config.json`](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1/blob/fc7ac94680e38d7348cfa806e51218e6273104b0/config.json).
<a id="ref-src-dropup-r"></a>43. Nakamura et al., 2025, *Drop-Upcycling*, arXiv:2502.19261, §5.
<a id="ref-src-shape-nemotron-ultra"></a>44. Nemotron 3 Ultra publisher [`config.json`](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4/blob/main/config.json).
<a id="ref-src-nemorl-freeze"></a>45. NVIDIA NeMo-RL at fb121a00, [`examples/nemo_gym/nemotron-3-super/stage1_rlvr.yaml#L59-L61`](https://github.com/NVIDIA-NeMo/RL/blob/fb121a00d6b49cffd59e9e13e6c92215008b948e/examples/nemo_gym/nemotron-3-super/stage1_rlvr.yaml#L59-L61) (`async_grpo: enabled: true`, `max_trajectory_age_steps: 1`).
<a id="ref-src-cfg-granularity"></a>46. Publisher configs (hidden size / routed expert width, experts / top-k), [`config.json`](https://huggingface.co/openai/gpt-oss-120b/blob/b5c939de8f754692c1647ca79fbf85e8c1e70f8a/config.json).
<a id="ref-src-cfg-latent"></a>47. Publisher configs, [`config.json`](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16/blob/2dc98e2afe4face0e4ce40972a915c45368bd34a/config.json).
<a id="ref-src-torch-topk"></a>48. PyTorch `torch.topk` documentation.
<a id="ref-src-cfg-qwen3next"></a>49. `Qwen/Qwen3-Next-80B-A3B-Instruct` [`config.json`](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct/blob/9c7f2fbe84465e40164a94cc16cd30b6999b0cc7/config.json).
<a id="ref-src-cfg-qwen35"></a>50. Qwen3.5-397B [`config.json`](https://huggingface.co/Qwen/Qwen3.5-397B-A17B/blob/8472618112abcbd45acbcdc58436aff4233c23f7/config.json).
<a id="ref-src-shape-qwen38"></a>51. Qwen3.8-2.4T-A95B publisher [`config.json`](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/config.json).
<a id="ref-src-hub-q38-ngram"></a>52. Qwen3.8-Flash-Next on the Hub (rev de4b8e4), [`modeling_qwen4_exp.py#L1262`](https://github.com/huggingface/transformers/blob/a672eb5f474b8b30173e9f96eab66adf292da635/src/transformers/models/qwen4_exp/modeling_qwen4_exp.py#L1262).
<a id="ref-src-ckpt-bias-means"></a>53. Released weights, one tensor range-read per layer from each safetensors file, [DeepSeek-V3-Base](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base).
<a id="ref-src-fp32-router-code"></a>54. Router GEMM cast to fp32 in inference code, [`modeling_deepseek_v32.py#L512`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/deepseek_v32/modeling_deepseek_v32.py#L512).
<a id="ref-src-shape-step5"></a>55. Step 5 Preview publisher [`config.json`](https://huggingface.co/stepfun-ai/Step-5-Preview-BF16/blob/main/config.json), text configuration.
<a id="ref-src-hub-step5-router"></a>56. Step-5-Preview on the Hub (`stepfun-ai/Step-5-Preview`, rev 364b3b0), [`inference/model.py#L2020-L2030`](https://huggingface.co/stepfun-ai/Step-5-Preview/blob/364b3b03fed2477aa0953fe855a2c4c8c48ee3cc/inference/model.py#L2020-L2030).
<a id="ref-src-hub-step5-route"></a>57. Step-5-Preview on the Hub (`stepfun-ai/Step-5-Preview`, rev 364b3b0), [`inference/model.py#L2021-L2025`](https://huggingface.co/stepfun-ai/Step-5-Preview/blob/364b3b03fed2477aa0953fe855a2c4c8c48ee3cc/inference/model.py#L2021-L2025).
<a id="ref-src-su-qb"></a>58. Su Jianlin, kexue.fm post 11619, "MoE环游记：6、最优分配促均衡".
<a id="ref-src-su-k3"></a>59. Su Jianlin, kexue.fm post 11848, "简单谈谈K3的MoE和Attention".
<a id="ref-src-cfg-clamp10"></a>60. `swiglu_limit: 10` in [`ai-sage/GigaChat3.5-432B-A28B`](https://huggingface.co/ai-sage/GigaChat3.5-432B-A28B/blob/d10dcaeccb04ca3186fdfa3bb3874b4474e6b41b/config.json).
<a id="ref-src-trackio-readme"></a>61. Trackio [`README.md`](https://github.com/gradio-app/trackio/blob/4bef24c5fd2db622c41cce7c763be504116281a2/README.md) at 4bef24c.
<a id="ref-src-tf-cohere2-moe"></a>62. transformers `cohere2_moe` at main ff704ff, [`modeling_cohere2_moe.py#L150-L160`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/cohere2_moe/modeling_cohere2_moe.py#L150-L160).
<a id="ref-src-tf-gemma4"></a>63. transformers `gemma4` at main ff704ff, `Gemma4TextRouter`, [`modeling_gemma4.py#L1323`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/gemma4/modeling_gemma4.py#L1323-L1324).
<a id="ref-src-tf-glm-moe-dsa"></a>64. transformers `glm_moe_dsa` at main ff704ff, [`modeling_glm_moe_dsa.py#L485`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/glm_moe_dsa/modeling_glm_moe_dsa.py#L485).
<a id="ref-src-tf-inkling"></a>65. transformers `inkling` at main ff704ff, [`modeling_inkling.py#L360`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/inkling/modeling_inkling.py#L360).
<a id="ref-src-hub-llama4-route"></a>66. transformers `llama4` at main ff704ff, [`modeling_llama4.py#L146-L148`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/llama4/modeling_llama4.py#L146-L148).
<a id="ref-src-tf-llama4"></a>67. transformers `llama4` at main ff704ff, [`modeling_llama4.py#L150`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/llama4/modeling_llama4.py#L150).
<a id="ref-src-hf-qwen3moe"></a>68. transformers main at a96730c8, [`qwen3_moe/modeling_qwen3_moe.py#L257-L264`](https://github.com/huggingface/transformers/blob/a96730c8c97b8efbf35bbaf7f5da33ec99231a49/src/transformers/models/qwen3_moe/modeling_qwen3_moe.py#L257-L264).
<a id="ref-src-tf-qwen4-exp"></a>69. transformers `qwen4_exp` at main ff704ff, [`modeling_qwen4_exp.py#L964`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/qwen4_exp/modeling_qwen4_exp.py#L964).
<a id="ref-src-tf-zaya"></a>70. transformers `zaya` at main ff704ff, [`modeling_zaya.py#L538`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/zaya/modeling_zaya.py#L538).
<a id="ref-src-trl-is"></a>71. TRL, `trl/trainer/grpo_config.py` at 3749f2a, [`importance_sampling_level`](https://github.com/huggingface/trl/blob/3749f2a59fdcd3b6435243faa44eedf2903bc30e/trl/trainer/grpo_config.py#L208-L213).
<a id="ref-src-cfg-maverick"></a>72. `unsloth/Llama-4-Maverick-17B-128E-Instruct` [`config.json`](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct/blob/86c5ecb6f2fbddf604c60120125fb202e09f2556/config.json), `text_config`.
<a id="ref-src-vllm-dbo"></a>73. vLLM at 790be385, [`vllm/config/parallel.py#L275-L276`](https://github.com/vllm-project/vllm/blob/790be385c8a69f45ec9a7a85ef00836d1684060f/vllm/config/parallel.py#L275-L276).
<a id="ref-src-ultraep-f11"></a>74. Wei et al., 2026, *UltraEP*, arXiv:2606.04101, §8.2 and Fig. 11 (training, resumed at global batch 3,500 for 20 more).
<a id="ref-src-dsvl2-bias"></a>75. Wu et al., 2024, *DeepSeek-V*, arXiv:2412.10302, §2.
<a id="ref-src-mimo-r3"></a>76. Xiaomi, 2026, *MiMo-V2-Flash Technical Report*, arXiv:2601.02780.
<a id="ref-src-cfg-glm45air"></a>77. `zai-org/GLM-4.5-Air` [`config.json`](https://huggingface.co/zai-org/GLM-4.5-Air/blob/a24ceef6ce4f3536971efe9b778bdaa1bab18daa/config.json).
<a id="ref-src-zaya1-adamw"></a>78. Zyphra, 2026, *ZAYA1-8B Technical Report*, arXiv:2605.05365, §II-A2.

<a id="fn-pop"></a>
