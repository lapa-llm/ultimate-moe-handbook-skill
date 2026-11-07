# annotated-trace

[Interactive original](../upstream/app/public/viz/index.html?c=annotated-trace) · [Poster](../upstream/app/public/viz/posters/annotated-trace.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/annotated-trace-MLmhJdXg.js)

## Controls

```json
{
  "zoom": {
    "min": 0,
    "max": 2,
    "step": 1,
    "value": 0,
    "label": "zoomed layer: median, least, most all-to-all"
  }
}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

What does a profiler trace of one MoE training step show?

One traced step on rank 0: binned kernel occupancy

lane height: share of each bin of about 28 ms that the lane’s kernels occupy (dotted line: 100%)

all-to-all

GEMMs

permute and copy

everything else

50.5%

0

5

10

15

19.97 s

zoomed below

One Transformer layer’s forward pass, attention and MoE: kernel intervals

layer 16 of micro-batch 3, the pass at the median all-to-all share (59%) among layers 2 to 16

all-to-all

GEMMs

permute and copy

everything else

dispatch 6.9 ms

combine 11.2 ms

expert GEMMs 4.0 ms

0

10

20

30

40 ms

One traced training step of our MoE on one node: the all-to-all kernels (blue) recur through every layer of every micro-batch, in the forward, the recomputed forward and the backward, with no compute running on this rank during them. The router was still unbalanced at this step, so part of that time may be waiting for other ranks.

## Sample 2

Parameters: `{"t": 0, "zoom": 1}`

What does a profiler trace of one MoE training step show?

One traced step on rank 0: binned kernel occupancy

lane height: share of each bin of about 28 ms that the lane’s kernels occupy (dotted line: 100%)

all-to-all

GEMMs

permute and copy

everything else

50.5%

0

5

10

15

19.97 s

zoomed below

One Transformer layer’s forward pass, attention and MoE: kernel intervals

layer 6 of micro-batch 8, the pass with the lowest all-to-all share (37%) among layers 2 to 16

all-to-all

GEMMs

permute and copy

everything else

dispatch 6.0 ms

combine 5.1 ms

expert GEMMs 8.0 ms

0

10

20

30

40 ms

One traced training step of our MoE on one node: the all-to-all kernels (blue) recur through every layer of every micro-batch, in the forward, the recomputed forward and the backward, with no compute running on this rank during them. The router was still unbalanced at this step, so part of that time may be waiting for other ranks.

## Sample 3

Parameters: `{"t": 0, "zoom": 2}`

What does a profiler trace of one MoE training step show?

One traced step on rank 0: binned kernel occupancy

lane height: share of each bin of about 28 ms that the lane’s kernels occupy (dotted line: 100%)

all-to-all

GEMMs

permute and copy

everything else

50.5%

0

5

10

15

19.97 s

zoomed below

One Transformer layer’s forward pass, attention and MoE: kernel intervals

layer 13 of micro-batch 5, the pass with the highest all-to-all share (84%) among layers 2 to 16

all-to-all

GEMMs

permute and copy

everything else

dispatch 9.2 ms

combine 25.7 ms

expert GEMMs 0.09 ms

0

10

20

30

40 ms

One traced training step of our MoE on one node: the all-to-all kernels (blue) recur through every layer of every micro-batch, in the forward, the recomputed forward and the backward, with no compute running on this rank during them. The router was still unbalanced at this step, so part of that time may be waiting for other ranks.
