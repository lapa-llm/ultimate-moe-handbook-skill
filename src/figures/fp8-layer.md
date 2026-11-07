# fp8-layer

[Interactive original](../upstream/app/public/viz/index.html?c=fp8-layer) · [Poster](../upstream/app/public/viz/posters/fp8-layer.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/fp8-layer-CltPtXVQ.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Where FP8 runs in an MoE layer

FP8 operandsBF16 or FP32MXFP8 on the wire, optional in Megatron

attention block

MoE block

forward

backward

norm

norm

QKV

QKV

attention

attention

out proj

out proj

norm

norm

router

router

dispatch

dispatch

fc1

fc1

activation

activation

fc2

fc2

combine

combine

Inside each FP8 linear layer

forward

input

×

weight

output

backward, input gradient

output gradient

×

weight

input gradient

backward, weight gradient

saved input

×

output gradient

weight gradient

master weights and optimizer

The attention and expert projections (blue) run their forward and backward matrix multiplications on FP8 inputs, while the norms, the attention core, the expert activation and the router stay in higher precision, following DeepSeek-V3’s FP8 recipe.
