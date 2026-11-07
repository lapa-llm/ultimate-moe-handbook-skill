# latent-moe

[Interactive original](../upstream/app/public/viz/index.html?c=latent-moe) · [Poster](../upstream/app/public/viz/posters/latent-moe.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/latent-moe-g6vBsQ6X.js)

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

What does a smaller expert input buy you?

routed experts: width m, height input widthselected for one token

more expert combinations

dispatch per token:  
k × input width

expert combinations:  
C(N, k), log scale

Standard MoE

input width d, expert width m \= d/2; top-4 of 16

4d

1,820

LatentMoE (α \= 2\)

input width ℓ \= d/2, expert width m \= d/2; top-8 of 32

4d

10.5 million

Each tile is one expert, its width the intermediate size and its height the input size; dark tiles are selected for one token. Halving the input lets the latent layer hold and select twice as many experts at the same expert parameters, compute and dispatch, so a token chooses among far more expert combinations, at the cost of two extra projections.
