# expert-granularity

[Interactive original](../upstream/app/public/viz/index.html?c=expert-granularity) · [Poster](../upstream/app/public/viz/posters/expert-granularity.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/expert-granularity-DUtO_tJE.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 4,
    "label": "seed",
    "hidden": true
  }
}
```

## Sample 1

Parameters: `{"t": 0}`

How fine-grained should experts be, at equal parameters and compute?

routed experts: width m, height input widthselected for one token

best in its column

dispatch per token:  
k × input width

expert combinations:  
C(N, k), log scale

Coarse-grained experts

m \= d, top-2 of 8; gpt-oss-120b (top-4 of 128\) and Trinity Large (top-4 of 256\) ship m \= d

2d

28

Fine-grained experts

each expert segmented in two: m \= d/2, top-4 of 16; Mistral Small 4 ships m \= d/2, top-4 of 128

4d

1,820

Finer-grained experts

segmented again: m \= d/4, top-8 of 32; Qwen3.5-35B-A3B ships m \= d/4, top-8 of 256

8d

10.5 million

Tile area is expert parameters and dark area one token’s expert compute. Splitting each expert into narrower ones while raising top-k keeps both fixed, raises dispatch per token and multiplies the expert combinations a token can select. Liew et al. trained this ladder in an 18-layer model with four times as many experts in each row: the loss fell down to the third row’s shape, then stopped improving with finer experts.
