# Citation evidence

These are the handbook’s citation popovers, preserved as searchable Markdown. Quotations and findings below are attributed to the original cited sources; they are not additional skill instructions.


<a id="aa-open-top"></a>

## aa-open-top

Artificial Analysis Intelligence Index v5.0.1, [open-weights models](https://artificialanalysis.ai/models/open-source)

29 open-weights releases have a score, one row per release at its highest-scoring effort level. Ranks 1 to 11 and 14 to 20 list total and active parameters (MoE); #12 Nanbeige4.3-33B (20.4) and #13 Qwen3.8 27B (Xhigh) (20.1) list one parameter count (dense), and each model's `config.json` on the Hugging Face Hub agrees (expert counts for the MoEs, none for these two); 21 of the 29 are MoEs. Highest MoE per lab, top five labs: DeepSeek V4.1 Flash 1017 (Max) 32.6, GLM-5.3 (Max) (Z AI) 31.7, MiMo-V2.6-Pro (Xiaomi) 29.9, Ling 3.1 Flash 1019 (InclusionAI) 29.6, MiniMax-M3.1-Flash 29.1; then Step 5 Preview (StepFun) 28.5, Mistral Large 4 (High) (Mistral) 26.1, Muse Spark Open (Xhigh) (Meta) 24.9. Kimi K3 is not ranked: Artificial Analysis marks it deprecated. The figure places each model at the release date Artificial Analysis lists.


<a id="stp-dense"></a>

## stp-dense

[The Smol Training Playbook](https://huggingfacetb-smol-training-playbook.hf.space/)

Hugging Face · 2025

The Smol Training Playbook (Hugging Face, published Oct. 30, 2025; [huggingfacetb-smol-training-playbook.hf.space](https://huggingfacetb-smol-training-playbook.hf.space/))

> We went with a dense transformer rather than MoE or hybrid

> Since we're not using a mixture-of-experts architecture, we don't need expert parallelism


<a id="pyxis-readme"></a>

## pyxis-readme

[pyxis](https://github.com/NVIDIA/pyxis)

NVIDIA · GitHub

[NVIDIA/pyxis README (github.com/NVIDIA/pyxis)](https://github.com/NVIDIA/pyxis)

> Pyxis is a SPANK plugin for the Slurm Workload Manager. It allows unprivileged cluster users to run containerized tasks through the command.


<a id="enroot-readme"></a>

## enroot-readme

[enroot](https://github.com/NVIDIA/enroot)

NVIDIA · GitHub

[NVIDIA/enroot README (github.com/NVIDIA/enroot)](https://github.com/NVIDIA/enroot)

> A simple, yet powerful tool to turn traditional container/OS images into unprivileged sandboxes

> …provides facilities to import well known container image formats (e.g. Docker)


<a id="hf-jobs-pricing"></a>

## hf-jobs-pricing

Hugging Face, [Jobs, Pricing and Billing](https://huggingface.co/docs/hub/jobs-pricing)

"Jobs are available to any user or organization with a positive credit balance. The monthly compute credits included with a PRO, Team, or Enterprise subscription count towards that balance"; "Billing on Jobs is based on hardware usage and is computed by the minute"; GPU table, "8x Nvidia H200 \| 184 vCPU \| 2048 GB \| 1128 GB \| 24000 GB \| $40.00".


<a id="hf-jobs-hardware"></a>

## hf-jobs-hardware

`hf jobs hardware`

26 flavors; the eight-GPU ones are `a100x8`, `h200x8` ("8x H200 (1128 GB)", $40.00 per hour), `l40sx8` and `rtx-pro-6000x8`; `h200` lists "1x H200 (141 GB)". `hf jobs run --help`: `IMAGE COMMAND...` arguments, `--flavor`, `--timeout` ("int with s (seconds, default), m (minutes), h (hours) or d (days)").


<a id="hf-jobs-guide"></a>

## hf-jobs-guide

Hugging Face, [Run and manage Jobs](https://huggingface.co/docs/huggingface_hub/en/guides/jobs)

a job is defined by "a command to run ..., a Docker Image from Hugging Face Spaces or Docker Hub, and a hardware flavor"; GPU example `hf jobs run --name gpu-check --flavor a10g-small pytorch/pytorch:2.6.0-cuda12.4-cudnn9-devel python -c "import torch; print(torch.cuda.get_device_name())"`; "Jobs have a default timeout (30 minutes), after which they will automatically stop".


<a id="dcgm-levels"></a>

## dcgm-levels

[DCGM Diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html)

NVIDIA · DCGM documentation

NVIDIA DCGM documentation, "DCGM Diagnostics" (https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html)

> DCGM Diagnostics

> Level 1 tests to use as a readiness metric


<a id="aws-nccl-image"></a>

## aws-nccl-image

[awsome-distributed-ai, NCCL test recipes](https://github.com/awslabs/awsome-distributed-ai/tree/main/micro-benchmarks/nccl-tests)

AWS Labs · GitHub

AWS Labs, [NCCL test recipes](https://github.com/awslabs/awsome-distributed-ai/tree/main/micro-benchmarks/nccl-tests), runtime preparation and image setup


<a id="enroot-import"></a>

## enroot-import

[enroot](https://github.com/NVIDIA/enroot)

NVIDIA · GitHub

NVIDIA Enroot, [import command](https://github.com/NVIDIA/enroot/blob/main/doc/cmd/import.md), Usage


<a id="nccl-tests-build"></a>

## nccl-tests-build

[nccl-tests](https://github.com/NVIDIA/nccl-tests)

NVIDIA · GitHub

NVIDIA, [nccl-tests README, Build](https://github.com/NVIDIA/nccl-tests#build)


<a id="hub-gated"></a>

## hub-gated

Hugging Face Hub API, [`api/models/meta-llama/Llama-3.2-1B`](https://huggingface.co/api/models/meta-llama/Llama-3.2-1B)

returns `"gated": "manual"`; [`api/models/unsloth/Llama-3.2-1B`](https://huggingface.co/api/models/unsloth/Llama-3.2-1B) and [`api/datasets/HuggingFaceFW/fineweb-edu`](https://huggingface.co/api/datasets/HuggingFaceFW/fineweb-edu) return `"gated": false`.


<a id="datatrove-skip"></a>

## datatrove-skip

datatrove, `src/datatrove/executor/base.py` [L30](https://github.com/huggingface/datatrove/blob/2c895af7a95010a96fa53e2dc77cc0ce92799e3f/src/datatrove/executor/base.py#L30)

> …whether to skip tasks that were completed in previous runs


<a id="trackio-readme"></a>

## trackio-readme

Trackio [`README.md`](https://github.com/gradio-app/trackio/blob/4bef24c5fd2db622c41cce7c763be504116281a2/README.md) at 4bef24c

L23 "a lightweight, free experiment tracking library built by Hugging Face"; L26 "local-first, because you shouldn't need to make an account to log data"; L27 logs "stored in SQLite database"; L42-L45 "API compatible" with wandb's init, log and finish calls, a "Drop-in replacement" via `import trackio as wandb`; L49 "dashboard runs locally by default ... you can also log metrics to a Hugging Face Space with `space_id`"; L54 "Everything here, including hosting on Hugging Face, is free!"


<a id="step35-f4"></a>

## step35-f4

[Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters](https://arxiv.org/abs/2602.10604)

Ailin Huang, Ang Li, Aobo Kong et al. · 2026 · arXiv:2602.10604

[§4.1.3 Localized Activation Blow-up in MoE Layers](https://arxiv.org/html/2602.10604#S4.F4)

Figure 4: Analysis of expert activation stability and mitigation strategies.

> …training loss appears indistinguishable

> …effectively bounds maximum norms


<a id="hub-dsv41"></a>

## hub-dsv41

DeepSeek-V4.1-Flash's own inference code, [`model.py#L811`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/2cba9e42aa026125f3ed06c6d98c1db82f7ca027/inference/model.py#L811) (router GEMM in fp32, divided by `gate_temp`, 1.0 by default)

The DeepSeek-V4.1-Flash-1017 checkpoint (Hub rev 1bae0e1), the version on the Artificial Analysis index, has an identical `config.json`.


<a id="tf-gemma4"></a>

## tf-gemma4

transformers `gemma4` at main ff704ff, `Gemma4TextRouter`, [`modeling_gemma4.py#L1323`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/gemma4/modeling_gemma4.py#L1323-L1324)

RMSNorm on the router input, times a learned scale and hidden\_size^-0.5, [L1326-L1329](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/gemma4/modeling_gemma4.py#L1326-L1329) (projection, softmax in fp32), [L1338-L1341](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/gemma4/modeling_gemma4.py#L1338-L1341) (renormalize, then per-expert scale); `num_experts: 128`, `top_k_experts: 8` in google/gemma-4-26b-a4b's config.


<a id="tf-glm-moe-dsa"></a>

## tf-glm-moe-dsa

transformers `glm_moe_dsa` at main ff704ff, [`modeling_glm_moe_dsa.py#L485`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/glm_moe_dsa/modeling_glm_moe_dsa.py#L485)

router GEMM in fp32; `moe_router_dtype: float32` in the config.


<a id="tf-inkling"></a>

## tf-inkling

transformers `inkling` at main ff704ff, [`modeling_inkling.py#L360`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/inkling/modeling_inkling.py#L360)

router GEMM in the model dtype, [L371-L372](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/inkling/modeling_inkling.py#L371-L372) (log-sigmoid, normalized over the top-k and the shared experts), [L374](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/inkling/modeling_inkling.py#L374) (route scale times a learned global scale); `route_scale: 8.0`, `n_shared_experts: 2` in the config.


<a id="hub-kimi-k3"></a>

## hub-kimi-k3

Kimi K3's repo code, [`modeling_kimi_linear.py#L707-L712`](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/modeling_kimi_linear.py#L707-L712) (router GEMM in fp32, sigmoid)

The gate never reads the config's `temperature`.


<a id="k3-qat"></a>

## k3-qat

[Kimi K3 tech report](https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf)

Kimi Team · GitHub, MoonshotAI/Kimi-K3

Kimi K3 tech report ([github.com/MoonshotAI/Kimi-K3, `k3_tech_report.pdf`](https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf)), §4.1.4 Deployment-Aware Post-Training, p. 14

> …while all non-expert components (attention projections, latent MoE projections, shared experts, and MoE routers) remain in higher precision


<a id="hub-mimo26"></a>

## hub-mimo26

MiMo-V2.6-Pro-RL's repo code, [`modeling_mimo_v2.py#L155`](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/73875d00b30a89ef8cc353a0b60b0e9f9561952d/modeling_mimo_v2.py#L155) (router GEMM in fp32)


<a id="tf-cohere2-moe"></a>

## tf-cohere2-moe

transformers `cohere2_moe` at main ff704ff, [`modeling_cohere2_moe.py#L150-L160`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/cohere2_moe/modeling_cohere2_moe.py#L150-L160)

router GEMM in the model dtype, softmax or sigmoid, renormalization only with `norm_topk_prob`; North-Mini-Code's config sets `expert_selection_fn: sigmoid`, `norm_topk_prob: false`.


<a id="tf-qwen4-exp"></a>

## tf-qwen4-exp

transformers `qwen4_exp` at main ff704ff

router GEMM in the model dtype at L963; [`modeling_qwen4_exp.py#L964`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/qwen4_exp/modeling_qwen4_exp.py#L964) (softmax over all experts), [`modeling_qwen4_exp.py#L966`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/qwen4_exp/modeling_qwen4_exp.py#L966-L967) (top-k renormalized when `norm_topk_prob`), which defaults to True ([`configuration_qwen4_exp.py#L162`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/qwen4_exp/configuration_qwen4_exp.py#L162)); the router has no routed scaling factor ([`modeling_qwen4_exp.py#L952`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/qwen4_exp/modeling_qwen4_exp.py#L952-L970) (whole router)).


<a id="hub-step5-router"></a>

## hub-step5-router

Step-5-Preview on the Hub (`stepfun-ai/Step-5-Preview`, rev 364b3b0)

`config.json` `text_config` has `moe_num_experts: 352`, `moe_top_k: 8`, `norm_expert_weight: true`, `moe_router_scaling_factor: 3.0`, `use_moe_router_bias: true`, `need_fp32_gate: true`; [`inference/model.py#L2020-L2030`](https://huggingface.co/stepfun-ai/Step-5-Preview/blob/364b3b03fed2477aa0953fe855a2c4c8c48ee3cc/inference/model.py#L2020-L2030): logits from fp32 inputs and weights, a sigmoid, top-k on sigmoid plus bias, weights without the bias, divided by their sum, times the scaling factor; no temperature or soft-cap. StepFun's technical blog (platform.stepfun.ai/blog/inside-step-5-preview) trains in mixed-precision FP8 with FP32 hidden states and RMSNorm scales, and gives no router precision.


<a id="tf-zaya"></a>

## tf-zaya

transformers `zaya` at main ff704ff, [`modeling_zaya.py#L538`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/zaya/modeling_zaya.py#L538)

down-projection to the 256-wide router, [L544-L545](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/zaya/modeling_zaya.py#L544-L545) (router MLP, softmax), [L552](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/zaya/modeling_zaya.py#L552) (the extra skip expert); `num_experts: 16`, `num_experts_per_tok: 1`, `router_hidden_size: 256` in the config.


<a id="dsv4-sqrtsp"></a>

## dsv4-sqrtsp

[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)

DeepSeek-AI, Anyi Xu, Bangcai Lin et al. · 2026 · arXiv:2606.19348

[§2.1 Designs Inherited from DeepSeek-V3](https://arxiv.org/html/2606.19348#S2.SS1)

> Different from DeepSeek-V3, we change the activation function that computes the affinity scores from Sigmoid(·) into Sqrt(Softplus(·))


<a id="lossfree-softmax"></a>

## lossfree-softmax

[Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664)

Lean Wang, Huazuo Gao, Chenggang Zhao et al. · 2024 · arXiv:2408.15664

[Appendix C Experiments with Softmax Gate](https://arxiv.org/html/2408.15664#A3)

> Adjusting the per-expert bias for the softmax gate is more challenging due to the normalization property of softmax, which makes the score gap between two experts sensitive to the scores of other experts


<a id="krajewski25-t6"></a>

## krajewski25-t6

[Scaling Fine-Grained MoE Beyond 50B Parameters: Empirical Evaluation and Practical Insights](https://arxiv.org/abs/2506.02890)

Jakub Krajewski, Marcin Chochowski, Daniel Korzekwa · 2025 · arXiv:2506.02890

[Table 6](https://arxiv.org/html/2506.02890#S4.T6)

Validation loss for training models with different orders of softmax and Top-k.


<a id="cfg-dsv3"></a>

## cfg-dsv3

DeepSeek-V3 [`config.json`](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/e815299b0bcbac849fa540c768ef21845365c9eb/config.json)

`routed_scaling_factor: 2.5`, `num_experts_per_tok: 8`.


<a id="tf-llama4"></a>

## tf-llama4

transformers `llama4` at main ff704ff, [`modeling_llama4.py#L150`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/llama4/modeling_llama4.py#L150)

sigmoid of the top-k router logit, [L169](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/llama4/modeling_llama4.py#L169) (`routed_in = routed_in * router_scores`: the score multiplies the expert's input), [L79-L81](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/llama4/modeling_llama4.py#L79-L81) (bias-free SwiGLU experts: `bmm` with `gate_up_proj`, then `up * act_fn(gate)` and `down_proj`); `num_experts_per_tok: 1` in the Scout and Maverick `config.json` (unsloth mirrors of the gated Meta repos).


<a id="skywork-eq6"></a>

## skywork-eq6

[Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models](https://arxiv.org/abs/2406.06563)

Tianwen Wei, Bo Zhu, Liang Zhao et al. · 2024 · arXiv:2406.06563

[§4.1 Gating Logit Normalization](https://arxiv.org/html/2406.06563#S4.SS1)


<a id="grok2-softcap"></a>

## grok2-softcap

Grok 2, [`config.json`](https://huggingface.co/xai-org/grok-2/blob/daf4395a80ad177386cfe39641b64fc12b1d70ed/config.json)


<a id="skywork-f2"></a>

## skywork-f2

[Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models](https://arxiv.org/abs/2406.06563)

Tianwen Wei, Bo Zhu, Liang Zhao et al. · 2024 · arXiv:2406.06563

[Figure 2](https://arxiv.org/html/2406.06563#S4.F2)

A comparison of gate distribution with and without logit normalization.


<a id="skywork-f3"></a>

## skywork-f3

[Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models](https://arxiv.org/abs/2406.06563)

Tianwen Wei, Bo Zhu, Liang Zhao et al. · 2024 · arXiv:2406.06563

[Figure 3](https://arxiv.org/html/2406.06563#S4.F3)

Top left: Training loss curves for MoE models with and without gating normalization, illustrating that gating normalization contributes to a moderate improvement in loss.


<a id="xmoe-t3"></a>

## xmoe-t3

[On the Representation Collapse of Sparse Mixture of Experts](https://arxiv.org/abs/2204.09179)

Zewen Chi, Li Dong, Shaohan Huang et al. · 2022 · arXiv:2204.09179

Table 3

Ablation studies of X-MoE components.


<a id="torch-topk"></a>

## torch-topk

PyTorch `torch.topk` documentation

it specifies `largest` and `sorted` ("will make sure that the returned k elements are themselves sorted") and says nothing about which index wins a tie.


<a id="stmoe-s34"></a>

## stmoe-s34

[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906)

Barret Zoph, Irwan Bello, Sameer Kumar et al. · 2022 · arXiv:2202.08906

[§3.4 Selecting a Precision Format: Trading Efficiency and Stability, Sparse expert models are sensitive to roundoff errors because they have more exponential functions due to the routers](https://arxiv.org/html/2202.08906#S3.SS4.SSS0.Px2)

> …can exacerbate roundoff errors ... and lead to training instabilities

> …penalizes large logits into the gating network


<a id="fp32-router-code"></a>

## fp32-router-code

Router GEMM cast to fp32 in inference code

transformers at main ff704ff, [`modeling_deepseek_v32.py#L512`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/deepseek_v32/modeling_deepseek_v32.py#L512) (DeepSeek-V3.2) and [`modeling_glm4_moe.py#L283`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/glm4_moe/modeling_glm4_moe.py#L283) (GLM-4.5); Kimi K2.5's repo code, [`modeling_deepseek.py#L445-L446`](https://huggingface.co/moonshotai/Kimi-K2.5/blob/4d01dfe0332d63057c186e0b262165819efb6611/modeling_deepseek.py#L445-L446).


<a id="switch-t2"></a>

## switch-t2

[Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961)

William Fedus, Barret Zoph, Noam Shazeer · 2021 · arXiv:2101.03961

[Table 2](https://arxiv.org/html/2101.03961#S2.T2)

Selective precision.


<a id="stmoe-t4"></a>

## stmoe-t4

[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906)

Barret Zoph, Irwan Bello, Sameer Kumar et al. · 2022 · arXiv:2202.08906

[§3.3 Stability and Quality Tradeoffs when Constraining Activations and Gradients](https://arxiv.org/html/2202.08906#S3.T4)

Table 4: Constraining weight updates and router logits.

> We choose a value of c\_z\=0.001 based on the best model quality after pre-training with a hyperparameter sweep


<a id="dsv3-noz"></a>

## dsv3-noz

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§2.1.2 DeepSeekMoE with Auxiliary-Loss-Free Load Balancing](https://arxiv.org/html/2412.19437#S2.SS1.SSS2)


<a id="zhou22-ec"></a>

## zhou22-ec

[Mixture-of-Experts with Expert Choice Routing](https://arxiv.org/abs/2202.09368)

Yanqi Zhou, Tao Lei, Hanxiao Liu et al. · 2022 · arXiv:2202.09368


<a id="hub-dsv4pro-route"></a>

## hub-dsv4pro-route

DeepSeek-V4-Pro's own inference code, [`model.py#L556`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/b5968e9190ef611bbf34a7229255be88a0e937c1/inference/model.py#L556) (hash routing when `layer_id < n_hash_layers`)


<a id="hub-v41-engram"></a>

## hub-v41-engram

DeepSeek-V4.1-Flash on the Hub (rev 314113f)

`config.json` `engram_layer_ids: [1, 14]`, `engram_max_ngram_size: 4`; `model.safetensors.index.json` holds `layers.1.engram.*` and `layers.14.engram.*` and no other Engram layer; [`inference/engram.py#L90`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/314113f8a7dadb388215396ba5fbee2c610a04d6/inference/engram.py#L90) (each position hashed as 2-gram up to `max_ngram_size`-gram), [`inference/model.py#L106`](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/314113f8a7dadb388215396ba5fbee2c610a04d6/inference/model.py#L106) ("n-gram hash lookups added into the residual stream at a few layers").


<a id="hub-llama4-route"></a>

## hub-llama4-route

transformers `llama4` at main ff704ff, [`modeling_llama4.py#L146-L148`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/llama4/modeling_llama4.py#L146-L148)

: `Llama4Router` runs `torch.topk(router_logits, self.top_k, dim=1)` over the expert axis for each token, so each token picks its experts (token choice, with `num_experts_per_tok` 1 plus an always-on shared expert, [L163](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/llama4/modeling_llama4.py#L163)); no token-id table.


<a id="hub-q38-ngram"></a>

## hub-q38-ngram

Qwen3.8-Flash-Next on the Hub (rev de4b8e4)

`config.json` `ngram_size: 3`, `ngram_vocab_size_base: 20000000`, `ple_layer_ids: [2]`; README "N-gram Embedding: 20,000,000 (bigrams/trigrams at layer 2)" and "51B n-gram embedding"; `model.safetensors.index.json` holds `ple.ple_embedding.ngram_embedding.*` only under `layers.1`. transformers `qwen4_exp` ([`modeling_qwen4_exp.py#L1262`](https://github.com/huggingface/transformers/blob/a672eb5f474b8b30173e9f96eab66adf292da635/src/transformers/models/qwen4_exp/modeling_qwen4_exp.py#L1262)) matches `ple_layer_ids` against `layer_idx + 1`, so the README's layer 2 is layer 1 counted from 0; [L1154](https://github.com/huggingface/transformers/blob/a672eb5f474b8b30173e9f96eab66adf292da635/src/transformers/models/qwen4_exp/modeling_qwen4_exp.py#L1154) hashes n-grams from 2 to `ngram_size`.


<a id="hub-step5-route"></a>

## hub-step5-route

Step-5-Preview on the Hub (`stepfun-ai/Step-5-Preview`, rev 364b3b0)

`config.json` `moe_num_experts: 352`, `moe_top_k: 8`, `use_moe_router_bias: true`, no hash, n-gram or Engram key; [`inference/model.py#L2021-L2025`](https://huggingface.co/stepfun-ai/Step-5-Preview/blob/364b3b03fed2477aa0953fe855a2c4c8c48ee3cc/inference/model.py#L2021-L2025) ("Pick `top_k` experts per token", a `torch.topk` over each token's scores).


<a id="lossfree-s52"></a>

## lossfree-s52

[Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664)

Lean Wang, Huazuo Gao, Chenggang Zhao et al. · 2024 · arXiv:2408.15664

[§5.2 Load Balancing and Future Token Leakage](https://arxiv.org/html/2408.15664#S5.SS2)

> EC ensures perfect load balance ... However, this approach inherently leads to a severe issue of future token leakage


<a id="et-ec-causal"></a>

## et-ec-causal

[Expert Threshold Routing for Autoregressive Language Modeling with Dynamic Computation Allocation and Load Balancing](https://arxiv.org/abs/2603.11535)

Hanchi Sun, Yixin Liu, Yonghui Wu et al. · 2026 · arXiv:2603.11535

§2 and §3

> …depends on all tokens' scores ... including future tokens unavailable during inference

> …z\_{t,i} depends only on r\_{t,i} and the global threshold c\_i, routing is fully causal while satisfying load balancing in expectation


<a id="et-t1"></a>

## et-t1

[Expert Threshold Routing for Autoregressive Language Modeling with Dynamic Computation Allocation and Load Balancing](https://arxiv.org/abs/2603.11535)

Hanchi Sun, Yixin Liu, Yonghui Wu et al. · 2026 · arXiv:2603.11535

[Table 1](https://arxiv.org/html/2603.11535#S4.T1)

Main results comparing Expert Choice (EC), Token Choice (TC), and Expert Threshold (ET) routing.


<a id="lossfree-maxvio"></a>

## lossfree-maxvio

[Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664)

Lean Wang, Huazuo Gao, Chenggang Zhao et al. · 2024 · arXiv:2408.15664

[§4.1 Experimental Setups](https://arxiv.org/html/2408.15664#S4.SS1)


<a id="dsv4-s41"></a>

## dsv4-s41

[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)

DeepSeek-AI, Anyi Xu, Bangcai Lin et al. · 2026 · arXiv:2606.19348

[§4.1 Data Construction](https://arxiv.org/html/2606.19348#S4.SS1)

> …use the Hash routing strategy for the first 3 MoE layers


<a id="dsv4-gate-code"></a>

## dsv4-gate-code

DeepSeek-V4-Pro Hub `inference/model.py`, `Gate` ([L546](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/b5968e9190ef611bbf34a7229255be88a0e937c1/inference/model.py#L546))

[L577](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/b5968e9190ef611bbf34a7229255be88a0e937c1/inference/model.py#L577) `indices = self.tid2eid[input_ids]`, [L580](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/b5968e9190ef611bbf34a7229255be88a0e937c1/inference/model.py#L580) `weights = original_scores.gather(1, indices)`, [L560](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/b5968e9190ef611bbf34a7229255be88a0e937c1/inference/model.py#L560) `self.bias = None` in hash layers.


<a id="dsv4-s21"></a>

## dsv4-s21

[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)

DeepSeek-AI, Anyi Xu, Bangcai Lin et al. · 2026 · arXiv:2606.19348

[§2.1 Designs Inherited from DeepSeek-V3](https://arxiv.org/html/2606.19348#S2.SS1)

> The Hash routing strategy determines the target experts of each token according to a predefined hash function with regard to the input token ID

> …we remove the constraint on the number of routing target nodes


<a id="roller-s52"></a>

## roller-s52

[Hash Layers For Large Sparse Models](https://arxiv.org/abs/2106.04426)

Stephen Roller, Sainbayar Sukhbaatar, Arthur Szlam et al. · 2021 · arXiv:2106.04426

[§5.2 Experimental Setup](https://arxiv.org/html/2106.04426#S5.SS2)

> …either outperforms or is competitive with ... Switch Transformers and BASE Layers


<a id="engram-s23"></a>

## engram-s23

Cheng et al., 2026, *Conditional Memory via Scalable Lookup*, arXiv:2601.07372, §2.2 (suffix N-grams of canonical token ids, retrieved by hashing into embedding tables) and §2.3

"The Engram module is integrated into the backbone via a residual connection".


<a id="dsv41-s242"></a>

## dsv41-s242

[DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

DeepSeek-AI, Anyi Xu, B. Li et al. · 2026 · arXiv:2609.19969

§2.4.2

> Each module uses $N$-gram orders $\\{2,3,4\\}$, with 8 hash heads

> The modules are placed at layers 1 and 14 (zero-indexed)


<a id="dsv41-engram"></a>

## dsv41-engram

[DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

DeepSeek-AI, Anyi Xu, B. Li et al. · 2026 · arXiv:2609.19969

[§4.2.1 Model Setups](https://arxiv.org/html/2609.19969#S4.SS2.SSS1)

> …multi-head hashing

> We employ MoE layers in all Transformer blocks


<a id="cfg-v4flash-rs"></a>

## cfg-v4flash-rs

DeepSeek-V4-Flash [`config.json`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/60d8d70770c6776ff598c94bb586a859a38244f1/config.json)

`routed_scaling_factor: 1.5`, `norm_topk_prob: true`, `num_experts_per_tok: 6`; transformers at main ff704ff multiplies the renormalized weights by it in both the learned and the hash router, [`modeling_deepseek_v4.py#L1082`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/deepseek_v4/modeling_deepseek_v4.py#L1082) and [L1113](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/deepseek_v4/modeling_deepseek_v4.py#L1113).


<a id="clark-appd"></a>

## clark-appd

[Unified Scaling Laws for Routed Language Models](https://arxiv.org/abs/2202.01169)

Aidan Clark, Diego de las Casas, Aurelia Guy et al. · 2022 · arXiv:2202.01169

[Appendix D Architectural Variations](https://arxiv.org/html/2202.01169#A4)

> …s-base scales well with routing frequency, but hash degrades in performance as shown in Fig. 11\. At a single routed layer, hash has the lowest validation loss across model sizes

> …hash flattens at higher frequencies


<a id="roller-hashfn"></a>

## roller-hashfn

[Hash Layers For Large Sparse Models](https://arxiv.org/abs/2106.04426)

Stephen Roller, Sainbayar Sukhbaatar, Arthur Szlam et al. · 2021 · arXiv:2106.04426

[§3.1 Hash Functions](https://arxiv.org/html/2106.04426#S5.T2)

Table 2: Comparison of Models on RoBERTa\+cc100en Data.

> …greedily assigning the most frequent tokens to the emptiest buckets

> …balanced assignment ... is more balanced, see Figure 4


<a id="dsv3-alpha"></a>

## dsv3-alpha

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

> For the balance loss, we set α to 0.0001


<a id="balance-dsv41"></a>

## balance-dsv41

[DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

DeepSeek-AI, Anyi Xu, B. Li et al. · 2026 · arXiv:2609.19969

[§2.1.1 Multimodal Architecture](https://arxiv.org/html/2609.19969#S2.SS1.SSS1)


<a id="balance-k3"></a>

## balance-k3

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

[§2.3.3 Quantile Balancing](https://arxiv.org/html/2607.24653#S2.SS3.SSS3)


<a id="balance-longcat"></a>

## balance-longcat

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

[§2.1.1 Computational Budget Control](https://arxiv.org/html/2509.01322#S2.SS1.SSS1)


<a id="balance-mimo26"></a>

## balance-mimo26

[MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://arxiv.org/abs/2610.11959)

Xiaomi LLM-Core Team, Zongming Qiao, Ziyue Hua et al. · 2026 · arXiv:2610.11959

[Figure 11](https://arxiv.org/html/2610.11959#S5.F11)

MiMo-V2.6-Pro expert-load balance at decoder layer 9 (384 experts) during RL, comparing runs with and without freezing the router.


<a id="balance-qwen3"></a>

## balance-qwen3

[Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)

An Yang, Anfeng Li, Baosong Yang et al. · 2025 · arXiv:2505.09388

architecture section


<a id="hf-qwen3moe"></a>

## hf-qwen3moe

transformers main at a96730c8, [`qwen3_moe/modeling_qwen3_moe.py#L257-L264`](https://github.com/huggingface/transformers/blob/a96730c8c97b8efbf35bbaf7f5da33ec99231a49/src/transformers/models/qwen3_moe/modeling_qwen3_moe.py#L257-L264)

softmax over all experts, top-k, divided by the top-k sum only `if self.norm_topk_prob`; no shared expert, sigmoid, selection bias or scaling factor in the file (grep); [`configuration_qwen3_moe.py#L51-L53`](https://github.com/huggingface/transformers/blob/a96730c8c97b8efbf35bbaf7f5da33ec99231a49/src/transformers/models/qwen3_moe/configuration_qwen3_moe.py#L51-L53) `attribute_map = {"num_experts": "num_local_experts"}`, L106 `norm_topk_prob: bool = False`.


<a id="dsmoe-device"></a>

## dsmoe-device

[DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066)

Damai Dai, Chengqi Deng, Chenggang Zhao et al. · 2024 · arXiv:2401.06066

§3.3

> …it becomes unnecessary to enforce strict balance constraints at the expert level, because excessive constraints on load balance will compromise model performance

> …we set a small expert-level balance factor to mitigate the risk of routing collapse, and meanwhile set a larger device-level balance factor


<a id="dsv2-coeffs"></a>

## dsv2-coeffs

[DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2405.04434

[§3.1.2 Hyper-Parameters](https://arxiv.org/html/2405.04434#S3.SS1.SSS2)

> As for balance losses, we set α1 to 0.003, α2 to 0.05, and α3 to 0.02


<a id="dsv3-nodevice"></a>

## dsv3-nodevice

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§2.1.2 DeepSeekMoE with Auxiliary-Loss-Free Load Balancing](https://arxiv.org/html/2412.19437#S2.SS1.SSS2)


<a id="deepinfer-eplb"></a>

## deepinfer-eplb

[DeepSeek V4.1 Flash 大规模推理部署实践 (the DeepInfer release post)](https://zhuanlan.zhihu.com/p/2095560295930508953)

DeepSeek-AI · Zhihu

DeepSeek-AI, *DeepSeek V4.1 Flash 大规模推理部署实践* (the DeepInfer release post), [Zhihu](https://zhuanlan.zhihu.com/p/2095560295930508953), section Expert-Parallel Load Balancer

> Measured \= 1.090


<a id="yuan3-t1"></a>

## yuan3-t1

[Yuan3.0 Ultra: A Trillion-Parameter Enterprise-Oriented MoE LLM](https://arxiv.org/abs/2601.14327)

YuanLab.ai, Shawn Wu, Jiangang Luo et al. · 2026 · arXiv:2601.14327

[Table 1](https://arxiv.org/html/2601.14327#S3.T1)

The impact of the hyperparameters of \\alpha and \\beta on training performance, and comparison among different auxiliary load balancing loss methods with different coefficient.

> …sequence-wise auxiliary loss from DeepSeek-V3


<a id="yuan3-l144"></a>

## yuan3-l144

[Yuan3.0 Ultra: A Trillion-Parameter Enterprise-Oriented MoE LLM](https://arxiv.org/abs/2601.14327)

YuanLab.ai, Shawn Wu, Jiangang Luo et al. · 2026 · arXiv:2601.14327

[§3.4.1 Sensitivity Analysis of Pruning Hyper-parameters](https://arxiv.org/html/2601.14327#S3.F5)

Figure 5: At the stable stage of pre-training (80B tokens), the token loads of individual experts under different auxiliary loss coefficient are illustrated, with experts sorted in descending order of token count.

> …substantially enforces load balancing across experts ... but this comes at the cost of degraded model accuracy

> …noticeable imbalance remains: in this case, the maximum token disparity within a layer can still reach approximately 13.6×


<a id="motif3-aux"></a>

## motif3-aux

[Motif 3: Technical Report](https://arxiv.org/abs/2608.09119)

Junghwan Lim, Joon Son Chung, Sungmin Lee et al. · 2026 · arXiv:2608.09119

[§4.2 MoE Training Stabilization, FP32 routing and selective load balancing](https://arxiv.org/html/2608.09119#S4.SS2.SSS0.Px1)

> …the earliest MoE layers were more susceptible to expert-load imbalance

> …we assign them stronger layer-specific auxiliary loss weights


<a id="lossfree-t2"></a>

## lossfree-t2

[Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664)

Lean Wang, Huazuo Gao, Chenggang Zhao et al. · 2024 · arXiv:2408.15664

Table 2 (validation set)

> Loss-Controlled

> 9.50, 0.04. §4.1: the baseline sets


<a id="lossfree-f2"></a>

## lossfree-f2

[Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664)

Lean Wang, Huazuo Gao, Chenggang Zhao et al. · 2024 · arXiv:2408.15664

Fig. 2 (1B, MaxVio\_global against validation perplexity, read off the plot)


<a id="sigma-early"></a>

## sigma-early

[Sigma-MoE-Tiny Technical Report](https://arxiv.org/abs/2512.16248)

Qingguo Hu, Zhenghao Lin, Ziyue Yang et al. · 2025 · arXiv:2512.16248

[§2.2.2 Progressive Sparsification Scheduling](https://arxiv.org/html/2512.16248#S2.SS2.SSS2)

> …routing collapse in the lower layers

> …takes a shortcut by driving p towards a uniform distribution


<a id="qiu-l57"></a>

## qiu-l57

[Demons in the Detail: On Implementing Load Balancing Loss for Training Specialized Mixture-of-Expert Models](https://arxiv.org/abs/2501.11873)

Zihan Qiu, Zeyu Huang, Bo Zheng et al. · 2025 · arXiv:2501.11873

[§2.2 Load-balancing Loss](https://arxiv.org/html/2501.11873#S2.SS2)

> …contains the domain-specific sequences

> …the router is still pushed to distribute tokens uniformly to all experts, thereby hurting MoE performance and preventing specialization


<a id="qiu-t1"></a>

## qiu-t1

[Demons in the Detail: On Implementing Load Balancing Loss for Training Specialized Mixture-of-Expert Models](https://arxiv.org/abs/2501.11873)

Zihan Qiu, Zeyu Huang, Bo Zheng et al. · 2025 · arXiv:2501.11873

[Table 1](https://arxiv.org/html/2501.11873#S4.T1)

Performance of different balance methods and Balance BSZ.


<a id="qiu-s42"></a>

## qiu-s42

[Demons in the Detail: On Implementing Load Balancing Loss for Training Specialized Mixture-of-Expert Models](https://arxiv.org/abs/2501.11873)

Zihan Qiu, Zeyu Huang, Bo Zheng et al. · 2025 · arXiv:2501.11873

[§4.2 Main Results](https://arxiv.org/html/2501.11873#S4.SS2)

> …methods using global-batch balance may experience local computational imbalance


<a id="qiu-t5"></a>

## qiu-t5

[Demons in the Detail: On Implementing Load Balancing Loss for Training Specialized Mixture-of-Expert Models](https://arxiv.org/abs/2501.11873)

Zihan Qiu, Zeyu Huang, Bo Zheng et al. · 2025 · arXiv:2501.11873

[Table 5](https://arxiv.org/html/2501.11873#S5.T5)

Performance and speed (seconds per iteration) in 43A6.6B setting.

> ; our copy L262:


<a id="dsv2-seq"></a>

## dsv2-seq

[DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2405.04434

[§2.2.3 Auxiliary Loss for Load Balance, Expert-Level Balance Loss](https://arxiv.org/html/2405.04434#S2.SS2.SSS3.Px1)

> T denotes the number of tokens in a sequence

> …we only employ a small expert-level balance loss with $\\alpha\_{1}\=0.001$, and do not employ device-level balance loss and communication balance loss for it


<a id="dsv3-seqwhy"></a>

## dsv3-seqwhy

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§2.1.2 DeepSeekMoE with Auxiliary-Loss-Free Load Balancing, Complementary Sequence-Wise Auxiliary Loss](https://arxiv.org/html/2412.19437#S2.SS1.SSS2.Px3)

> …to prevent extreme imbalance within any single sequence, we also employ a complementary sequence-wise balance loss


<a id="dsv3-s453"></a>

## dsv3-s453

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§4.5.3 Batch-Wise Load Balance VS. Sequence-Wise Load Balance](https://arxiv.org/html/2412.19437#S4.SS5.SSS3)

> 2.258 (using a sequence-wise auxiliary loss), 2.253 (using the auxiliary-loss-free method), and 2.253 (using a batch-wise auxiliary loss)


<a id="slicing-f12"></a>

## slicing-f12

[Slicing and Dicing: Configuring Optimal Mixtures of Experts](https://arxiv.org/abs/2605.11689)

Margaret Li, Sneha Kudugunta, Danielle Rothermel et al. · 2026 · arXiv:2605.11689

[Figure 12](https://arxiv.org/html/2605.11689#A3.F12)

Load Imbalance (§3.3).


<a id="slicing-s33"></a>

## slicing-s33

[Slicing and Dicing: Configuring Optimal Mixtures of Experts](https://arxiv.org/abs/2605.11689)

Margaret Li, Sneha Kudugunta, Danielle Rothermel et al. · 2026 · arXiv:2605.11689

[§3.3 Ablations](https://arxiv.org/html/2605.11689#S3.SS3)

> No setting clearly dominates at total expert count n≤128. However, with higher n, loss-free load balancing damages performance

> At large n, bias γ\=1e-3 may result in overly coarse-grained adjustments. Thus, the bias γ requires tuning, especially at high n


<a id="lossfree-f3"></a>

## lossfree-f3

[Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664)

Lean Wang, Huazuo Gao, Chenggang Zhao et al. · 2024 · arXiv:2408.15664

Fig. 3 (MaxVio\_batch over training steps, averaged over 100 steps, read off the plot)


<a id="zaya1-adamw"></a>

## zaya1-adamw

Zyphra, 2026, *ZAYA1-8B Technical Report*, arXiv:2605.05365, §II-A2

"Our PID optimizer uses AdamW internally, where the error signal passed to the optimizer is the difference between the empirical routing probability distribution and the uniform distribution"; L56: top-1 routing.


<a id="moonlight-centered"></a>

## moonlight-centered

[Muon is Scalable for LLM Training](https://arxiv.org/abs/2502.16982)

Jingyuan Liu, Jianlin Su, Xingcheng Yao et al. · 2025 · arXiv:2502.16982

App. C

> $b\_{i}\=b\_{i}\+u\\times(\\text{sign}(e\_{i})-\\text{sign}(e).\\text{mean}())$

> …in order to control the magnitude of the bias, while does not change the topk selection logic


<a id="trinity-centered"></a>

## trinity-centered

Arcee AI, 2026, *Arcee Trinity Large Technical Report*, arXiv:2602.17004, §2.3

"For Trinity Mini and Trinity Nano, we used the standard formulation of auxiliary-loss-free load balancing (Wang et al., 2024a), with an additional re-centering of the expert bias updates"; eq. 22 subtracts the mean bias after each sign step.


<a id="ckpt-bias-means"></a>

## ckpt-bias-means

Released weights, one tensor range-read per layer from each safetensors file, [DeepSeek-V3-Base](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base)

`mlp.gate.e_score_correction_bias`, layers 3 to 60, per-layer mean from 2.23 (layer 59\) to 8.04 (layer 48); [Moonlight-16B-A3B](https://huggingface.co/moonshotai/Moonlight-16B-A3B), all 26 MoE layers, absolute mean at most 3e-5; [ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B) `mlp.gate.balancing_biases`, the 16 experts of all 40 layers, absolute mean at most 9e-5; [LongCat-Flash-Chat](https://huggingface.co/meituan-longcat/LongCat-Flash-Chat) `mlp.router.e_score_correction_bias`, the 512 FFN experts of all 28 layers, mean from -0.0109 to -0.0055 (the 256 zero-computation slots are 0).


<a id="chang-cdb"></a>

## chang-cdb

[Causal Routing Bias for Aux-Loss-Free MoE Training](https://jonathanc.net/blog/causal-routing-bias)

Jonathan Chang · blog

Jonathan Chang, *Causal Routing Bias for Aux-Loss-Free MoE Training* (blog), [jonathanc.net/blog/causal-routing-bias](https://jonathanc.net/blog/causal-routing-bias)

> Heuristic Causal Bias (CB)

> Causal Dual Bias (CDB)


<a id="dsvl2-bias"></a>

## dsvl2-bias

Wu et al., 2024, *DeepSeek-V*, arXiv:2412.10302, §2

"we introduce a global bias term" for each expert "to cost-effectively improve load balancing between experts"; Table 1 (L67 to L68): sigmoid routing with expert correction bias for DeepSeek-VL2; Table 2 (L205): bias correction step 0.001 in its second training stage, on a mix of about 70% vision-language and 30% text-only data (L81).


<a id="kimivl-bias"></a>

## kimivl-bias

Kimi-VL-A3B-Instruct publisher [`config.json`](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct/blob/main/config.json)

`topk_method: noaux_tc`, `scoring_func: sigmoid`; its weights hold one `mlp.gate.e_score_correction_bias` per layer for all tokens, and they differ from Moonlight-16B-A3B-Instruct's, the language model it starts from (layer 13: std 0.075 against 0.051), so the bias kept updating during Kimi-VL's training.


<a id="idbal-t1"></a>

## idbal-t1

[ID Balancing: Stable Training of Extremely Sparse MoE via PID-Based Load Control](https://arxiv.org/abs/2609.39137)

Peng Jin, Zihan Qiu, Zekun Wang et al. · 2026 · arXiv:2609.39137

[Table 1](https://arxiv.org/html/2609.39137#S3.T1)

ID Balancing improves backbone load control while maintaining competitive LM loss.


<a id="k3-qb-why"></a>

## k3-qb-why

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

§2.3.3

> …slow adaptation against load oscillation

> Maintaining balanced loads becomes more challenging as LatentMoE increases the routed expert pool to 896 per layer


<a id="su-qb"></a>

## su-qb

Su Jianlin, kexue.fm post 11619, "MoE环游记：6、最优分配促均衡"

"也正是为此，我们称这个算法为“Quantile Balancing (QB)”。" (that is why we call this algorithm Quantile Balancing).


<a id="su-k3"></a>

## su-k3

Su Jianlin, kexue.fm post 11848, "简单谈谈K3的MoE和Attention"

"跟上一代模型K2一样，K3同样采用Loss-Free的负载均衡方案，但之前所用的SignSGD式更新规则，在K3这么大的总Expert数下表现已经不大稳定了，所以我们引入了QB" (like K2, K3 balances without a loss, but the SignSGD-style rule used before was no longer stable at K3's expert count, so QB was introduced).


<a id="eqb-t1"></a>

## eqb-t1

[Exact Quantile Balancing and Load-Error Injection for Mixture-of-Experts](https://arxiv.org/abs/2609.28053)

Pit Neitemeier, Jiaze Li, Alessio Serra et al. · 2026 · arXiv:2609.28053

[Table 1](https://arxiv.org/html/2609.28053#S5.T1)

100B-token ablation.


<a id="eqb-lim"></a>

## eqb-lim

[Exact Quantile Balancing and Load-Error Injection for Mixture-of-Experts](https://arxiv.org/abs/2609.28053)

Pit Neitemeier, Jiaze Li, Alessio Serra et al. · 2026 · arXiv:2609.28053

[§6 Conclusion, Limitations](https://arxiv.org/html/2609.28053#S6.SS0.SSS0.Px1)

> Local MaxVio is a proxy for dispatch cost rather than measured EP throughput


<a id="idbal-f5"></a>

## idbal-f5

[ID Balancing: Stable Training of Extremely Sparse MoE via PID-Based Load Control](https://arxiv.org/abs/2609.39137)

Peng Jin, Zihan Qiu, Zekun Wang et al. · 2026 · arXiv:2609.39137

[§3 ID Balancing](https://arxiv.org/html/2609.39137#S3.F5)

Figure 5: EMA smoothing reduces bias drift but slows load correction in Quantile Balancing.

> Why ID Balancing omits the proportional term

> …stronger smoothing reduces bias drift but weakens early load control


<a id="shape-dsv41"></a>

## shape-dsv41

[DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

DeepSeek-AI, Anyi Xu, B. Li et al. · 2026 · arXiv:2609.19969


<a id="shape-glm53"></a>

## shape-glm53

GLM-5.3 publisher [`config.json`](https://huggingface.co/zai-org/GLM-5.3/blob/main/config.json)

`n_routed_experts: 256`, `num_experts_per_tok: 8`, `moe_intermediate_size: 2048`, `n_shared_experts: 1`, `hidden_act: silu`; no activation-clipping limit specified.


<a id="shape-k3"></a>

## shape-k3

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

[§2.3 Stable LatentMoE](https://arxiv.org/html/2607.24653#S2.SS3)


<a id="shape-longcat"></a>

## shape-longcat

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

[§2.4 Model Information](https://arxiv.org/html/2509.01322#S2.SS4)


<a id="shape-mimo26"></a>

## shape-mimo26

MiMo-V2.6-Pro-RL publisher [`config.json`](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/config.json), text configuration

`n_routed_experts: 384`, `num_experts_per_tok: 8`, `moe_intermediate_size: 2048`, `n_shared_experts: null`, `hidden_act: silu`; no activation-clipping limit specified.


<a id="shape-nemotron-ultra"></a>

## shape-nemotron-ultra

Nemotron 3 Ultra publisher [`config.json`](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4/blob/main/config.json)

`n_routed_experts: 512`, `num_experts_per_tok: 22`, `moe_intermediate_size: 5120`, `hidden_size: 8192`, `moe_latent_size: 2048`, `moe_shared_expert_intermediate_size: 10240`, `mlp_hidden_act: relu2`.


<a id="shape-qwen38"></a>

## shape-qwen38

Qwen3.8-2.4T-A95B publisher [`config.json`](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/config.json)

`num_experts: 512`, `num_experts_per_tok: 10`, `moe_intermediate_size: 2048`, `shared_expert_intermediate_size: 2048`, `hidden_act: silu`; no activation-clipping limit specified.


<a id="shape-step5"></a>

## shape-step5

Step 5 Preview publisher [`config.json`](https://huggingface.co/stepfun-ai/Step-5-Preview-BF16/blob/main/config.json), text configuration

`moe_num_experts: 352`, `moe_top_k: 8`, `moe_intermediate_size: 1536`, `share_expert_dim: 1536`; `swiglu_limits` and `swiglu_limits_shared` both set to 7.0 throughout.


<a id="liew-t6"></a>

## liew-t6

[Towards Principled Design of Mixture-of-Experts Language Models under Memory and Inference Constraints](https://arxiv.org/abs/2601.08215)

Seng Pei Liew, Kenta Shinzato, Yuyang Dong · 2026 · arXiv:2601.08215

[Table 6](https://arxiv.org/html/2601.08215#A2.T6)

Detailed results for the granularity g ablation study with fixed total and active parameters.


<a id="cfg-granularity"></a>

## cfg-granularity

Publisher configs (hidden size / routed expert width, experts / top-k)

gpt-oss-120b [`config.json`](https://huggingface.co/openai/gpt-oss-120b/blob/b5c939de8f754692c1647ca79fbf85e8c1e70f8a/config.json) `hidden_size: 2880`, `intermediate_size: 2880`, `num_local_experts: 128`, `num_experts_per_tok: 4`; Trinity Large [`config.json`](https://huggingface.co/arcee-ai/Trinity-Large-Base/blob/b2a665b40e5d67b05fb164205cf63155f7958e2a/config.json) (Trinity-Large-Base) `hidden_size: 3072`, `moe_intermediate_size: 3072`, `num_experts: 256`, `num_experts_per_tok: 4`; Mistral Small 4 [`config.json`](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/blob/a11f36bebf709121056b1dbcc943d1c6afbe494d/config.json) `hidden_size: 4096`, `moe_intermediate_size: 2048`, `n_routed_experts: 128`, `num_experts_per_tok: 4`; Qwen3.5-35B-A3B [`config.json`](https://huggingface.co/Qwen/Qwen3.5-35B-A3B/blob/59d61f3ce65a6d9863b86d2e96597125219dc754/config.json) `hidden_size: 2048`, `moe_intermediate_size: 512`, `num_experts: 256`, `num_experts_per_tok: 8`.


<a id="longcat-ngram-f2"></a>

## longcat-ngram-f2

Liu et al. (Meituan LongCat), 2026, *Scaling Embeddings Outperforms Scaling Experts in Language Models*, arXiv:2601.21204, Fig. 2 and §3.2.1, 280M active parameters, 300B tokens

"at high sparsity levels, the benefits of N-gram Embedding become significantly more pronounced"; "the intersection point lies slightly above a ratio of 20\. At this juncture, N-gram Embedding parameters constitute approximately 50% of the total parameter count (given that the base MoE model maintains a ratio of 12)"; "Allocate no more than 50% of the total parameter budget to N-gram Embedding." Tables added to the low-ratio base (about 3.8 times active, read off Fig. 2\) stay above the experts line. English validation panel, exact path coordinates in the paper's Fig. 2 SVG (arXiv v2 source, `scaling-200M_pol_n.svg`): base 11.87, crossing 20.6, so tables hold (20.6 \- 11.87) / 20.6 \= 42% of the parameters there; the paper's own "slightly above 20" on a base of 12 gives about 40%. Training loss crosses at about 33 and Chinese validation at about 30\. At 17.2 times active, the tables run reads 2.965 against 2.974 for more experts (Fig. 2 SVG coordinates), about 0.01 lower.


<a id="flashlite-ngram"></a>

## flashlite-ngram

Liu et al. (Meituan LongCat), 2026, *Scaling Embeddings Outperforms Scaling Experts in Language Models*, arXiv:2601.21204, §6

LongCat-Flash-Lite "has 68.5 billion total parameters" and "includes 31.4B N-gram Embedding parameters, accounting for 46% of the total"; [`config.json`](https://huggingface.co/meituan-longcat/LongCat-Flash-Lite/blob/b62b68827ead0b7fef3ba98b57f18484acaaec06/config.json) `ngram_vocab_size_ratio: 78`, `vocab_size: 131072`, `hidden_size: 3072` (78 x 131,072 x 3,072 \= 31.4B).


<a id="chinchilla-allocation"></a>

## chinchilla-allocation

[Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)

Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch et al. · 2022 · arXiv:2203.15556

abstract and section 2


<a id="mosaic-f1"></a>

## mosaic-f1

[Compute-Optimal Is Not Cluster-Optimal: Systems-Aware Scaling for Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.10605)

Soumajyoti Sarkar, Yuxin Tang, Sheng Zha · 2026 · arXiv:2608.10605

[Figure 1](https://arxiv.org/html/2608.10605#S1.F1)

The systems-aware scaling motivation for MOSAIC.

> …sparser MoE models reach lower loss at any model-FLOPs budget with the optimal sparsity sitting at the boundary

> …is minimized at the interior sparsity S\*\_cluster and is 0.031 nats lower than at S\* \= S\_max


<a id="step35-dead"></a>

## step35-dead

[Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters](https://arxiv.org/abs/2602.10604)

Ailin Huang, Ang Li, Aobo Kong et al. · 2026 · arXiv:2602.10604

§4.1.2

> …experts receiving negligible token dispatch for extended periods

> …expert collapse can also manifest as an \*expert-side\* pathology even when router dispatch remains stable, i.e., vanishing expert activations and stagnant or decaying expert parameter norms


<a id="latentmoe-alpha"></a>

## latentmoe-alpha

[LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts](https://arxiv.org/abs/2601.18089)

Venmugil Elango, Nidhi Bhatia, Roger Waleffe et al. · 2026 · arXiv:2601.18089


<a id="latentmoe-t4"></a>

## latentmoe-t4

[LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts](https://arxiv.org/abs/2601.18089)

Venmugil Elango, Nidhi Bhatia, Roger Waleffe et al. · 2026 · arXiv:2601.18089

[Table 4](https://arxiv.org/html/2601.18089#S4.T4)

Accuracy comparisons of hybrid Mamba-Attention MoEs with and without LatentMoE.


<a id="mhlatent-t1"></a>

## mhlatent-t1

[Multi-Head LatentMoE and Head Parallel: Communication-Efficient and Deterministic MoE Parallelism](https://arxiv.org/abs/2602.04870)

Chenwei Cui, Rockwell Jackson, Benjamin Joseph Herrera et al. · 2026 · arXiv:2602.04870

[Table 1](https://arxiv.org/html/2602.04870#S4.T1)

Model performance comparison across feedforward designs.


<a id="cfg-latent"></a>

## cfg-latent

Publisher configs

Nemotron 3 Super [`config.json`](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16/blob/2dc98e2afe4face0e4ce40972a915c45368bd34a/config.json) `moe_latent_size: 1024` against `hidden_size: 4096`, `mlp_hidden_act: "relu2"`; Nemotron 3 Ultra [`config.json`](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16/blob/77df655d5e9f8362164ed14dd8b48f8bce657498/config.json) `moe_latent_size: 2048` against `hidden_size: 8192`, `mlp_hidden_act: "relu2"`; Kimi K3 [`config.json`](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/config.json) `routed_expert_hidden_size: 3584` against `hidden_size: 7168`, with `latent_moe_use_norm: true`.


<a id="latentmoe-t5"></a>

## latentmoe-t5

[LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts](https://arxiv.org/abs/2601.18089)

Venmugil Elango, Nidhi Bhatia, Roger Waleffe et al. · 2026 · arXiv:2601.18089

[Table 5](https://arxiv.org/html/2601.18089#S4.T5)

Comparison of LatentMoE and Standard MoE performance metrics.


<a id="latentmoe-opt"></a>

## latentmoe-opt

[LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts](https://arxiv.org/abs/2601.18089)

Venmugil Elango, Nidhi Bhatia, Roger Waleffe et al. · 2026 · arXiv:2601.18089

[§4.3 Inference Performance](https://arxiv.org/html/2601.18089#S4.SS3)

> …separate CUDA streams for routed and shared experts

> …ensure that inner dimensions remain large enough ... avoid SM-bound workloads


<a id="k3-latent"></a>

## k3-latent

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

[§2.3 Stable LatentMoE](https://arxiv.org/html/2607.24653#S2.SS3)

> This ill-conditioned structure, combined with the 2.8-trillion-parameter scale, produces exploding internal activations in the routed branch

> …to suppress activation explosion


<a id="cfg-k3"></a>

## cfg-k3

Kimi K3 [`config.json`](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/config.json)

`latent_moe_use_norm: true`, `routed_scaling_factor: 1.0`, `activation_situ_beta 4.0`, `activation_situ_linear_beta 25.0`.


<a id="dsmoe-shared-purpose"></a>

## dsmoe-shared-purpose

[DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066)

Damai Dai, Chengqi Deng, Chenggang Zhao et al. · 2024 · arXiv:2401.06066


<a id="dsmoe-f3"></a>

## dsmoe-f3

[DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066)

Damai Dai, Chengqi Deng, Chenggang Zhao et al. · 2024 · arXiv:2401.06066

[§4.4 Ablation Studies, Shared Expert Isolation](https://arxiv.org/html/2401.06066#S4.F3)

Figure 3: Ablation studies for DeepSeekMoE.

> …the intentional isolation of a shared expert yields improved performance across a majority of benchmarks


<a id="qwen3-moe"></a>

## qwen3-moe

[Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)

An Yang, Anfeng Li, Baosong Yang et al. · 2025 · arXiv:2505.09388

[§2 Architecture](https://arxiv.org/html/2505.09388#S2)

> …the Qwen3-MoE design excludes shared experts


<a id="cfg-qwen3next"></a>

## cfg-qwen3next

`Qwen/Qwen3-Next-80B-A3B-Instruct` [`config.json`](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct/blob/9c7f2fbe84465e40164a94cc16cd30b6999b0cc7/config.json)

`shared_expert_intermediate_size: 512`, `model_type: qwen3_next`; its `shared_expert_gate` output goes through `F.sigmoid` in transformers ([`modeling_qwen3_next.py#L854`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/qwen3_next/modeling_qwen3_next.py#L854)). The same config has `norm_topk_prob: true`, so the routed weights sum to 1 and the gated shared expert takes sigmoid/(1 \+ sigmoid), below 50%, of the output weight.


<a id="cfg-qwen35"></a>

## cfg-qwen35

Qwen3.5-397B [`config.json`](https://huggingface.co/Qwen/Qwen3.5-397B-A17B/blob/8472618112abcbd45acbcdc58436aff4233c23f7/config.json)

`shared_expert_intermediate_size: 1024`; transformers [`modular_qwen3_5_moe.py#L196`](https://github.com/huggingface/transformers/blob/ff704ffd47d800e31b31f2f81a5a2952fb0fbf71/src/transformers/models/qwen3_5_moe/modular_qwen3_5_moe.py#L196) subclasses `Qwen3NextSparseMoeBlock`.


<a id="pangu-ultra-f2"></a>

## pangu-ultra-f2

[Pangu Ultra MoE: How to Train Your Big MoE on Ascend NPUs](https://arxiv.org/abs/2505.04519)

Yehui Tang, Yichun Yin, Yaoyuan Wang et al. · 2025 · arXiv:2505.04519

[Figure 2](https://arxiv.org/html/2505.04519#S2.F2)

Shared expert ablation.


<a id="et-t8"></a>

## et-t8

[Expert Threshold Routing for Autoregressive Language Modeling with Dynamic Computation Allocation and Load Balancing](https://arxiv.org/abs/2603.11535)

Hanchi Sun, Yixin Liu, Yonghui Wu et al. · 2026 · arXiv:2603.11535

[Table 8](https://arxiv.org/html/2603.11535#A5.T8)

Ablation on the shared expert mechanism.


<a id="olmoe-f6"></a>

## olmoe-f6

[OLMoE: Open Mixture-of-Experts Language Models](https://arxiv.org/abs/2409.02060)

Niklas Muennighoff, Luca Soldaini, Dirk Groeneveld et al. · 2024 · arXiv:2409.02060

[§4.1.3 Shared Experts](https://arxiv.org/html/2409.02060#S4.F6)

Figure 6: Shared experts.

> …sharing an expert performs slightly worse


<a id="slicing-shared"></a>

## slicing-shared

[Slicing and Dicing: Configuring Optimal Mixtures of Experts](https://arxiv.org/abs/2605.11689)

Margaret Li, Sneha Kudugunta, Danielle Rothermel et al. · 2026 · arXiv:2605.11689

[§3.2 Additional Expert Configurations: Generalists and Heterogeneity, Generalists do not improve performance](https://arxiv.org/html/2605.11689#S3.SS2.SSS0.Px2)

> …comparable to or slightly degraded


<a id="mellum2-shared"></a>

## mellum2-shared

[Mellum2 Technical Report](https://arxiv.org/abs/2605.31268)

Marko Kojic, Ivan Bondyrev, Aral de Moor et al. · 2026 · arXiv:2605.31268

[Appendix A Architecture Exploration Details, A.2  MoE Architecture Exploration](https://arxiv.org/html/2605.31268#A1.SS2)

> Adding a shared expert (always active in addition to the routed top-k) yielded no measurable quality gain at our scale and consistently hurt inference performance because of the extra always-on FFN compute per token.


<a id="grok2-parallel"></a>

## grok2-parallel

Grok 2, [`config.json`](https://huggingface.co/xai-org/grok-2/blob/main/config.json)

a dense MLP runs alongside the MoE, and their outputs are combined with a factor of 1/√2. `Grok1MoE` builds its router with `TopK(..., renormalize=False)`, so the top-2 softmax weights sum to less than 1 while the dense MLP keeps weight 1\.


<a id="cfg-glm45air"></a>

## cfg-glm45air

`zai-org/GLM-4.5-Air` [`config.json`](https://huggingface.co/zai-org/GLM-4.5-Air/blob/a24ceef6ce4f3536971efe9b778bdaa1bab18daa/config.json)

`n_shared_experts: 1`, `norm_topk_prob: true`, `routed_scaling_factor: 1.0`.


<a id="cfg-mistral-large3"></a>

## cfg-mistral-large3

`mistralai/Mistral-Large-3-675B-Instruct-2512` [`params.json`](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512/blob/383ffea2c7d60dfd44ca960e8e691709d4fdb9cd/params.json)

`moe.num_shared_experts: 1`, `moe.routed_scale: 1.0`; vLLM maps it onto DeepSeek-V3's MoE with `norm_topk_prob = True` ([`configs/mistral.py#L285-L306`](https://github.com/vllm-project/vllm/blob/d881812500b49bc77c8e1106664c75ffee16958e/vllm/transformers_utils/configs/mistral.py#L285-L306)).


<a id="shared-glm53"></a>

## shared-glm53

[GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763)

GLM-5-Team, Aohan Zeng, Xin Lv et al. · 2026 · arXiv:2602.15763

[Appendix A Hyper-Parameters](https://arxiv.org/html/2602.15763#A1)


<a id="shared-k3"></a>

## shared-k3

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

[Figure 2](https://arxiv.org/html/2607.24653#S2.F2)

The Kimi K3 architecture, organized around token, channel, and layer mixing, with a native vision pathway at the input.


<a id="shared-dsv41"></a>

## shared-dsv41

[DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

DeepSeek-AI, Anyi Xu, B. Li et al. · 2026 · arXiv:2609.19969

architecture and model hyperparameters


<a id="shared-mimo26"></a>

## shared-mimo26

[MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://arxiv.org/abs/2610.11959)

Xiaomi LLM-Core Team, Zongming Qiao, Ziyue Hua et al. · 2026 · arXiv:2610.11959

text backbone architecture


<a id="longcat-budget"></a>

## longcat-budget

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

[§2.1 Zero-Computation Experts](https://arxiv.org/html/2509.01322#S2.SS1)


<a id="longcat-f3c"></a>

## longcat-f3c

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

Fig. 3c and §2.1.1

> The standard deviation of activated FFN experts grows to 3

> …the standard deviation persisted at a relatively high level


<a id="modse-f2"></a>

## modse-f2

[Mixture of Diverse Size Experts](https://arxiv.org/abs/2409.12210)

Manxi Sun, Wei Liu, Jian Luan et al. · 2024 · arXiv:2409.12210

[Figure 2](https://arxiv.org/html/2409.12210#S4.F2)

Training and validation loss curves for the 300M\\times 8 and 700M\\times 8 models, with cross-entropy loss values indicated on the curves.


<a id="cfg-mixtral"></a>

## cfg-mixtral

`mistralai/Mixtral-8x7B-v0.1` [`config.json`](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1/blob/fc7ac94680e38d7348cfa806e51218e6273104b0/config.json)

`num_local_experts: 8`, `num_experts_per_tok: 2`, one expert width (`intermediate_size: 14336`).


<a id="longcat-f3a"></a>

## longcat-f3a

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

[Figure 3](https://arxiv.org/html/2509.01322#S2.F3)

(a) Validation loss curve comparing models with/without zero-computation experts under matched computation budgets.

> The baseline (top-k\=8, blue) activates fixed 6B parameters per token, while the zero-expert variant (top-k\=12, orange) dynamically activates 4.2B-7.0B parameters but maintains 8 FFN experts expectation (with fluctuation less than 1%). The consistent loss reduction demonstrates the efficacy of zero-computation experts.


<a id="hmoe-3b"></a>

## hmoe-3b

[HMoE: Heterogeneous Mixture of Experts for Language Modeling](https://arxiv.org/abs/2408.10681)

An Wang, Xingwu Sun, Ruobing Xie et al. · 2024 · arXiv:2408.10681


<a id="slicing-pools"></a>

## slicing-pools

[Slicing and Dicing: Configuring Optimal Mixtures of Experts](https://arxiv.org/abs/2605.11689)

Margaret Li, Sneha Kudugunta, Danielle Rothermel et al. · 2026 · arXiv:2605.11689

> …one router per pool


<a id="grove-infer"></a>

## grove-infer

[Grove MoE: Towards Efficient and Superior MoE LLMs with Adjugate Experts](https://arxiv.org/abs/2508.07785)

Haoyuan Wu, Haoxing Chen, Xiaodong Chen et al. · 2025 · arXiv:2508.07785


<a id="cfg-swiglu"></a>

## cfg-swiglu

`hidden_act: silu` with gated experts in [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/e815299b0bcbac849fa540c768ef21845365c9eb/config.json)


<a id="powlu-t2"></a>

## powlu-t2

[PowLU: An Activation Function for Stable Pre-Training of LLMs](https://arxiv.org/abs/2605.25704)

Peijie Jiang, Yuqi Feng, Cunyin Peng et al. · 2026 · arXiv:2605.25704

[Table 2](https://arxiv.org/html/2605.25704#S4.T2)

Comparisons among SwiGLU, SwiGLU-Clip, and PowLU activation functions.


<a id="powlu-f4"></a>

## powlu-f4

[PowLU: An Activation Function for Stable Pre-Training of LLMs](https://arxiv.org/abs/2605.25704)

Peijie Jiang, Yuqi Feng, Cunyin Peng et al. · 2026 · arXiv:2605.25704

[§4.3.1 Loss Spike Analysis](https://arxiv.org/html/2605.25704#S4.F4)

Figure 4: Visualization of the training loss curves of large-scale LLMs with SwiGLU, SwiGLU-Clip, or PowLU activation functions.

> …delayed the timing of loss spikes compared to the SwiGLU baseline with FP8 training ... but it also suffers from the loss spike around training step 77,000


<a id="kexaone-peak"></a>

## kexaone-peak

LG AI Research, 2026, *K-EXAONE 2.0 Technical Report*, arXiv:2608.04505, §2.2 Training stability

"with the clamp disabled at inference, the peak SwiGLU activation grows monotonically with depth and reaches 6862 at the last layer, while the clamp holds it at silu(τ)·τ \= 48.96" (its clamp is 7).


<a id="polynorm-t2"></a>

## polynorm-t2

[Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://arxiv.org/abs/2411.03884)

Zhijian Zhuo, Ya Wang, Yutao Zeng et al. · 2024 · arXiv:2411.03884

[Table 2](https://arxiv.org/html/2411.03884#S4.T2)

Validation losses of MoE models with different activation functions.


<a id="motif3-f6a"></a>

## motif3-f6a

[Motif 3: Technical Report](https://arxiv.org/abs/2608.09119)

Junghwan Lim, Joon Son Chung, Sungmin Lee et al. · 2026 · arXiv:2608.09119

[Figure 6](https://arxiv.org/html/2608.09119#S4.F6)

MoE component training comparisons from controlled experiments using models with approximately 10 billion parameters.


<a id="k3-appb"></a>

## k3-appb

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

[Appendix B Details of Sigmoid Tanh Unit GLU](https://arxiv.org/html/2607.24653#A2)

> …better training behavior


<a id="dsv41-activation"></a>

## dsv41-activation

[DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

DeepSeek-AI, Anyi Xu, B. Li et al. · 2026 · arXiv:2609.19969

model hyperparameters


<a id="cfg-clamp10"></a>

## cfg-clamp10

`swiglu_limit: 10` in [`ai-sage/GigaChat3.5-432B-A28B`](https://huggingface.co/ai-sage/GigaChat3.5-432B-A28B/blob/d10dcaeccb04ca3186fdfa3bb3874b4474e6b41b/config.json)


<a id="step35-ratio"></a>

## step35-ratio

[Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters](https://arxiv.org/abs/2602.10604)

Ailin Huang, Ang Li, Aobo Kong et al. · 2026 · arXiv:2602.10604


<a id="step5-activation"></a>

## step5-activation

Step 5 Preview publisher [`config.json`](https://huggingface.co/stepfun-ai/Step-5-Preview-BF16/blob/main/config.json), text configuration

`swiglu_limits` and `swiglu_limits_shared` both specify 7.0 across layers.


<a id="layout-dsv3"></a>

## layout-dsv3

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§2 Architecture](https://arxiv.org/html/2412.19437#S2)


<a id="layout-dsv41"></a>

## layout-dsv41

[DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

DeepSeek-AI, Anyi Xu, B. Li et al. · 2026 · arXiv:2609.19969

[§2 Architecture](https://arxiv.org/html/2609.19969#S2)


<a id="layout-glm53"></a>

## layout-glm53

GLM-5.3 publisher [`config.json`](https://huggingface.co/zai-org/GLM-5.3/blob/main/config.json)

`num_hidden_layers: 78`, `first_k_dense_replace: 3`, `moe_layer_freq: 1`.


<a id="layout-k3"></a>

## layout-k3

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

[§2 Model Architecture](https://arxiv.org/html/2607.24653#S2)


<a id="cfg-maverick"></a>

## cfg-maverick

`unsloth/Llama-4-Maverick-17B-128E-Instruct` [`config.json`](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct/blob/86c5ecb6f2fbddf604c60120125fb202e09f2556/config.json), `text_config`

`interleave_moe_layer_step` 2, `moe_layers` \[1, 3, ..., 47\], 48 layers, so layer 0 is dense.


<a id="layout-longcat"></a>

## layout-longcat

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

[§2 Architecture](https://arxiv.org/html/2509.01322#S2.F2)

Figure 2: The architecture adopted in LongCat-Flash.


<a id="layout-mimo26"></a>

## layout-mimo26

[MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://arxiv.org/abs/2610.11959)

Xiaomi LLM-Core Team, Zongming Qiao, Ziyue Hua et al. · 2026 · arXiv:2610.11959

text backbone architecture


<a id="cfg-moe-every"></a>

## cfg-moe-every

An MoE in every layer, [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B/blob/ad44e777bcd18fa416d9da3bd8f70d33ebb85d39/config.json)

`decoder_sparse_step: 1`, `mlp_only_layers: []`; [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b/blob/b5c939de8f754692c1647ca79fbf85e8c1e70f8a/config.json) (36 layers, each with 128 experts); [MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2/blob/04312f0cfbdeefb912575595b7c045512a29293c/config.json), whose transformers `MiniMaxM2DecoderLayer` builds a sparse MoE block in every layer; [Llama 4 Scout](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct/blob/afd8e498c87bda51c7ea8ec68ea2f7c066e6340b/config.json) `interleave_moe_layer_step: 1`.


<a id="dsv3-dense"></a>

## dsv3-dense

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§4.2 Hyper-Parameters, Model Hyper-Parameters](https://arxiv.org/html/2412.19437#S4.SS2.SSS0.Px1)

> We substitute all FFNs except for the first three layers with MoE layers


<a id="ling-el"></a>

## ling-el

[Towards Greater Leverage: Scaling Laws for Efficient Mixture-of-Experts Language Models](https://arxiv.org/abs/2507.17702)

Changxin Tian, Kunlong Chen, Jia Liu et al. · 2025 · arXiv:2507.17702

[§4.1.4 Other Configurations of MoE Architecture](https://arxiv.org/html/2507.17702#S4.SS1.SSS4)

> 60-layer models with the first 1-3 layers set dense ... efficiency leverage close to 1 within a FLOPs budget of up to 3e20


<a id="dsmoe-early"></a>

## dsmoe-early

[DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066)

Damai Dai, Chengqi Deng, Chenggang Zhao et al. · 2024 · arXiv:2401.06066

[§5.1.2 Hyper-Parameters, Model Settings](https://arxiv.org/html/2401.06066#S5.SS1.SSS2.Px1)

> …load balance status converges especially slower for the first layer


<a id="ling-early"></a>

## ling-early

[Towards Greater Leverage: Scaling Laws for Efficient Mixture-of-Experts Language Models](https://arxiv.org/abs/2507.17702)

Changxin Tian, Kunlong Chen, Jia Liu et al. · 2025 · arXiv:2507.17702

[Appendix D Additional Experiments, Arrangement of MoE and Dense Layers](https://arxiv.org/html/2507.17702#A4.SS0.SSS0.Px2)

> …mitigates routing imbalances in the early layers


<a id="nucleus-dense"></a>

## nucleus-dense

[Nucleus-Image: Sparse MoE for Image Generation](https://arxiv.org/abs/2604.12163)

Chandan Akiti, Ajay Modukuri, Murali Nandan Nagarapu et al. · 2026 · arXiv:2604.12163

[§3.5 Architectural Choices for Training Stability](https://arxiv.org/html/2604.12163#S3.SS5)

> The first three transformer layers (indices 0, 1, 2\) use dense ... without dense initial layers ... leading to divergence


<a id="solar-early"></a>

## solar-early

[Solar Open Technical Report](https://arxiv.org/abs/2601.07022)

Sungrae Park, Sanghoon Kim, Jungho Cho et al. · 2026 · arXiv:2601.07022

[§2.2 Mixture-of-Experts Architecture, Architectural Design Process](https://arxiv.org/html/2601.07022#S2.SS2.SSS0.Px1)

> …we follow gpt-oss-120b in using MoE layers throughout

> …early layers consistently exhibit severe imbalance ... introducing load balancing loss resolves this issue


<a id="ernie5-first"></a>

## ernie5-first

[ERNIE 5.0 Technical Report](https://arxiv.org/abs/2602.04705)

Haifeng Wang, Hua Wu, Tian Wu et al. · 2026 · arXiv:2602.04705

[§6.4.1 Modality-Agnostic Expert Routing, Perspective of Load Balancing](https://arxiv.org/html/2602.04705#S6.SS4.SSS1.Px3)

> …consistently high and stable ... across almost all layers

> …the first layer does not show severe imbalance, contradicting the common assumption that early MoE layers require dense designs


<a id="parallel-block"></a>

## parallel-block

[`CohereLabs/North-Mini-Code-1.0`](https://huggingface.co/CohereLabs/North-Mini-Code-1.0/blob/d11e61a842617a22dc328552fa5bb86231ee4f37/config.json)

`x = x + l_attn + l_mlp`, with both read from `layer_norm(x)`.


<a id="longcat-scmoe"></a>

## longcat-scmoe

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

> …allows the dense FFN from the preceding block to execute in parallel with the dispatch/combine communication of the current MoE layer

> …allows the computation of the preceding block to be fully parallel with its dispatch and combine communication phases


<a id="scmoe-pos"></a>

## scmoe-pos

[Shortcut-connected Expert Parallelism for Accelerating Mixture-of-Experts](https://arxiv.org/abs/2404.05019)

Weilin Cai, Juyong Jiang, Le Qin et al. · 2024 · arXiv:2404.05019

§3.1

> …output, intermediate, and input

> …we favor selecting 'Pos-2' for practical development


<a id="scmoe-t2"></a>

## scmoe-t2

[Shortcut-connected Expert Parallelism for Accelerating Mixture-of-Experts](https://arxiv.org/abs/2404.05019)

Weilin Cai, Juyong Jiang, Le Qin et al. · 2024 · arXiv:2404.05019

[Table 2](https://arxiv.org/html/2404.05019#S4.T2)

Comparison of zero-shot evaluation and end-to-end speedup of training and inference (one iteration) for the pre-trained GPT2-MoE and LLaMA2-MoE models with various architectures in the 8\\timesA800-NVLink…


<a id="longcat-shortcut"></a>

## longcat-shortcut

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

[§2.1.2 Load Balance Control](https://arxiv.org/html/2509.01322#S2.SS1.SSS2)

> …virtually indistinguishable


<a id="instella-t13"></a>

## instella-t13

[Instella-MoE Technical Report](https://arxiv.org/abs/2609.00791)

Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra et al. · 2026 · arXiv:2609.00791

[Table 13](https://arxiv.org/html/2609.00791#S3.T13)

Architecture ablation.


<a id="farskip-t3"></a>

## farskip-t3

[FarSkip-Collective: Unhobbling Blocking Communication in Mixture of Experts Models](https://arxiv.org/abs/2511.11505)

Yonatan Dukler, Guihong Li, Deval Shah et al. · 2025 · arXiv:2511.11505

[§5.1 Model Capabilities](https://arxiv.org/html/2511.11505#S5.T3)

Table 3: Pretraining model performance of Regular and FarSkip-Collective MoE using DS-V2-Lite architecture (16B) trained on 200B tokens.

> …on par performance with 0.3% gap


<a id="instella-tput"></a>

## instella-tput

[Instella-MoE Technical Report](https://arxiv.org/abs/2609.00791)

Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra et al. · 2026 · arXiv:2609.00791

[§3.4 Training Efficiency](https://arxiv.org/html/2609.00791#S3.SS4)

> 12.7% pre-training throughput improvement


<a id="longcat-overlap"></a>

## longcat-overlap

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

[§5.3 Distributed Strategy for Large-scale Training](https://arxiv.org/html/2509.01322#S5.SS3)

> …each comprising 32 accelerators

> …decreases from 25.3% to 8.4% with ScMoE architecture


<a id="shazeer-collapse"></a>

## shazeer-collapse

[Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)

Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz et al. · 2017 · arXiv:1701.06538

[§4 Balancing Expert Utilization](https://arxiv.org/html/1701.06538#S4)

> …the gating network tends to converge to a state where it always produces large weights for the same few experts. This imbalance is self-reinforcing, as the favored experts are trained more rapidly and thus are selected even more


<a id="train-dsv3"></a>

## train-dsv3

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§4.2 Hyper-Parameters](https://arxiv.org/html/2412.19437#S4.SS2)

> …we maintain the original precision (e.g., BF16 or FP32) for the following components: the embedding module, the output head, MoE gating modules, normalization operators, and attention operators

> …ensure stable training dynamics


<a id="train-dsv41"></a>

## train-dsv41

[DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969)

DeepSeek-AI, Anyi Xu, B. Li et al. · 2026 · arXiv:2609.19969

[§2.1 Overview](https://arxiv.org/html/2609.19969#S2.SS1)

> SwiGLU activation function with clamping (OpenAI, 2025\) at a threshold of 10


<a id="train-k3"></a>

## train-k3

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

[§2.3 Stable LatentMoE](https://arxiv.org/html/2607.24653#S2.SS3)

> …we keep the attention output in FP32 during training

> …language and vision are jointly optimized from the start of training, rather than grafting a vision encoder onto a pre-trained language model


<a id="train-longcat"></a>

## train-longcat

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

§2.3.4 and §3.3 to §3.4

> …we adopt ε\=1e-16

> Adam LR Full Align


<a id="train-step35"></a>

## train-step35

[Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters](https://arxiv.org/abs/2602.10604)

Ailin Huang, Ang Li, Aobo Kong et al. · 2026 · arXiv:2602.10604

[§4.1 Training Stability](https://arxiv.org/html/2602.10604#S4.SS1)

> This observation leads us to prefer activation clipping over weight clipping


<a id="sparse-upcycle-lr"></a>

## sparse-upcycle-lr

[Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints](https://arxiv.org/abs/2212.05055)

Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp et al. · 2022 · arXiv:2212.05055

[Appendix A Training and evaluation details, A.1.1 Language](https://arxiv.org/html/2212.05055#A1.SS1.SSS1)

> …continuing the inverse square root learning rate schedule where the dense checkpoint left off


<a id="sparse-upcycle-opt"></a>

## sparse-upcycle-opt

[Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints](https://arxiv.org/abs/2212.05055)

Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp et al. · 2022 · arXiv:2212.05055

[§3.1 Design Decisions](https://arxiv.org/html/2212.05055#S3.SS1)

> …gives a performance boost for vision models

> We did not, however, see any improvement from reusing the dense model optimizer state in our language experiments


<a id="olmoe-upcycle"></a>

## olmoe-upcycle

[OLMoE: Open Mixture-of-Experts Language Models](https://arxiv.org/abs/2409.02060)

Niklas Muennighoff, Luca Soldaini, Dirk Groeneveld et al. · 2024 · arXiv:2409.02060

[§4.1.5 Sparse Upcycling](https://arxiv.org/html/2409.02060#S4.SS1.SSS5)

> …only requires 25% of the compute budget of the original dense model to catch up

> …after 500B tokens


<a id="sparse-upcycle"></a>

## sparse-upcycle

[Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints](https://arxiv.org/abs/2212.05055)

Aran Komatsuzaki, Joan Puigcerver, James Lee-Thorp et al. · 2022 · arXiv:2212.05055

[§4.2.1 Core results](https://arxiv.org/html/2212.05055#S4.SS2.SSS1)

> …requires about 120% of the original dense checkpoint's computation budget to catch up


<a id="expup-copy"></a>

## expup-copy

Expert Upcycling, 2026, arXiv:2604.19835, Definition 3.1

"copy the parameters of expert e exactly r\_e times", "Copy the router weight vector of source expert e to each of its r\_e replicas"; Table 3: the 10-layer interleaved MoE grows from 32 to 64 experts, top-2.


<a id="kexaone-grow"></a>

## kexaone-grow

LG AI Research, 2026, *K-EXAONE 2.0 Technical Report*, arXiv:2608.04505, §2.2

width up-scaling "128 → 256 experts"; "Each expert is duplicated together with its router row", and "Duplication alone leaves the two copies exactly tied", so "we therefore add a random rotation noise to the duplicated experts".


<a id="expup-drop"></a>

## expup-drop

Expert Upcycling, arXiv:2604.19835, App. D, Tables 9 and 11

Drop Upcycle, "Re-initialize a fraction of weight-matrix columns while keeping the remainder from the original expert", run at drop 0.3, 0.5 and 0.7 in the 32 to 64 growth (moderate, Xavier, drop 0.5: 2.77125 against 2.76858 for the copy).


<a id="dropup-r"></a>

## dropup-r

Nakamura et al., 2025, *Drop-Upcycling*, arXiv:2502.19261, §5

"a re-initialization ratio of 0.5 yielded the best results for both models" (8×152M and 8×1.5B, dense to MoE).


<a id="emo-init"></a>

## emo-init

EMO, 2026, arXiv:2605.13247, §3.3

"we use Gaussian initialization for new experts and router weights, and reset all router biases to zero"; L226: five stages, 8 → 16 → 32 → 64 → 128 experts.


<a id="dsv3-adamw"></a>

## dsv3-adamw

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

§4.2

> We employ the AdamW optimizer ... with hyper-parameters set to β1 \= 0.9, β2 \= 0.95, and weight\_decay \= 0.1


<a id="dsv4-muon"></a>

## dsv4-muon

[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)

DeepSeek-AI, Anyi Xu, Bangcai Lin et al. · 2026 · arXiv:2606.19348

[§2.4 Muon Optimizer, Basic Configurations](https://arxiv.org/html/2606.19348#S2.SS4.SSS0.Px1)

> For MoE parameters, we optimize each expert independently

> We maintain the AdamW optimizer for the embedding module, the prediction head module, the static biases and gating factors of mHC modules, and the weights of all RMSNorm modules. All other modules are updated with Muon


<a id="moonlight-t4"></a>

## moonlight-t4

[Muon is Scalable for LLM Training](https://arxiv.org/abs/2502.16982)

Jingyuan Liu, Jianlin Su, Xingcheng Yao et al. · 2025 · arXiv:2502.16982

[§3.3 Pretraining with Muon, Performance](https://arxiv.org/html/2502.16982#S3.T4)

Table 4: Comparison of different models at around 1.2T tokens.

> Comparison of different models at around 1.2T tokens

> Moonlight performs significantly better than Moonlight-A


<a id="qwen38-router"></a>

## qwen38-router

[On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability](https://arxiv.org/abs/2608.30320)

Zihan Qiu, Zekun Wang, Xiao Li et al. · 2026 · arXiv:2608.30320

[§3.1 Optimizer](https://arxiv.org/html/2608.30320#S3.SS1)

> For the MoE router, we observe that Muon exacerbates early-training fluctuations and destabilizes the router ... Therefore, we use AdamW for the router.


<a id="symcompat-router"></a>

## symcompat-router

[Symmetry-Compatible Principle for Optimizer Design: Embeddings, LM Heads, SwiGLU MLPs, and MoE Routers](https://arxiv.org/abs/2605.18106)

Tim Tsz-Kit Lau, Weijie Su · 2026 · arXiv:2605.18106

[§4.3 OLMoE-1B-7B-Style Pre-Training](https://arxiv.org/html/2605.18106#S4.SS3)


<a id="laguna-collapse"></a>

## laguna-collapse

[Laguna M.1/XS.2 Technical Report](https://arxiv.org/abs/2605.27605)

Julien Abadji, Marah Abdin, Connor Adams et al. · 2026 · arXiv:2605.27605

> Expert Collapse

> Muon without this rescaling and with standard weight decay coefficients caused expert collapse beginning at around 450B tokens into training and propagating layer-by-layer through the first three MoE layers until the training diverged


<a id="mellum2-muon"></a>

## mellum2-muon

[Mellum2 Technical Report](https://arxiv.org/abs/2605.31268)

Marko Kojic, Ivan Bondyrev, Aral de Moor et al. · 2026 · arXiv:2605.31268

[§3.4.1 Optimizer](https://arxiv.org/html/2605.31268#S3.SS4.SSS1)

> Megatron defaults (extra scale factor 1.0) and the Moonlight setup (extra scale factor 0.2)

> On the dense 7B architecture ... Megatron defaults caused immediate divergence ... We selected the Moonlight configuration


<a id="dsv3-mtp"></a>

## dsv3-mtp

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§2.2 Multi-Token Prediction, MTP Training Objective](https://arxiv.org/html/2412.19437#S2.SS2.SSS0.Px2)

> …an additional training objective

> …consistently enhances the model performance on most of the evaluation benchmarks


<a id="mellum2-mtp"></a>

## mellum2-mtp

[Mellum2 Technical Report](https://arxiv.org/abs/2605.31268)

Marko Kojic, Ivan Bondyrev, Aral de Moor et al. · 2026 · arXiv:2605.31268

[§2.1.5 Multi-Token Prediction](https://arxiv.org/html/2605.31268#S2.SS1.SSS5)

> In ablation studies involving a 14B MoE model trained on 105B data tokens, MTP yielded significant benchmark improvements at a cost of only 7% additional training time.

> …is trained with a scaled loss (α\=0.1)


<a id="ling2-mtp"></a>

## ling2-mtp

[Every Activation Boosted: Scaling General Reasoner to 1 Trillion Open Language Foundation](https://arxiv.org/abs/2510.22115)

Ling Team, Ang Li, Ben Liu et al. · 2025 · arXiv:2510.22115

[§5.2 Heterogeneous Fine-grained Pipeline Parallelism](https://arxiv.org/html/2510.22115#S5.SS2)

> …the computation cost of a MTP layer is approximately 1.7x that of a standard MoE layer. Based on this observation, we progressively refined the PP partition strategy, ultimately achieving a 40% relative end-to-end improvement


<a id="dsv3-mtp-lambda"></a>

## dsv3-mtp-lambda

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§4.2 Hyper-Parameters, Training Hyper-Parameters](https://arxiv.org/html/2412.19437#S4.SS2.SSS0.Px2)

> The MTP loss weight λ is set to 0.3 for the first 10T tokens, and to 0.1 for the remaining 4.8T tokens.


<a id="qwen38-spike"></a>

## qwen38-spike

[On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability](https://arxiv.org/abs/2608.30320)

Zihan Qiu, Zekun Wang, Xiao Li et al. · 2026 · arXiv:2608.30320

> …no run exhibits a single step where the loss exceeds its local median by more than 0.1


<a id="systems-dsv3"></a>

## systems-dsv3

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§2.1.2 DeepSeekMoE with Auxiliary-Loss-Free Load Balancing](https://arxiv.org/html/2412.19437#S2.SS1.SSS2)


<a id="systems-dsv4"></a>

## systems-dsv4

[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)

DeepSeek-AI, Anyi Xu, Bangcai Lin et al. · 2026 · arXiv:2606.19348

[§2.1 Designs Inherited from DeepSeek-V3](https://arxiv.org/html/2606.19348#S2.SS1)


<a id="systems-k3"></a>

## systems-k3

[Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

Kimi Team, Tongtong Bai, Yifan Bai et al. · 2026 · arXiv:2607.24653

distributed optimizer discussion


<a id="hub-kimi-k3-route"></a>

## hub-kimi-k3-route

Kimi K3's repo code, [`modeling_kimi_linear.py#L724`](https://huggingface.co/moonshotai/Kimi-K3/blob/f831ab66814297da540d832a5235f8e904f29d06/modeling_kimi_linear.py#L724)

The gate never reads the config's `use_grouped_topk: true`.


<a id="systems-longcat"></a>

## systems-longcat

[LongCat-Flash Technical Report](https://arxiv.org/abs/2509.01322)

Meituan LongCat Team, Bayan, Bei Li et al. · 2025 · arXiv:2509.01322

[§3.4 Long Context Extension](https://arxiv.org/html/2509.01322#S3.SS4)


<a id="mcore-s437"></a>

## mcore-s437

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§4.3.7 Full CUDA Graphs Coverage for Dropless MoE via Sync-Free Kernels, ECHO, and Paged Stashing](https://arxiv.org/html/2603.07685#S4.SS3.SSS7)

> EP ranks hosting hot experts become compute bottlenecks, causing other ranks to wait at synchronization points


<a id="dsv3-dualpipe"></a>

## dsv3-dualpipe

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§3.2.1 DualPipe and Computation-Communication Overlap](https://arxiv.org/html/2412.19437#S3.SS2.SSS1)

> The key idea of DualPipe is to overlap the computation and communication within a pair of individual forward and backward chunks

> …both all-to-all and PP communication can be fully hidden


<a id="mcore-fgo-doc"></a>

## mcore-fgo-doc

[Megatron-LM PR #1913, feat(moe): Fine-grained activation offloading](https://github.com/NVIDIA/Megatron-LM/pull/1913)

NVIDIA · GitHub

Megatron-LM `docs/user-guide/features/fine_grained_activation_offloading.md` at d6316eb45 (added in PR #1913, b97184db5; later commits add CUDA graph capture #3697, the fused grouped MLP module…

> Contributed in collaboration with RedNote

> Combining with Fine-Grained Recomputation


<a id="mcore-fgo-pr1913"></a>

## mcore-fgo-pr1913

[Megatron-LM PR #1913, feat(moe): Fine-grained activation offloading](https://github.com/NVIDIA/Megatron-LM/pull/1913)

NVIDIA · GitHub

NVIDIA/Megatron-LM PR #1913, "feat(moe): Fine-grained activation offloading", Benchmark section

> …feat(moe): Fine-grained activation offloading


<a id="mcore-paged-stash"></a>

## mcore-paged-stash

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§4.3.7 Full CUDA Graphs Coverage for Dropless MoE via Sync-Free Kernels, ECHO, and Paged Stashing](https://arxiv.org/html/2603.07685#S4.F28)

Figure 28: Memory layout comparison across three execution modes.

> …and Figure 28: CUDA graph buffers

> …buffers in all layers are allocated according to the worst-case size


<a id="dsv3-s212"></a>

## dsv3-s212

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§2.1.2 DeepSeekMoE with Auxiliary-Loss-Free Load Balancing](https://arxiv.org/html/2412.19437#S2.SS1.SSS2)

> …each token will be sent to at most M nodes, which are selected according to the sum of the highest K\_r/M affinity scores

> …at most 4 nodes


<a id="pangu-pro-moge"></a>

## pangu-pro-moge

[Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity](https://arxiv.org/abs/2505.21411)

Yehui Tang, Xiaosong Li, Fangcheng Liu et al. · 2025 · arXiv:2505.21411

[§1 Introduction](https://arxiv.org/html/2505.21411#S1)

> …we divide the experts into equal groups and then choose experts from each of the groups. Each group has an identical number of activated experts

> …the experts are assigned to the devices according to the group ID


<a id="interns1pro-s21"></a>

## interns1pro-s21

Intern-S1-Pro, 2026, *Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale*, arXiv:2603.25040, §2.1 Group Routing

"Combined with the configuration of the Intern s1-pro 1T model ($k\=8$) and the EP8 training strategy, we can divide all experts into 8 groups and select the Top-1 expert within each group"; Hub `internlm/Intern-S1-Pro` config.json `router_n_groups 8`, `num_experts 512`, `num_experts_per_tok 8`, `modeling_interns1_pro.py` L367-L380 (top `top_k // router_n_groups` per group).


<a id="dsv3-s322"></a>

## dsv3-s322

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§3.2.2 Efficient Implementation of Cross-Node All-to-All Communication](https://arxiv.org/html/2412.19437#S3.SS2.SSS2)

> …will first be transmitted via IB to the GPUs with the same in-node index on its target nodes

> …forwarded via NVLink to specific GPUs that host their target experts


<a id="deepep-readme"></a>

## deepep-readme

DeepSeek-AI, DeepEP README at tag v1.2.1

"To align with the group-limited gating algorithm proposed in the DeepSeek-V3 paper, DeepEP offers a set of kernels optimized for asymmetric-domain bandwidth forwarding, such as forwarding data from NVLink domain to RDMA domain."


<a id="terrace-t8"></a>

## terrace-t8

[TerraceMoE: A Cost Model for Hierarchical MoE All-to-All Communication](https://arxiv.org/abs/2608.27874)

Weicheng Xue, Bingqiang Wang, Li Yuan et al. · 2026 · arXiv:2608.27874

[Table 8](https://arxiv.org/html/2608.27874#S7.T8)

Quality cost of the routing constraints at the 20k-step readpoint.


<a id="pangu-s32"></a>

## pangu-s32

[Pangu Ultra MoE: How to Train Your Big MoE on Ascend NPUs](https://arxiv.org/abs/2505.04519)

Yehui Tang, Yichun Yin, Yaoyuan Wang et al. · 2025 · arXiv:2505.04519

[§3.2 Drop-and-Pad vs Dropless](https://arxiv.org/html/2505.04519#S3.F6)

Figure 6: Training loss curves for the 20B MoE models trained with drop-and-pad and dropless methods.

> …is effective in improving training speed by bounding the peak computational load on individual experts

> …the dropless method consistently exhibits lower loss


<a id="stmoe-cf-mem"></a>

## stmoe-cf-mem

[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906)

Barret Zoph, Irwan Bello, Sameer Kumar et al. · 2022 · arXiv:2202.08906

[§5.2 Choosing the Capacity Factor and Routing Algorithm](https://arxiv.org/html/2202.08906#S5.SS2)

> Increasing the capacity factor linearly increases the einsums costs, memory for activations, all2all communication costs


<a id="vavre-t2"></a>

## vavre-t2

[Llama 3 Meets MoE: Efficient Upcycling](https://arxiv.org/abs/2412.09952)

Aditya Vavre, Ethan He, Dennis Liu et al. · 2024 · arXiv:2412.09952

[§3.2 Training Framework](https://arxiv.org/html/2412.09952#S3.T2)

Table 2: Training performance for different configurations.

> …capacity factor 1 has better MFU than dropless training, since they can prevent the load imbalance issue and have less memory footprint to enable smaller model parallelism


<a id="ultraep-f11"></a>

## ultraep-f11

Wei et al., 2026, *UltraEP*, arXiv:2606.04101, §8.2 and Fig. 11 (training, resumed at global batch 3,500 for 20 more)

average per-rank max/mean imbalance "averaged across all layers and batches" (§8.1) for Megatron-LM against UltraEP, 2.23 against 1.02 on GLM4.5-106B-A12B, 2.86 against 1.03 on Qwen3-235B-A22B, 1.30 against 1.01 on DeepSeek-V3-671B-A37B; UltraEP "rebalances every microbatch and layer" (abstract). The abstract's 1.30 to 4.01 also counts serving prefill.


<a id="mcore-echo"></a>

## mcore-echo

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§4.3.7 Full CUDA Graphs Coverage for Dropless MoE via Sync-Free Kernels, ECHO, and Paged Stashing](https://arxiv.org/html/2603.07685#S4.SS3.SSS7)

> …much more expensive than for inference: each cloned expert requires weight communication during forward and gradient reduction during backward

> …with minimal cloning overhead


<a id="dsv3-redundant"></a>

## dsv3-redundant

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§3.4.1 Prefilling](https://arxiv.org/html/2412.19437#S3.SS4.SSS1)

> …based on statistics collected during the online deployment and are adjusted periodically (e.g., every 10 minutes)


<a id="megablocks-f2"></a>

## megablocks-f2

[MegaBlocks: Efficient Sparse Training with Mixture-of-Experts](https://arxiv.org/abs/2211.15841)

Trevor Gale, Deepak Narayanan, Cliff Young et al. · 2022 · arXiv:2211.15841

[§2.1 Routing](https://arxiv.org/html/2211.15841#S2.F2)

Figure 2: MoEs Trained on The Pile with Different Capacity Factors.

> …the loss reached by the MoE models decreases significantly as expert capacity is increased


<a id="vavre-t4"></a>

## vavre-t4

[Llama 3 Meets MoE: Efficient Upcycling](https://arxiv.org/abs/2412.09952)

Aditya Vavre, Ethan He, Dennis Liu et al. · 2024 · arXiv:2412.09952

[§5.1 Choice of Capacity Factor](https://arxiv.org/html/2412.09952#S5.T4)

Table 4: Model Flops Utilization (MFU) and MMLU accuracy of Llama 3-8B base model continued training (CT) vs upcycled Llama 3-8B E8T2 model with different capacity factors (CF).

> …a lack of regularization that is introduced implicitly by the CF


<a id="mobilemoe-sft"></a>

## mobilemoe-sft

[MobileMoE: Scaling On-Device Mixture of Experts](https://arxiv.org/abs/2605.27358)

Yanbei Chen, Hanxian Huang, Ernie Chang et al. · 2026 · arXiv:2605.27358

[§3.4 Scaling MobileMoE with Full Training Recipe](https://arxiv.org/html/2605.27358#S3.SS4)

> …would discard tokens from structured instruction-response pairs, distorting the learning signal and degrading SFT quality


<a id="stmoe-t8"></a>

## stmoe-t8

[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906)

Barret Zoph, Irwan Bello, Sameer Kumar et al. · 2022 · arXiv:2202.08906

[Table 8](https://arxiv.org/html/2202.08906#S5.T8)

Comparing capacity factors (CF) and routing algorithms.


<a id="dsv2-s224"></a>

## dsv2-s224

[DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2405.04434

[§2.2.4 Token-Dropping Strategy](https://arxiv.org/html/2405.04434#S2.SS2.SSS4)

> …tokens belonging to approximately 10% of the training sequences will never be dropped. In this way, we can flexibly decide whether to drop tokens during inference according to the efficiency requirements, and always ensure consistency between training and inference.


<a id="mcore-fp8-why"></a>

## mcore-fp8-why

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§4.3.5 Reduced-Precision Training: Low-Precision Acceleration](https://arxiv.org/html/2603.07685#S4.SS3.SSS5)

> …often memory-bandwidth bound

> …by reducing data movement and using faster FP8/FP4 Tensor Core operations on Hopper and Blackwell GPUs


<a id="mcore-fp8-e2e"></a>

## mcore-fp8-e2e

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§4.3.5 Reduced-Precision Training: Low-Precision Acceleration](https://arxiv.org/html/2603.07685#S4.SS3.SSS5)

> FP8 training achieves approximately 10% to 25% end-to-end performance improvement for large-scale MoE training on different hardware platforms


<a id="dsv3-fp8"></a>

## dsv3-fp8

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§3.3.1 Mixed Precision Framework](https://arxiv.org/html/2412.19437#S3.SS3.SSS1)

> …are executed in FP8

> …the embedding module, the output head, MoE gating modules, normalization operators, and attention operators


<a id="mcore-fp8-mem"></a>

## mcore-fp8-mem

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§5.2.1 Breaking the Memory Wall with Reduced-Precision Training](https://arxiv.org/html/2603.07685#S5.SS2.SSS1)

> FP8 saves approximately 16 GB of activation memory per GPU for DeepSeek-V3


<a id="mcore-s51"></a>

## mcore-s51

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§5.1 Why Reduced-Precision Training Matters for MoE](https://arxiv.org/html/2603.07685#S5.SS1)

> Router decisions depend on precise scores

> …could destabilize expert selection


<a id="dsv3-fp8-tiles"></a>

## dsv3-fp8-tiles

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§3.3.2 Improved Precision from Quantization and Multiplication](https://arxiv.org/html/2412.19437#S3.SS3.SSS2)

> …makes low-precision training highly sensitive to activation outliers


<a id="ling-fp8"></a>

## ling-fp8

[Every Activation Boosted: Scaling General Reasoner to 1 Trillion Open Language Foundation](https://arxiv.org/abs/2510.22115)

Ling Team, Ang Li, Ben Liu et al. · 2025 · arXiv:2510.22115

[§5.1 FP8 Training](https://arxiv.org/html/2510.22115#S5.SS1)

> …with a relative loss difference within 0.25% (averaging around 0.1%) compared to the BF16 baseline

> \+15% MFU improvement over BF16 training


<a id="mcore-fp8-recipes"></a>

## mcore-fp8-recipes

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§5.3.2 Blockwise FP8 on Hopper](https://arxiv.org/html/2603.07685#S5.SS3.SSS2)

> …the recommended FP8 recipe on the Hopper platform


<a id="dsv3-fp8-comm"></a>

## dsv3-fp8-comm

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[§3.3.3 Low-Precision Storage and Communication](https://arxiv.org/html/2412.19437#S3.SS3.SSS3)

> …compatible with FP8 Fprop in MoE up-projections

> A similar strategy is applied to the activation gradient before MoE down-projections. For both the forward and backward combine components, we retain them in BF16 to preserve training precision in critical parts of the training pipeline.


<a id="dsv3-fp8-val"></a>

## dsv3-fp8-val

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

DeepSeek-AI, Aixin Liu, Bei Feng et al. · 2024 · arXiv:2412.19437

[Appendix B Ablation Studies for Low-Precision Training](https://arxiv.org/html/2412.19437#A2)


<a id="nemotron3s-nvfp4"></a>

## nemotron3s-nvfp4

[Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2604.12374)

NVIDIA, Aakshita Chandiramani, Aaron Blakeman et al. · 2026 · arXiv:2604.12374

[§2 Pretraining](https://arxiv.org/html/2604.12374#S2.T3)

Table 3: Precision by Layer Type


<a id="nemotron3u-nvfp4"></a>

## nemotron3u-nvfp4

[Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2606.15007)

NVIDIA, Aaron Blakeman, Aaron Thomas et al. · 2026 · arXiv:2606.15007

[§2.2 NVFP4 Pretraining](https://arxiv.org/html/2606.15007#S2.SS2)

> …below 0.4% on average


<a id="mcore-fp4-mem"></a>

## mcore-fp4-mem

[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

Zijie Yan, Hongxiao Bai, Xin Yao et al. · 2026 · arXiv:2603.07685

[§5.2.1 Breaking the Memory Wall with Reduced-Precision Training](https://arxiv.org/html/2603.07685#S5.SS2.SSS1)

> …in FP8/FP4 instead of BF16, the memory footprint is reduced by 50%/75%


<a id="nvfp4-hw"></a>

## nvfp4-hw

[Pretraining Large Language Models with NVFP4](https://arxiv.org/abs/2509.25149)

NVIDIA, Felix Abecassis, Anjulie Agrusa et al. · 2025 · arXiv:2509.25149


<a id="fp4-hopper"></a>

## fp4-hopper

[Practical FP4 Training for Large-Scale MoE Models on Hopper GPUs](https://arxiv.org/abs/2603.02731)

Wuyue Zhang, Chongdong Huang, Chunbo You et al. · 2026 · arXiv:2603.02731

[§1 Introduction](https://arxiv.org/html/2603.02731#S1)

> …software-emulated MXFP4 for MoE training on Hopper GPUs. At the 671B parameter scale, our method reduces peak activation memory by 14.8% (11.8 GB), improves throughput by 12.5% (from 1157 to 1302 tokens/GPU/s), and matches the convergence of strong FP8 baselines


<a id="nemotron3s-zeros"></a>

## nemotron3s-zeros

[Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2604.12374)

NVIDIA, Aakshita Chandiramani, Aaron Blakeman et al. · 2026 · arXiv:2604.12374

[Figure 6](https://arxiv.org/html/2604.12374#S2.F6)

Channel Magnitude Patterns in Weights of Expert Layers in Nemotron 3 Super.


<a id="kcut-cost"></a>

## kcut-cost

[Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/abs/2609.04575)

Xing Chen, Hengshuai Yao · 2026 · arXiv:2609.04575

[Cost accounting.](https://arxiv.org/html/2609.04575#Sx7.SS0.SSS0.Px7)

> …a 17% end-to-end reduction against the \~3.0B parameters per token

> Memory is unchanged (all E experts stay resident)


<a id="lexi-gate"></a>

## lexi-gate

Chitty-Venkata, Madireddy, Emani and Vishwanath, 2025, *LExI: Layer-Adaptive Active Experts for Efficient MoE Model Inference*, arXiv:2509.02753

the gate is a softmax over the top-k logits, TopK selecting the experts and "Softmax normalizes their scores into a probability distribution", so the weights are renormalized over whatever k a layer is given.


<a id="kcut-t3"></a>

## kcut-t3

[Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/abs/2609.04575)

Xing Chen, Hengshuai Yao · 2026 · arXiv:2609.04575

Table 3

Cumulative router softmax mass by rank on Qwen3.6-35B-A3B, averaged over tokens and layers.


<a id="kcut-t5"></a>

## kcut-t5

[Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/abs/2609.04575)

Xing Chen, Hengshuai Yao · 2026 · arXiv:2609.04575

Table 5

MMLU, 5-shot, greedy, paired McNemar test against each model’s native baseline.


<a id="kcut-appa"></a>

## kcut-appa

[Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/abs/2609.04575)

Xing Chen, Hengshuai Yao · 2026 · arXiv:2609.04575

[Appendix A Appendix A: A Third Architecture](https://arxiv.org/html/2609.04575#A1)

> …whereas the identical intervention costs \+356% on Qwen

> A matched k1/k2 replication on this architecture remains future work


<a id="emoe-s32"></a>

## emoe-s32

[Elastic MoE: Unlocking the Inference-Time Scalability of Mixture-of-Experts](https://arxiv.org/abs/2509.21892)

Naibin Gu, Zhenyu Zhang, Yuchen Feng et al. · 2025 · arXiv:2509.21892

[§3.2 Findings and Analysis](https://arxiv.org/html/2509.21892#S3.SS2)

> …causes performance to degrade rapidly

> …stems from insufficient learning of diverse expert combinations during training


<a id="kcut-ppl"></a>

## kcut-ppl

[Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/abs/2609.04575)

Xing Chen, Hengshuai Yao · 2026 · arXiv:2609.04575

Table 4

Perplexity relative to the native baseline (absolute PPL in the native rows).

> Perplexity is minimized at k2 equal to the trained k on both models and all three corpora


<a id="gptoss-mxfp4"></a>

## gptoss-mxfp4

[gpt-oss-120b \& gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925)

OpenAI, Sandhini Agarwal, Lama Ahmad et al. · 2025 · arXiv:2508.10925

[§2.1 Quantization](https://arxiv.org/html/2508.10925#S2.SS1)

> We post-trained the models with quantization of the MoE weights to MXFP4 format, where weights are quantized to 4.25 bits per parameter. The MoE weights are responsible for 90\+% of the total parameter count

> …on a single 80GB GPU


<a id="dsv4-fp4qat"></a>

## dsv4-fp4qat

[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)

DeepSeek-AI, Anyi Xu, Bangcai Lin et al. · 2026 · arXiv:2606.19348

[§5.2.1 FP4 Quantization-Aware Training](https://arxiv.org/html/2606.19348#S5.SS2.SSS1)


<a id="glm5-int4"></a>

## glm5-int4

[GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763)

GLM-5-Team, Aohan Zeng, Xin Lv et al. · 2026 · arXiv:2602.15763

[§2.4.3 INT4 Quantization-aware training](https://arxiv.org/html/2602.15763#S2.SS4.SSS3)

> …we apply INT4 QAT in the SFT stage

> …standard Attention and MLP blocks use W8A8 (INT8), while the MoE experts are compressed to W4A8 (INT4)


<a id="lowbit-experts-cfg"></a>

## lowbit-experts-cfg

Hub config.json `quantization_config`, [`Zyphra/ZAYA1-8B-MXFP4-Experts`](https://huggingface.co/Zyphra/ZAYA1-8B-MXFP4-Experts/blob/d8602cda89e0f5f8ff268593778f4f27c8cbfe65/config.json)

(`mxfp4-pack-quantized`, group 32, `ignore: ["re:^(?!.*experts).*$"]`); [`moonshotai/Kimi-K2-Thinking`](https://huggingface.co/moonshotai/Kimi-K2-Thinking/blob/a51ccc050d73dab088bf7b0e2dd9b30ae85a4e55/config.json) (int, 4 bits, group 32; `ignore`: `lm_head`, `self_attn`, `shared_experts`, dense `mlp` projections); [`Qwen/Qwen3.5-35B-A3B-GPTQ-Int4`](https://huggingface.co/Qwen/Qwen3.5-35B-A3B-GPTQ-Int4/blob/3af5ca2972faf6de1fd6f4efc4d8d319ca751e8b/config.json) (gptq, 4 bits, group 128; `dynamic` excludes `lm_head`, `embed_tokens`, `.*attn.*`, `.*shared_expert.*`, `.*mtp.*`), the same in `Qwen/Qwen3.5-397B-A17B-GPTQ-Int4`.


<a id="lowbit-all-cfg"></a>

## lowbit-all-cfg

Hub config.json `quantization_config`, [`Qwen/Qwen3-30B-A3B-GPTQ-Int4`](https://huggingface.co/Qwen/Qwen3-30B-A3B-GPTQ-Int4/blob/9b534e4318b7ebc3c961a839f13eb18b1833f441/config.json)

and [`tencent/Hunyuan-A13B-Instruct-GPTQ-Int4`](https://huggingface.co/tencent/Hunyuan-A13B-Instruct-GPTQ-Int4/blob/835e6eb3eafc5bc9b00865592fd49cce5d0adce4/config.json): gptq, 4 bits, group 128, no `dynamic`, `modules_to_not_convert` or ignore list. Their safetensors headers hold `qweight` for attention and expert projections (Hunyuan also its shared MLP), while the router (`mlp.gate`, F16 in Qwen; `mlp.gate.wg`, F32 in Hunyuan), the embeddings and Qwen's `lm_head` stay unquantized.


<a id="deepinfer-qa-chunk"></a>

## deepinfer-qa-chunk

[DeepSeek V4.1 Flash Inference Deployment Q\&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md)

DeepSeek-AI · GitHub, deepseek-ai/DeepInfer

[DeepSeek-AI, *DeepSeek V4.1 Flash Inference Deployment Q\&A*, github.com/deepseek-ai/DeepInfer `doc/inference_deployment_qa.md` (commit 774ce244; Chinese PDF in 8b161497), "Prefill Load Balancer"](https://github.com/deepseek-ai/DeepInfer)

> Prefill Load Balancer

> …the largest that stays within the 32,768-token budget


<a id="deepinfer-qa-par"></a>

## deepinfer-qa-par

[DeepSeek V4.1 Flash Inference Deployment Q\&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md)

DeepSeek-AI · GitHub, deepseek-ai/DeepInfer

[DeepSeek-AI, *DeepSeek V4.1 Flash Inference Deployment Q\&A*, github.com/deepseek-ai/DeepInfer `doc/inference_deployment_qa.md` (commit 774ce244; Chinese PDF in 8b161497), "Inference system overview"](https://github.com/deepseek-ai/DeepInfer)

> Inference system overview

> Expert parallelism (EP) for the MoE part within a (super)node: increases batch size and GPU matrix-multiplication efficiency, and therefore throughput


<a id="deepinfer-qa-wideep"></a>

## deepinfer-qa-wideep

[DeepSeek V4.1 Flash Inference Deployment Q\&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md)

DeepSeek-AI · GitHub, deepseek-ai/DeepInfer

[DeepSeek-AI, *DeepSeek V4.1 Flash Inference Deployment Q\&A*, github.com/deepseek-ai/DeepInfer `doc/inference_deployment_qa.md` (commit 774ce244; Chinese PDF in 8b161497), chart `doc/images/wide_ep_decode_pareto.png`, "EP8 vs. EP64 benchmark data"](https://github.com/deepseek-ai/DeepInfer)

> EP8 vs. EP64 benchmark data


<a id="deepinfer-qa-unit"></a>

## deepinfer-qa-unit

[DeepSeek V4.1 Flash Inference Deployment Q\&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md)

DeepSeek-AI · GitHub, deepseek-ai/DeepInfer

[DeepSeek-AI, *DeepSeek V4.1 Flash Inference Deployment Q\&A*, github.com/deepseek-ai/DeepInfer `doc/inference_deployment_qa.md` (commit 774ce244; Chinese PDF in 8b161497), "How large does the smallest deployment unit have to be?"](https://github.com/deepseek-ai/DeepInfer)

> How large does the smallest deployment unit have to be?

> …the GPU ratio between P and D is roughly 1:1. Since the recommended decode configuration is EP64 or above, the smallest efficient deployment unit is 64 GPUs of prefill plus 64 GPUs of decode.


<a id="deepinfer-ft"></a>

## deepinfer-ft

[DeepSeek V4.1 Flash 大规模推理部署实践 (the DeepInfer release post)](https://zhuanlan.zhihu.com/p/2095560295930508953)

DeepSeek-AI · Zhihu

DeepSeek-AI, *DeepSeek V4.1 Flash 大规模推理部署实践*, [Zhihu](https://zhuanlan.zhihu.com/p/2095560295930508953), fault tolerance

> 大 EP 部署下，一个实例的全部卡构成单一通信域，任意一张卡故障即导致整个实例不可用


<a id="step3-s3"></a>

## step3-s3

[Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding](https://arxiv.org/abs/2507.19427)

StepFun, Bin Wang, Bojun Wang et al. · 2025 · arXiv:2507.19427

[§3 Attention-FFN Disaggregation](https://arxiv.org/html/2507.19427#S3)

> …one of the first production quality serving systems that leverages the Attention-FFN Disaggregation (AFD) idea

> …have a smaller number of parameters, but require storing the key-value cache


<a id="msi-abs"></a>

## msi-abs

[MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism](https://arxiv.org/abs/2504.02263)

Ruidong Zhu, Ziheng Jiang, Chao Jin et al. · 2025 · arXiv:2504.02263

> …attention and FFN modules within each model layer

> …up to 1.90× higher per-GPU throughput than state-of-the-art solutions


<a id="afd-ledger"></a>

## afd-ledger

[AFD-Ledger: Deployment Provisioning for Attention--FFN Disaggregation](https://arxiv.org/abs/2608.04502)

Chengyu Qiu, Xiao Fu, Fengcun Li et al. · 2026 · arXiv:2608.04502

> …homogeneous AFD improves fixed-budget throughput in only a minority of the studied settings

> …an offline analytical provisioning system


<a id="vllm-dbo"></a>

## vllm-dbo

vLLM at 790be385, [`vllm/config/parallel.py#L275-L276`](https://github.com/vllm-project/vllm/blob/790be385c8a69f45ec9a7a85ef00836d1684060f/vllm/config/parallel.py#L275-L276)

> Enable dual batch overlap for the model executor


<a id="step3-t8"></a>

## step3-t8

[Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding](https://arxiv.org/abs/2507.19427)

StepFun, Bin Wang, Bojun Wang et al. · 2025 · arXiv:2507.19427

[Table 8](https://arxiv.org/html/2507.19427#S7.T8)

Performance comparison with reported number of DSv3 under 20 tokens/s decoding SLA.

> …under 20 tokens/s decoding SLA


<a id="step3-s54"></a>

## step3-s54

[Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding](https://arxiv.org/abs/2507.19427)

StepFun, Bin Wang, Bojun Wang et al. · 2025 · arXiv:2507.19427

[§5.3 FFN’s Batch Requirement for High MFU](https://arxiv.org/html/2507.19427#S5.SS3)

> 8 experts are chosen from 256 plus one shared expert, then S \= 9/256

> Step-3 chooses a sparsity of around 0.08 (including shared expert)


<a id="step3-s55"></a>

## step3-s55

[Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding](https://arxiv.org/abs/2507.19427)

StepFun, Bin Wang, Bojun Wang et al. · 2025 · arXiv:2507.19427

[§5.5 Discussion: Workaround for Over-sparsity](https://arxiv.org/html/2507.19427#S5.SS5)

> MoE Routing Restrictions

> Step-3's design avoids this sparsity issue ... and eliminates the need for any routing restrictions


<a id="r3-engines"></a>

## r3-engines

[Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370)

Wenhan Ma, Hailin Zhang, Liang Zhao et al. · 2025 · arXiv:2510.11370

[§1 Introduction](https://arxiv.org/html/2510.11370#S1)

> SGLang ... for rollout and Megatron ... for training

> …can lead to divergent token probabilities


<a id="gspo-drift"></a>

## gspo-drift

[Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071)

Chujie Zheng, Shixuan Liu, Mingze Li et al. · 2025 · arXiv:2507.18071

[§5.3 Benefit of GSPO for MoE Training, Background](https://arxiv.org/html/2507.18071#S5.SS3.SSS0.Px1)

> …with the 48-layer Qwen3-30B-A3B-Base model, after each RL gradient update and for the same rollout sample, there are roughly 10% of the experts activated under the new policy πθ that are different from those under the old policy πθold


<a id="r3-mismatch"></a>

## r3-mismatch

[Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370)

Wenhan Ma, Hailin Zhang, Liang Zhao et al. · 2025 · arXiv:2510.11370

[§3.2 Routing Discrepancies between Training and Inference in MoE Models](https://arxiv.org/html/2510.11370#S3.SS2)

> …approximately 10% of the routers select different experts during training compared to inference


<a id="r3-kl"></a>

## r3-kl

[Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370)

Wenhan Ma, Hailin Zhang, Liang Zhao et al. · 2025 · arXiv:2510.11370

> …decrease from 1.5e-3 to 7.5e-4, which is near the 6.4e-4 observed for the dense model


<a id="v32-keep-routing"></a>

## v32-keep-routing

DeepSeek-AI, 2025, *DeepSeek-V3.2*, arXiv:2512.02556

"we preserve the expert routing paths used during sampling in the inference framework and enforce the same routing paths during training".


<a id="mimo-r3"></a>

## mimo-r3

Xiaomi, 2026, *MiMo-V2-Flash Technical Report*, arXiv:2601.02780

SGLang rollouts and a Megatron trainer, "Rollout Routing Replay (R3) ... to train RL using the same routed experts from rollout".


<a id="instella-r3"></a>

## instella-r3

[Instella-MoE Technical Report](https://arxiv.org/abs/2609.00791)

Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra et al. · 2026 · arXiv:2609.00791

> MoE-aware train/inference consistency

> …we enable Rollout Routing Replay (R3) ..., which fixes the expert-assignment decisions made during sampling by recording and replaying them inside the training forward pass


<a id="k25-mask"></a>

## k25-mask

Kimi Team, 2026, *Kimi K2.5: Visual Agentic Intelligence*, arXiv:2602.02276

a token-level clip "to mitigate the off-policy divergence amplified by discrepancies between training and inference frameworks", "gradients for tokens falling outside this range are zeroed out"; no routing replay in the full text (grep).


<a id="mellum2-icepop"></a>

## mellum2-icepop

[Mellum2 Technical Report](https://arxiv.org/abs/2605.31268)

Marko Kojic, Ivan Bondyrev, Aral de Moor et al. · 2026 · arXiv:2605.31268

> Train versus inference importance sampling

> …may dispatch a token to a different expert than the trainer-side router


<a id="r3-t1"></a>

## r3-t1

[Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370)

Wenhan Ma, Hailin Zhang, Liang Zhao et al. · 2025 · arXiv:2510.11370

[Table 1](https://arxiv.org/html/2510.11370#S5.T1)

Main evaluation results.


<a id="r3-gains"></a>

## r3-gains

[Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370)

Wenhan Ma, Hailin Zhang, Liang Zhao et al. · 2025 · arXiv:2510.11370

[§1 Introduction](https://arxiv.org/html/2510.11370#S1)

> …significant improvements in training stability and performance


<a id="qwen-rl-r3"></a>

## qwen-rl-r3

[Stabilizing Reinforcement Learning with LLMs: Formulation and Practices](https://arxiv.org/abs/2512.01374)

Chujie Zheng, Kai Dang, Bowen Yu et al. · 2025 · arXiv:2512.01374

[§4.3 Results of On-policy Training](https://arxiv.org/html/2512.01374#S4.SS3)

> Applying R3 in on-policy training does not yield performance gains


<a id="esrl-t1"></a>

## esrl-t1

[Expert-Space Exploration in MoE Reinforcement Learning](https://arxiv.org/abs/2609.13058)

Hongyi He, Zhenghao Lin, Xiao Liu et al. · 2026 · arXiv:2609.13058

[Table 1](https://arxiv.org/html/2609.13058#S4.T1)

Evaluation results on mathematical reasoning benchmarks.


<a id="r3-overhead"></a>

## r3-overhead

[Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370)

Wenhan Ma, Hailin Zhang, Liang Zhao et al. · 2025 · arXiv:2510.11370

[§4.1 Implementation](https://arxiv.org/html/2510.11370#S4.SS1)

> …an overall latency overhead below 3% during the rollout phase


<a id="gspo-replay"></a>

## gspo-replay

[Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071)

Chujie Zheng, Shixuan Liu, Mingze Li et al. · 2025 · arXiv:2507.18071

[§5.3 Benefit of GSPO for MoE Training, Benefit of GSPO](https://arxiv.org/html/2507.18071#S5.SS3.SSS0.Px3)

> …incurs additional memory and communication overhead and can also limit the actual capacity of the MoE model

> …eliminates the dependency on Routing Replay


<a id="trl-is"></a>

## trl-is

TRL, `trl/trainer/grpo_config.py` at 3749f2a, [`importance_sampling_level`](https://github.com/huggingface/trl/blob/3749f2a59fdcd3b6435243faa44eedf2903bc30e/trl/trainer/grpo_config.py#L208-L213)

"`\"sequence\"` averages the log-probability ratios across valid tokens to produce a single ratio per sequence", citing GSPO; default `"token"`; [`vllm_importance_sampling_correction`](https://github.com/huggingface/trl/blob/3749f2a59fdcd3b6435243faa44eedf2903bc30e/trl/trainer/grpo_config.py#L322-L341) (default `True`: "apply Importance Sampling (IS) to correct for the mismatch between vLLM completion logprobs and recomputed training logprobs"; default mode `"sequence_mask"`: "Sequences with ratios outside \[C\_min, C\_max\] are masked out"; C\_max default 3.0).


<a id="deepinfer-bi"></a>

## deepinfer-bi

[DeepInfer](https://github.com/deepseek-ai/DeepInfer)

DeepSeek-AI · GitHub

[DeepSeek-AI, DeepInfer README, github.com/deepseek-ai/DeepInfer (commit 9bd9cf24), "Feature details and configuration"](https://github.com/deepseek-ai/DeepInfer)

> Feature details and configuration

> Batch-invariant inference: keep model results identical across different batch compositions. Enable with (NVIDIA only)


<a id="step5-rl"></a>

## step5-rl

[Inside Step 5 Preview](https://platform.stepfun.ai/blog/inside-step-5-preview)

StepFun · blog

StepFun, *Inside Step 5 Preview* (technical blog, [platform.stepfun.ai/blog/inside-step-5-preview](https://platform.stepfun.ai/blog/inside-step-5-preview)), "Zero Training-Inference Mismatch"

> Zero Training-Inference Mismatch

> At we fully aligned the operators between training and inference: the difference is exactly zero


<a id="nemorl-freeze"></a>

## nemorl-freeze

NVIDIA NeMo-RL at fb121a00, [`examples/nemo_gym/nemotron-3-super/stage1_rlvr.yaml#L59-L61`](https://github.com/NVIDIA-NeMo/RL/blob/fb121a00d6b49cffd59e9e13e6c92215008b948e/examples/nemo_gym/nemotron-3-super/stage1_rlvr.yaml#L59-L61) (`async_grpo: enabled: true`, `max_trajectory_age_steps: 1`)

Megatron at d6316eb45: [`moe_utils.py#L936-L939`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/moe_utils.py#L936-L939) adds `expert_bias` to the scores for top-k selection only and gathers the weights from the unbiased scores; [`#L1258-L1262`](https://github.com/NVIDIA/Megatron-LM/blob/d6316eb45bf1bfbb6f1f848c0b56e55166564d80/megatron/core/transformer/moe/moe_utils.py#L1260-L1263) moves it each update by the sign of the load error times the rate.


<a id="quads"></a>

## quads

[QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810)

Zhengyang Zhuge, Hao Yu, Xin Wang et al. · 2026 · arXiv:2607.15810

> NVFP4 rollout with BF16 training collapses after roughly 150 steps

> …activation quantization, not weight quantization, is the dominant driver of log-probability divergence and reward collapse
