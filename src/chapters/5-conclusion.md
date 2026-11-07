> Source: [Hugging Face handbook](https://huggingface.co/spaces/huggingface/moe-blogpost/blob/ef70726e6f8b99d74298a16a4894340f288a58c2/app/src/content/chapters/5-conclusion.mdx), revision `ef70726e6f8b99d74298a16a4894340f288a58c2`.


<a id="s-5"></a>

## 5\. Conclusion

We started from a dense run, took the MoE layer apart setting by setting, and then followed the trained model into serving and RL post-training. You can now test a cluster before trusting it, train a dense baseline and an MoE on the same data and launch script, and make two runs repeatable enough to compare. Chapter 3 paired each part of the layer, from the router's scores to the all-to-all, with a signal to watch and a recommendation. Appendix [A.2](A-appendix.md#s-a-2) runs the other way, from a symptom on the dashboard back to the config behind it.

The block below gathers every flag the chapters recommend, each with a comment naming the section that argues for it: commented-out lines hold only under a condition or replace a line above them, and values in angle brackets are yours to choose. Start from your own launch script and bring the groups in one at a time, measuring each against the run before it, since each recommendation comes from its own setup and their gains need not add up.

**Every recommended flag, by section**

```
# 2.1 Test your hardware
--gpu-sniff-test-interval <n>               # 2.1: GPU and EP all-to-all check every n iters

# 2.2 Build your image (EFA on AWS P5)
# 2.2, 3.7: EFA libraries first, or NCCL quietly falls back to sockets
export LD_LIBRARY_PATH=/opt/amazon/ofi-nccl/lib:/opt/amazon/efa/lib:${LD_LIBRARY_PATH:-}
export NCCL_NET_PLUGIN=ofi                  # 2.2: by name; a path left NCCL on sockets
export FI_PROVIDER=efa                      # 2.2
export FI_EFA_USE_DEVICE_RDMA=1             # 2.2
export NCCL_SOCKET_IFNAME='^lo,docker0,veth_def_agent'  # 2.2: adapt to your interfaces
export NCCL_DEBUG=INFO                      # 2.2, 3.7: want "Using network Libfabric"

# 2.5 Your first MoE
# --deterministic-mode                      # 2.5: to compare runs or chase a NaN;
# export NVTE_ALLOW_NONDETERMINISTIC_ALGO=0 #   also drop --cross-entropy-loss-fusion

# 3.0 Monitoring
--moe-per-layer-logging                     # 3.0, 3.5: router losses per layer
--save <dir> --save-interval <m>            # 3.0: token counts and dumps go here
--save-tokens-per-expert-interval <n>       # 3.0, 3.3: tokens per expert, MaxVio
--log-throughput --log-params-norm          # 3.0: TFLOP/s, parameter norm
--log-num-zeros-in-grad --log-max-attention-logit  # 3.0: run health
# --moe-routing-trace-path <dir> --moe-routing-trace-max-training-iters <n>
# --cuda-graph-impl none                    # 3.0: bounded routing trace; hooks skip graphs
# --save-activations-interval <n>           # 3.0, 3.4: expert output norms; sample sparsely

# 3.1 Router scoring
--moe-router-dtype fp32                     # 3.1: bf16 ties can flip experts
# --moe-router-score-function sigmoid       # 3.1, 3.3: needed by the expert bias
# --moe-router-pre-softmax                  # 3.1: softmax at top-1, else no router gradient
# --moe-z-loss-coeff 1e-3                   # 3.1: softmax router whose logits drift up

# 3.2 Routing strategy
# --moe-num-hash-layers <n>                 # 3.2: only to reproduce DeepSeek-V4;
#                                           #   load a fixed table, not the placeholder

# 3.3 Load balancing
--moe-router-load-balancing-type aux_loss --moe-aux-loss-coeff 1e-3  # 3.3 Aux loss
# --moe-router-force-load-balancing         # 3.3, 3.7: control run only, never train
# --moe-router-load-balancing-type global_aux_loss  # 3.3 Scope: domain experts, +5.8% step
# 3.3 Loss-free bias, in place of the aux_loss line:
# --moe-router-enable-expert-bias --moe-router-score-function sigmoid
# --moe-router-bias-update-rate <rate>      # tune to expert count; 1e-3 coarse past 128
# --moe-router-load-balancing-type seq_aux_loss --moe-aux-loss-coeff 1e-4  # DeepSeek-V3
# --moe-router-load-balancing-type quantile_balancing  # 3.3 Quantile: no aux loss,
#                                           #   router fusion or group-limited routing

# 3.4 Experts
# 2.5 shape; 3.4 Count and size: finer experts help, up to a point
--num-experts 64 --moe-ffn-hidden-size 1024 --moe-router-topk 8
# --moe-latent-size <l>                     # 3.4 Latent MoE: more experts, same traffic
# --moe-use-norm-before-up-proj             # 3.4: Kimi K3's fix for latent blow-ups
# --moe-shared-expert-intermediate-size 1024  # 3.4: routed width, top-k one lower
# --activation-func-clamp-value 10          # 3.4 Activation: if expert norms diverge
# --activation-func-tanh-clamp-scale 4 --activation-func-tanh-clamp-scale-linear 25
#                                           # 3.4: Kimi K3's SiTU-GLU, Megatron Core v0.20 on

# 3.5 Block layout
# --moe-layer-freq "([0]+[1]*15)"           # 3.5: leading dense layer, fewer all-to-alls
# --moe-shortcut-connection --moe-shortcut-parallel  # 3.5 Block wiring: hybrid stack;
#                                           #   no FSDP, CUDA graphs or full recompute

# 3.6 Training
# --moe-use-upcycling --moe-upcycling-granularity 8  # 3.6: first run only, 2.5's two fixes
# --optimizer muon --muon-extra-scale-factor 0.2     # 3.6 Optimizer: 1.0 diverged; no FSDP
# --moe-router-skip-muon                    # 3.6: router on Adam, Megatron Core v0.20 on
# --mtp-num-layers 1 --mtp-loss-scaling-factor 0.1   # 3.6 MTP
# --pipeline-model-parallel-layout <layout> # 3.6: place the MTP layer under PP
# --timing-log-level 2 --timing-log-option all       # 3.6: find the slowest PP stage
--rerun-mode validate_results               # 3.6 Stability: the default; keep it

# 3.7 Systems
# --profile --profile-step-start <a> --profile-step-end <b> --profile-ranks <r>
#                                           # 3.7 Profiling: one step per new config
# --moe-permute-fusion                      # 3.7: if permute and copy kernels show
--expert-model-parallel-size 8              # 3.7 Interconnect: EP inside one node
# --overlap-moe-expert-parallel-comm --delay-wgrad-compute  # 3.7 Overlap: exposed
#                                           #   all-to-all; no full recompute, VPP under PP
# --recompute-granularity selective --recompute-modules layernorm moe_act
# --fine-grained-activation-offloading --offload-modules core_attn attn_proj expert_fc1
#                                           # 3.7 Memory: when the overlap does not fit
# --activation-offload-fraction <f>         # 3.7: lower it if step time grows
# --moe-token-dispatcher-type flex --moe-router-num-groups <nodes> --moe-router-group-topk <g>
#                                           # 3.7 Group-limited: EP across nodes, DeepEP
# --moe-expert-capacity-factor <cf> --moe-pad-expert-input-to-capacity
#                                           # 3.7 Capacity: memory short; dropless to fine-tune
# --fp8-format <fmt> --fp8-recipe blockwise # 3.7 Precision: Hopper; mxfp8 on Blackwell
# --moe-router-padding-for-quantization     # 3.7: aligned counts for quantized GEMMs
# --moe-dispatch-fwd-dtype mxfp8 --moe-combine-bwd-dtype mxfp8  # 3.7: ncclep, Blackwell

# 4 From training to serving
# --fp4-format e2m1                         # 4 Low-bit: NVFP4 on Blackwell, not with FP8
# --rl-inference-expert-model-parallel-size <n>  # 4: rollout engine's own EP size
# --moe-enable-routing-replay               # 4 RL routing: rollout and trainer disagree
# --batch-invariant-mode                    # 4: kernels' share of the mismatch; slow
```

Plenty remains open. Most of what we know about training MoEs at scale comes from the technical reports of open-weight models, and a report shows what a team shipped: rarely what it tried and dropped, or the run that settled a choice. Many of the recommendations above rest on one ablation in one lab's setup, and each is an experiment worth rerunning at another scale, on other data or on another cluster. If you run one, publish it with its configs and logs, the negative results included: that is how the next team starts from what you learned instead of from scratch. Share yours, or ask about ours, on the [discussion page](https://huggingface.co/spaces/huggingface/moe-blogpost/discussions) of this post.

We hope this post saves your next MoE run a few of the days it cost ours.

<a id="s-5-acknowledgements"></a>

### Acknowledgements

We thank [Antoine Bosselut](https://huggingface.co/atcbosselut), [Martin Jaggi](https://huggingface.co/mjaggi) and the Swiss AI team for providing part of the compute behind this post, and for insightful conversations along the way. We also thank [Thibaud Frere](https://huggingface.co/tfrere) for his help with the figures.
