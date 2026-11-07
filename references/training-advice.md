# Apply the handbook to a training plan

Use this as a decision guide; follow linked sections for the full evidence and exact recipes. The numerical settings in the handbook belong to its pinned experiment, not a default for every model.

## Establish a comparison

Read [setup and the first MoE](../src/chapters/2-setup-and-your-first-run.md#s-2) before adapting the launch scripts. Identify model objective, hardware/topology, framework revision, data/tokenizer, token budget, precision, sequence and batch sizes, and distributed layout from the available artifacts. Ask only for missing facts that change the recommendation.

Validate the data path and a dense baseline, then the dense-to-MoE sanity checks in [§2.5](../src/chapters/2-setup-and-your-first-run.md#s-2-5). Increasing total parameters while holding active parameters roughly fixed changes memory and communication even when token compute is similar. State the comparison budget before recommending an architecture.

For a gated expert with model width `d` and intermediate width `h`, its three weight matrices contribute approximately `3*d*h` parameters, excluding biases. Count shared experts and dense layers separately. Total routed-expert parameters scale with expert count `E`; active routed-expert parameters scale with selected count `k`. Neither is the entire model's count or a complete FLOPs estimate. See the worked example and [expert granularity](../src/chapters/3-anatomy-of-moe-training.md#s-3-4-count-and-size).

## Choose architecture and routing

- In [scoring](../src/chapters/3-anatomy-of-moe-training.md#s-3-1), distinguish which experts win from how their outputs are weighted. Softmax placement, selected-weight renormalization and an output scaling factor can change output magnitude without changing selected expert identities. Diagnose flat selected weights using actual reconstructed weights and the run's score function.
- In [routing strategy](../src/chapters/3-anatomy-of-moe-training.md#s-3-2), separate learned token choice, expert choice and hash routing. An expert-choice training result does not imply identical inference behavior; a bias controller cannot rebalance a fixed hash assignment.
- In [balancing](../src/chapters/3-anatomy-of-moe-training.md#s-3-3), choose the scope of balance deliberately: device, expert, sequence, micro-batch and global batch describe different constraints. Stronger auxiliary loss can trade language-model quality for balance. Bias-based control has an adaptation rate and can lag; assess its evolution before changing its rule.
- More, smaller experts can reduce GEMM efficiency and increase dispatch costs. Shared experts add active computation when added on top of routed `k`; latent experts add projections and different normalization needs. Read [§3.4](../src/chapters/3-anatomy-of-moe-training.md#s-3-4) before assuming these are free capacity.
- The first MoE layers and block wiring can affect both stability and overlap. Consider [dense placement and layout](../src/chapters/3-anatomy-of-moe-training.md#s-3-5) using evidence from the intended architecture rather than transferring a frontier model's choices wholesale.
- Treat upcycling, optimizer updates, MTP and activation controls as separate interventions with their own compatibility and cost. Use [§3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6); preserve its distinction between observed failures, upstream bugs and generally applicable principles.

## Diagnose before changing the recipe

| Observation | First discriminating check | Intervention to evaluate |
| --- | --- | --- |
| Aux loss near 1, one GPU slow | Per-layer expert counts and device counts, including zero-load experts; micro-batch and global scopes | Address demonstrated imbalance or placement, then profile communication; do not declare balance from aux loss alone |
| Multi-node slowdown, NCCL says `Using network Socket` | Verify the intended transport and all-to-all performance at the actual node count | Fix the network/container path before architecture tuning; the source's slowdown factor is experiment-specific |
| Exposed all-to-all despite sound balance | Warmed-up step profile, dispatch/combine timing, token destination fan-out | Evaluate EP placement, group-limited routing and compatible overlap; quantify quality and communication tradeoffs |
| OOM on one rank while reported peak looks fine | Peak allocated memory on every rank over the same reset interval; busiest rank's token load | Resolve imbalance if present, otherwise evaluate the memory interventions and compatibility constraints in §3.7 |
| NaN without prior movement in z-loss or norms | Earliest failing operation, rerun outcome on a different GPU, checkpoint/data reproducibility | Follow §3.6 rerun diagnosis; do not blindly increase z-loss, lower LR, or disable NaN checks |
| Rising router logits before loss spike | Per-layer z-loss, router precision and reconstructed score distribution | Evaluate the precision and stabilization mechanisms in §3.1; keep the quality comparison controlled |
| Growing expert output norms | Per-token norms, per-expert mean norms and layer-wide ratios, excluding padding | Evaluate activation bounds or latent normalization where evidence points; a concatenated norm confounds magnitude with token count |
| Collapse after changing optimizer | Expert utilization, update scale and the pinned implementation's optimizer details | Read §3.6 optimizer evidence before applying a scale or precision change; do not assume a universal Muon fix |

The complete [42-symptom index](troubleshooting.md) includes launch assertions, global auxiliary-loss limitations, dead experts, capacity drops, shared experts, upcycling bugs and RL drift.

## Capture measurements correctly

Read [A.1](../src/chapters/A-appendix.md#s-a-1) for capture commands and readers embedded in the source.

- For counts `[2, 2, 4, 0]`, mean is 2 and MaxVio is 1. Include the empty expert. If micro-batches alternate `[4, 0]` and `[0, 4]`, each has MaxVio 1 but their summed counts `[4, 4]` have MaxVio 0.
- Rank-local expert indices need an explicit mapping to global experts. Keep pipeline stages, MTP depths and independent replicas distinct; do not pool tensor-parallel duplicates. Disable pipeline interleaving when the saved record format cannot distinguish its reused local layer IDs.
- Post-dispatch counts can include capacity/padding effects. Use unpadded router assignments for original demand. Missing trace records caused by dropping are missing observations, not zeros.
- Reconstruct selected weights with the configured score function, normalization and routed scale, retaining recorded selections. Captured logits are recomputed and stored in bf16, so reconstructed weights are approximate.
- Compare expert output magnitudes using per-token L2 or RMS and then per-expert means. Empty experts and a zero median yield undefined ratios. Join EP shards before a layer-wide median; combine expert-TP partial vectors before computing their norms.
- Report training timings from a warmed-up interval without trace hooks, CPU activation copies or profiler overhead. Use separate short captures for diagnosis. The default memory logger may omit the failing rank.

## Serving and RL consequences

The [serving chapter](../src/chapters/4-from-training-to-serving.md#s-4) discusses changing `k`, low-bit experts, serving EP, disaggregation and RL routing drift. Training throughput is not a serving-latency measurement. Evaluate smaller inference `k` or quantization against task quality and output scaling, and assess train/inference routing and probability gaps when RL reward stalls. Use these consequences to inform training choices without expanding an ordinary training question into a deployment project.
