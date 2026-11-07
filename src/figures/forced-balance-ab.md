# forced-balance-ab

[Interactive original](../upstream/app/public/viz/index.html?c=forced-balance-ab) · [Poster](../upstream/app/public/viz/posters/forced-balance-ab.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/forced-balance-ab-BVz-PhjB.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How much throughput does uneven expert load cost?

median model TFLOP/s per GPU

Forced even

149.4 MaxVio \~0

Forced biased

131.4 MaxVio 2.6

117.5 MaxVio 5.0

107.1 MaxVio 6.8

100.5 MaxVio 7.0 −33% vs forced even

Learned router

99.2 first 40 iterations

The same MoE on one node, trained with forced even routing, with forced routing biased more and more toward a few experts, and with a learned router. Throughput falls as a few experts take more of the tokens, and a freshly initialised learned router ran its first iterations as slowly as the worst forced case. Each MaxVio, how far the busiest expert sits above the mean load, comes from replaying that run’s routing rule, since the runs saved no token counts.
