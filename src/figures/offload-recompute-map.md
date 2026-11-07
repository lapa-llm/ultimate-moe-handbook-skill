# offload-recompute-map

[Interactive original](../upstream/app/public/viz/index.html?c=offload-recompute-map) · [Poster](../upstream/app/public/viz/posters/offload-recompute-map.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/offload-recompute-map-U5VmnW43.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Which saved tensor does each offload and recompute option act on?

--offload-modules value: copied to the CPU--recompute-modules value: discarded, then rebuilt

attention

MoE

layer input

attention norm

attn\_norm

QKV projection

qkv\_linear

layernorm

core attention

core\_attn

mla\_up\_proj

MLA

output projection

attn\_proj

with core\_attn

mlp\_norm

MoE norm

router and dispatch

layernorm

expert fc1

expert\_fc1

activation

moe\_act

expert fc2

moe\_act

combine

layer output

shared expert

shared\_experts

moe

whole MoE layer

fused\_group\_mlp

whole expert MLP

One MoE layer, each label on the tensor it acts on: recompute the cheap norms and expert activation, and offload the large inputs such as attention’s query, key and value. Adapted from the figure in Megatron-LM’s [fine-grained activation offloading guide](https://github.com/NVIDIA/Megatron-LM/blob/main/docs/user-guide/features/fine_grained_activation_offloading.md#combining-with-fine-grained-recomputation) (NVIDIA).
