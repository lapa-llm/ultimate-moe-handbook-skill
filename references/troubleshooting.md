# Troubleshooting index

Start with the first signal that changed. Check stack correctness using the two sanity checks in [§2.5](../src/chapters/2-setup-and-your-first-run.md#s-2-5), then follow the linked handbook explanation. Symptoms suggest hypotheses, not proven causes.

| Tag | Symptom | Read |
| --- | --- | --- |
| `slow` | throughput drop | [3.3](../src/chapters/3-anatomy-of-moe-training.md#s-3-3), [3.7](../src/chapters/3-anatomy-of-moe-training.md#s-3-7) profiling |
| `slow` | half the single-node step is all-to-all | [3.3](../src/chapters/3-anatomy-of-moe-training.md#s-3-3) balance first, then [3.7](../src/chapters/3-anatomy-of-moe-training.md#s-3-7) overlap |
| `slow` | aux loss near 1 but one GPU slow | [3.3 Cost of imbalance](../src/chapters/3-anatomy-of-moe-training.md#s-3-3-cost-of-imbalance) (the aux loss equals 1 for flat router probabilities whatever the load; read MaxVio) |
| `slow`, `learns badly` | loss-free bias run still unbalanced after many steps | [3.3 Loss-free bias](../src/chapters/3-anatomy-of-moe-training.md#s-3-3-loss-free-bias) (fixed step lags; quantile balancing) |
| `slow`, `learns badly` | a few experts overloaded only in the first layers | [3.2](../src/chapters/3-anatomy-of-moe-training.md#s-3-2) hash layers, [3.5 Dense layers](../src/chapters/3-anatomy-of-moe-training.md#s-3-5-dense-layers) |
| `slow` | each token's all-to-all reaches every node | [3.7 Interconnect](../src/chapters/3-anatomy-of-moe-training.md#s-3-7-interconnect) and group-limited routing |
| `slow` | throughput drops after moving to more, smaller experts | [3.4](../src/chapters/3-anatomy-of-moe-training.md#s-3-4) count and size |
| `slow`, `OOM` | step much slower after turning on MTP, or OOM with more layers under pipeline parallelism | [3.6 MTP](../src/chapters/3-anatomy-of-moe-training.md#s-3-6-mtp) |
| `slow` | all-to-all exposed in the profile | [3.5 Block wiring](../src/chapters/3-anatomy-of-moe-training.md#s-3-5-block-wiring), [3.7 Overlap](../src/chapters/3-anatomy-of-moe-training.md#s-3-7-overlap) |
| `slow` | multi-node about 25x slower on our EP16 proxy and the NCCL log says 'Using network Socket' | [3.7 Interconnect](../src/chapters/3-anatomy-of-moe-training.md#s-3-7-interconnect) |
| `slow` | step slower after moving to `global_aux_loss` | [3.3 Scope](../src/chapters/3-anatomy-of-moe-training.md#s-3-3-scope) |
| `slow` | under quantile balancing, MaxVio per global batch low but per micro-batch high | [3.3 Quantile](../src/chapters/3-anatomy-of-moe-training.md#s-3-3-quantile) |
| `slow` | step slower with `--moe-latent-size` | [3.4 Latent MoE](../src/chapters/3-anatomy-of-moe-training.md#s-3-4-latent-moe), from the two d × ℓ projections and smaller expert GEMMs ([3.4](../src/chapters/3-anatomy-of-moe-training.md#s-3-4)); the throughput LatentMoE reports is serving, 12% lower at concurrency 1 |
| `slow` | slower inference after adding a shared expert on top of the routed top-k | [3.4 Shared experts](../src/chapters/3-anatomy-of-moe-training.md#s-3-4-shared-experts) |
| `slow` | full recompute still on | [3.7 Memory](../src/chapters/3-anatomy-of-moe-training.md#s-3-7-memory) |
| `slow` | TFLOP/s still short after balance, overlap and fusions | [3.7 Precision](../src/chapters/3-anatomy-of-moe-training.md#s-3-7-precision) |
| `OOM` | OOM on one rank | [3.3](../src/chapters/3-anatomy-of-moe-training.md#s-3-3) (imbalance), [3.7](../src/chapters/3-anatomy-of-moe-training.md#s-3-7) memory |
| `OOM` | peak memory looks fine but one rank OOMs | [3.7](../src/chapters/3-anatomy-of-moe-training.md#s-3-7) memory (Megatron logs data-parallel rank 0 only) |
| `blows up` | a NaN with nothing moving before it (grad norm, params norm, z-loss flat) | [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) stability (no warning; the rerun on another GPU tells a faulty GPU from a reproducible NaN) |
| `blows up` | exit code 16 twice on one node | [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) stability (the rerun needs a different GPU) |
| `blows up` | Muon run diverges in the first steps | [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) optimizer (update scale, `--muon-extra-scale-factor`) |
| `blows up` | z-loss or router logits climbing before a spike | [3.1](../src/chapters/3-anatomy-of-moe-training.md#s-3-1) precision (a flat z-loss before a NaN points to [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) stability instead) |
| `blows up` | expert output norms growing, or their max-to-median ratio climbing before a spike | [3.4](../src/chapters/3-anatomy-of-moe-training.md#s-3-4) activation (clamp) |
| `blows up` | exploding activations or a spike with a latent MoE | [3.4](../src/chapters/3-anatomy-of-moe-training.md#s-3-4) latent (norm before the up-projection) |
| `blows up` | grad norm and load-balancing loss jump a few iterations before a NaN | [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) stability, [3.3](../src/chapters/3-anatomy-of-moe-training.md#s-3-3). Our 7B-A1B |
| `blows up` | loss spikes under Muon that resuming from a nearby checkpoint often avoids | [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) optimizer (orthogonalization in bf16) |
| `learns badly` | RL reward stalls or collapses while the train-inference probability gap grows | [4 RL routing](../src/chapters/4-from-training-to-serving.md#s-4-rl-routing) |
| `learns badly` | loss flat but MaxVio or an expert's output norm drifting from the layer median (collapse, dead or rogue expert) | [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) stability, [3.3](../src/chapters/3-anatomy-of-moe-training.md#s-3-3) |
| `learns badly` | top-k weights all equal (flat gate) | [3.1](../src/chapters/3-anatomy-of-moe-training.md#s-3-1) sharpness |
| `learns badly` | dead experts with an aux loss on | [3.3 Aux loss](../src/chapters/3-anatomy-of-moe-training.md#s-3-3-aux-loss) (coefficient too small) |
| `learns badly` | `global_aux_loss` with more than 256 micro-batches per global batch | [3.3 Scope](../src/chapters/3-anatomy-of-moe-training.md#s-3-3-scope) Flags (bf16 counter) |
| `learns badly`, `blows up` | routing collapse or divergence in the first MoE layers | [3.5 Dense layers](../src/chapters/3-anatomy-of-moe-training.md#s-3-5-dense-layers) |
| `learns badly` | a capacity factor is set and the loss lags the dropless run | [3.7 Capacity and replicas](../src/chapters/3-anatomy-of-moe-training.md#s-3-7-capacity-and-replicas) (drops are not logged |
| `learns badly` | experts collapse layer by layer under Muon | [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) optimizer |
| `learns badly` | with `--moe-router-pre-softmax` (top-k weights not renormalized), loss above a renormalized run | [3.1 Output scale](../src/chapters/3-anatomy-of-moe-training.md#s-3-1-output-scale) |
| `learns badly` | experts that do not specialize by domain | [3.3 Scope](../src/chapters/3-anatomy-of-moe-training.md#s-3-3-scope) |
| `learns badly` | LM loss rising with the aux coefficient | [3.3 Aux loss](../src/chapters/3-anatomy-of-moe-training.md#s-3-3-aux-loss) |
| `learns badly` | loss no longer improving as experts get smaller | [3.4 Count and size](../src/chapters/3-anatomy-of-moe-training.md#s-3-4-count-and-size) |
| `learns badly` | a model trained with expert choice routing differently at inference | [3.2 Who selects](../src/chapters/3-anatomy-of-moe-training.md#s-3-2-who-selects) |
| `learns badly` | an upcycled MoE that learns slowly after its head start | [3.6 Upcycling](../src/chapters/3-anatomy-of-moe-training.md#s-3-6-upcycling) |
| `won't start` | `--moe-use-upcycling` fails with "unexpected keyword argument 'model'" or a missing `pre_mlp_layernorm` key | [3.6](../src/chapters/3-anatomy-of-moe-training.md#s-3-6) upcycling (two upstream bugs) |
| `won't start` | assert about full recomputation after turning on `--overlap-moe-expert-parallel-comm` | [3.7](../src/chapters/3-anatomy-of-moe-training.md#s-3-7) overlap and memory |

Read the full [debugging commentary](../src/chapters/A-appendix.md#s-a-2) and [measurement limits](../src/chapters/A-appendix.md#s-a-1) before interpreting metrics.
