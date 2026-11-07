# low-bit-experts

[Interactive original](../upstream/app/public/viz/index.html?c=low-bit-experts) · [Poster](../upstream/app/public/viz/posters/low-bit-experts.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/low-bit-experts-B85KoVIh.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 2,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Which weights to store in 4 bits: routed experts or every linear layer?

gpt-oss-20b, batch-1 decode: each token picks its own experts but reads the same number of bytes

width \= bytes, one scale for every bar

read for this tokennot read

Everything in bf16

16 bits per weight, as transformers loads gpt-oss without MXFP4 kernels

attention 0.64B params

embedding 0.58B params

unembedding 0.58B params

32 experts × 24 layers: 19.12B params (91%)

39.0 GiB in memory

6.72 GiB of weights read per token, 66% of it experts

Routed experts in 4 bits

experts in MXFP4 (4.25 bits), the rest in bf16: gpt-oss, Kimi K3, ZAYA1-8B (same scope, other bits: Kimi K2 Thinking, DeepSeek-V4, Qwen3.5-Int4)

12.8 GiB in memory

3.45 GiB of weights read per token, 34% of it experts

Every linear layer in 4 bits

attention in 4 bits too, embeddings in bf16: whole-model GPTQ-Int4 of Qwen3, Hunyuan-A13B (int4 g128, drawn at 4.25 bits)

11.9 GiB in memory

2.58 GiB of weights read per token, 46% of it experts

Blue marks the weights one token reads in batch-1 decode, its KV cache left out. MXFP4 experts shrink the model much more than a token’s reads, since the bf16 attention and unembedding become a large share of them; storing attention in 4 bits too cuts reads further.
