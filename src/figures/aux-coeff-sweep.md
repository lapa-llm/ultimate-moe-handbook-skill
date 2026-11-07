# aux-coeff-sweep

[Interactive original](../upstream/app/public/viz/index.html?c=aux-coeff-sweep) · [Poster](../upstream/app/public/viz/posters/aux-coeff-sweep.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/aux-coeff-sweep-BI8vZUNr.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How does aux-loss strength trade expert balance for test loss?

test loss of Yuan3.0's 10B base model

1.66

1.68

1.70

no aux loss 1.661

0

63.3×

1e-4

1.656

13.6×

1e-3

1e-2

1.2×

1e-1

1.707

busiest expert’s tokens over the least used one’s (layer 3\)

auxiliary loss coefficient

Yuan3.0’s sweep of the sequence-wise auxiliary loss coefficient: the smallest coefficient slightly lowers the loss but leaves the expert load uneven, while a large one balances the load and raises the loss.
