# ep-placement

[Interactive original](../upstream/app/public/viz/index.html?c=ep-placement) · [Poster](../upstream/app/public/viz/posters/ep-placement.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/ep-placement-Bt6a2-Q1.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Expert parallelism: inside one node or across two?

one expert-parallel group

placement, 8 GPUs per node

median throughput, TFLOP/s per GPU, two unmatched runs

0

50

100

EP8 in one node

every all-to-all stays on NVLink

NVLink

102.5

EP16 across two nodes

part of every all-to-all crosses EFA between the nodes

NVLink

NVLink

EFA

42.0 , 59% below EP8

Each square is a GPU and each dark outline an expert-parallel group: inside one node every all-to-all stays on NVLink, across two nodes part of it goes over EFA. The cross-node run measured lower throughput, but the two runs differ in more than placement, so benchmark both on your cluster.
