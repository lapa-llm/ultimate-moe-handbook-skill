# combined-1f1b

[Interactive original](../upstream/app/public/viz/index.html?c=combined-1f1b) · [Poster](../upstream/app/public/viz/posters/combined-1f1b.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/combined-1f1b-Bl4O0Z3K.js)

## Controls

```json
{}
```

Animation duration: 8.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How does interleaving two micro-batches hide dispatch and combine?

one MoE layer on one GPU
computeexposed all-to-alloverlapped all-to-all→ forward of micro-batch 2← backward of micro-batch 1

One micro-batch at a time

the forward of micro-batch 2, then the backward of micro-batch 1

compute

all-to-all

Interleaved

the same work, with the all-to-alls on a separate stream (--overlap-moe-expert-parallel-comm --delay-wgrad-compute)

compute

all-to-all

time

Every all-to-all is drawn shorter than any compute block.

One micro-batch at a time: each all-to-all has to finish before the compute that needs it can start.

Every all-to-all is drawn shorter than any compute block.

## Sample 2

Parameters: `{"t": 4.25}`

How does interleaving two micro-batches hide dispatch and combine?

one MoE layer on one GPU
computeexposed all-to-alloverlapped all-to-all→ forward of micro-batch 2← backward of micro-batch 1

One micro-batch at a time

the forward of micro-batch 2, then the backward of micro-batch 1

compute

all-to-all

→ attention \+ router

→ dispatch

→ experts

→ combine

← combine

← experts

← weights

← dispatch

Interleaved

the same work, with the all-to-alls on a separate stream (--overlap-moe-expert-parallel-comm --delay-wgrad-compute)

compute

all-to-all

← combine

→ attention \+ router

← experts

→ dispatch

← weights

← dispatch

→ experts

→ combine

← attention \+ router

time

Every all-to-all is drawn shorter than any compute block.

One micro-batch at a time: each all-to-all has to finish before the compute that needs it can start.

Every all-to-all is drawn shorter than any compute block.

## Sample 3

Parameters: `{"t": 8.5}`

How does interleaving two micro-batches hide dispatch and combine?

one MoE layer on one GPU
computeexposed all-to-alloverlapped all-to-all→ forward of micro-batch 2← backward of micro-batch 1

One micro-batch at a time

the forward of micro-batch 2, then the backward of micro-batch 1

compute

all-to-all

→ attention \+ router

→ dispatch

→ experts

→ combine

← combine

← experts

← weights

← dispatch

← attention \+ router

← weights

Interleaved

the same work, with the all-to-alls on a separate stream (--overlap-moe-expert-parallel-comm --delay-wgrad-compute)

compute

all-to-all

← combine

→ attention \+ router

← experts

→ dispatch

← weights

← dispatch

→ experts

→ combine

← attention \+ router

← weights

time

Every all-to-all is drawn shorter than any compute block.

Both rows do the same work, so the shorter interleaved row is the all-to-all time the overlap takes off the step.

Every all-to-all is drawn shorter than any compute block.

## Sample 4

Parameters: `{"t": 4.5}`

How does interleaving two micro-batches hide dispatch and combine?

one MoE layer on one GPU
computeexposed all-to-alloverlapped all-to-all→ forward of micro-batch 2← backward of micro-batch 1

One micro-batch at a time

the forward of micro-batch 2, then the backward of micro-batch 1

compute

all-to-all

→ attention \+ router

→ dispatch

→ experts

→ combine

← combine

← experts

← weights

← dispatch

Interleaved

the same work, with the all-to-alls on a separate stream (--overlap-moe-expert-parallel-comm --delay-wgrad-compute)

compute

all-to-all

← combine

→ attention \+ router

← experts

→ dispatch

← weights

← dispatch

→ experts

→ combine

← attention \+ router

← weights

time

Every all-to-all is drawn shorter than any compute block.

Interleaved, the backward dispatch runs under its own delayed weight gradients, the other three under the other micro-batch.

Every all-to-all is drawn shorter than any compute block.
