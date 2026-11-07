# router-precision

[Interactive original](../upstream/app/public/viz/index.html?c=router-precision) · [Poster](../upstream/app/public/viz/posters/router-precision.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/router-precision-7pcACdMD.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 7,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 12 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Router precision: how often does bf16 rounding change the top-8?

each token’s gap between its 8th and 9th logits

can tie: gap under the bf16 spacingcannot

share of tokens whose top-8 differs from fp32

bf16 routerbatch mean logsumexp 4.6

logit \= bf16(W·x) (inference code of gpt-oss, and of Mixtral and Qwen3, whose fp32 softmax comes after the rounding)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

2%

training step

differs

none

bf16 router \+ z-lossbatch mean logsumexp 4.6

logit \= bf16(W·x), plus ST-MoE’s router z-loss 10⁻³·logsumexp(logit)² in the loss (OLMoE)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

2%

training step

differs

none

fp32 routerbatch mean logsumexp 4.6

logit \= fp32(W·x) (Switch in training; inference code of DeepSeek-V3.2, GLM-4.5, Kimi K2.5)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

\|logit\| of the 8th expert

fp32 spacing: 65,536× finer, below the axis

0%

training step

differs

none

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

Step 1 of 40\. Without z-loss, the logits’ shared offset grows each step, and bf16 rounds close logits ever more coarsely.

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

## Sample 2

Parameters: `{"t": 6}`

Router precision: how often does bf16 rounding change the top-8?

each token’s gap between its 8th and 9th logits

can tie: gap under the bf16 spacingcannot

share of tokens whose top-8 differs from fp32

bf16 routerbatch mean logsumexp 6.2

logit \= bf16(W·x) (inference code of gpt-oss, and of Mixtral and Qwen3, whose fp32 softmax comes after the rounding)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

4%

training step

differs

none

bf16 router \+ z-lossbatch mean logsumexp 1.4

logit \= bf16(W·x), plus ST-MoE’s router z-loss 10⁻³·logsumexp(logit)² in the loss (OLMoE)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

4%

training step

differs

none

fp32 routerbatch mean logsumexp 6.2

logit \= fp32(W·x) (Switch in training; inference code of DeepSeek-V3.2, GLM-4.5, Kimi K2.5)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

\|logit\| of the 8th expert

fp32 spacing: 65,536× finer, below the axis

0%

training step

differs

none

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

Step 25 of 40\. With z-loss the logits sink instead of rising: the 8th logit ends near −2.2 rather than \+3.6, both on the staircase step between 2 and 4 in size, so here as many top-8s differ from fp32; only the fp32 router has none.

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

## Sample 3

Parameters: `{"t": 12}`

Router precision: how often does bf16 rounding change the top-8?

each token’s gap between its 8th and 9th logits

can tie: gap under the bf16 spacingcannot

share of tokens whose top-8 differs from fp32

bf16 routerbatch mean logsumexp 7.1

logit \= bf16(W·x) (inference code of gpt-oss, and of Mixtral and Qwen3, whose fp32 softmax comes after the rounding)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

4%

training step

differs

none

bf16 router \+ z-lossbatch mean logsumexp 1.3

logit \= bf16(W·x), plus ST-MoE’s router z-loss 10⁻³·logsumexp(logit)² in the loss (OLMoE)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

4%

training step

differs

none

fp32 routerbatch mean logsumexp 7.1

logit \= fp32(W·x) (Switch in training; inference code of DeepSeek-V3.2, GLM-4.5, Kimi K2.5)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

\|logit\| of the 8th expert

fp32 spacing: 65,536× finer, below the axis

0%

training step

differs

none

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

Step 40 of 40\. With z-loss the logits sink instead of rising: the 8th logit ends near −2.2 rather than \+3.6, both on the staircase step between 2 and 4 in size, so here as many top-8s differ from fp32; only the fp32 router has none.

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Router precision: how often does bf16 rounding change the top-8?

each token’s gap between its 8th and 9th logits

can tie: gap under the bf16 spacingcannot

share of tokens whose top-8 differs from fp32

bf16 routerbatch mean logsumexp 4.7

logit \= bf16(W·x) (inference code of gpt-oss, and of Mixtral and Qwen3, whose fp32 softmax comes after the rounding)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

2%

training step

differs

none

bf16 router \+ z-lossbatch mean logsumexp 4.7

logit \= bf16(W·x), plus ST-MoE’s router z-loss 10⁻³·logsumexp(logit)² in the loss (OLMoE)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

2%

training step

differs

none

fp32 routerbatch mean logsumexp 4.7

logit \= fp32(W·x) (Switch in training; inference code of DeepSeek-V3.2, GLM-4.5, Kimi K2.5)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

\|logit\| of the 8th expert

fp32 spacing: 65,536× finer, below the axis

0%

training step

differs

none

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

Step 1 of 40\. Without z-loss, the logits’ shared offset grows each step, and bf16 rounds close logits ever more coarsely.

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Router precision: how often does bf16 rounding change the top-8?

each token’s gap between its 8th and 9th logits

can tie: gap under the bf16 spacingcannot

share of tokens whose top-8 differs from fp32

bf16 routerbatch mean logsumexp 4.6

logit \= bf16(W·x) (inference code of gpt-oss, and of Mixtral and Qwen3, whose fp32 softmax comes after the rounding)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

3%

training step

differs

none

bf16 router \+ z-lossbatch mean logsumexp 4.6

logit \= bf16(W·x), plus ST-MoE’s router z-loss 10⁻³·logsumexp(logit)² in the loss (OLMoE)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

3%

training step

differs

none

fp32 routerbatch mean logsumexp 4.6

logit \= fp32(W·x) (Switch in training; inference code of DeepSeek-V3.2, GLM-4.5, Kimi K2.5)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

\|logit\| of the 8th expert

fp32 spacing: 65,536× finer, below the axis

0%

training step

differs

none

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

Step 1 of 40\. Without z-loss, the logits’ shared offset grows each step, and bf16 rounds close logits ever more coarsely.

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

## Sample 6

Parameters: `{"t": 5.1}`

Router precision: how often does bf16 rounding change the top-8?

each token’s gap between its 8th and 9th logits

can tie: gap under the bf16 spacingcannot

share of tokens whose top-8 differs from fp32

bf16 routerbatch mean logsumexp 5.9

logit \= bf16(W·x) (inference code of gpt-oss, and of Mixtral and Qwen3, whose fp32 softmax comes after the rounding)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

5%

training step

differs

none

bf16 router \+ z-lossbatch mean logsumexp 1.4

logit \= bf16(W·x), plus ST-MoE’s router z-loss 10⁻³·logsumexp(logit)² in the loss (OLMoE)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

bf16 spacing

4%

training step

differs

none

fp32 routerbatch mean logsumexp 5.9

logit \= fp32(W·x) (Switch in training; inference code of DeepSeek-V3.2, GLM-4.5, Kimi K2.5)

1/4

1/2

1

2

4

8

1/4096

1/512

1/64

1/8

1

\|logit\| of the 8th expert

fp32 spacing: 65,536× finer, below the axis

0%

training step

differs

none

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.

Step 21 of 40\. With z-loss the logits sink instead of rising: the 8th logit ends near −2.2 rather than \+3.6, both on the staircase step between 2 and 4 in size, so here as many top-8s differ from fp32; only the fp32 router has none.

End logsumexp from ST-MoE’s decoder-layer router z-loss curves (7.1 without z-loss, 1.3 with); only the logits are rounded. At top-8 of 64, the 8th logit sits about 3.5 below the logsumexp, so both ends leave it on the same bf16 spacing.
