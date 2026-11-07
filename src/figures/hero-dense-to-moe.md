# hero-dense-to-moe

[Interactive original](../upstream/app/public/viz/index.html?c=hero-dense-to-moe) · [Poster](../upstream/app/public/viz/posters/hero-dense-to-moe.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/hero-dense-to-moe-DHSLOS2p.js)

## Controls

```json
{
  "state": {
    "min": 1,
    "max": 5,
    "step": 1,
    "value": 5,
    "label": "Animation step",
    "wide": true,
    "hidden": true
  }
}
```

Animation duration: 23 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

What an MoE layer changes

each

token

picks

its

experts

FFN

Σ

output

Every token runs through the whole feed-forward block.

## Sample 2

Parameters: `{"t": 11.5}`

What an MoE layer changes

each

token

picks

its

experts

router

scores

top-8

64 experts

Σ

weighted sum

dense FFN width

output

Their outputs are summed, weighted by the kept scores renormalized to sum to one.

## Sample 3

Parameters: `{"t": 2}`

What an MoE layer changes

each

token

picks

its

experts

FFN

Σ

output

Many small experts take its place; together they hold many times the dense block's parameters.

## Sample 4

Parameters: `{"t": 6.8}`

What an MoE layer changes

each

token

picks

its

experts

64 experts

Σ

output

The router scores every expert for this token and keeps the best few.

## Sample 5

Parameters: `{"t": 15.6}`

What an MoE layer changes

each

token

picks

its

experts

router

scores

top-8

64 experts

Σ

weighted sum

dense FFN width

output

The next token picks its own set, yet each token runs only one dense block's worth of compute.

## Sample 6

Parameters: `{"t": 22}`

What an MoE layer changes

each

token

picks

its

experts

router

scores

top-8

ringed: picked by both tokens

64 experts

Σ

weighted sum

dense FFN width

output

Every token runs through the whole feed-forward block.
