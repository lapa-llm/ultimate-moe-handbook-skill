# attention-ffn-disaggregation

[Interactive original](../upstream/app/public/viz/index.html?c=attention-ffn-disaggregation) · [Poster](../upstream/app/public/viz/posters/attention-ffn-disaggregation.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/attention-ffn-disaggregation-DFHsRzc6.js)

## Controls

```json
{}
```

Animation duration: 9.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Does attention-FFN disaggregation decode more per GPU than colocated EP?

What one GPU holds

186 GB of HBM per GPU

other weightsexpertsKV cacheactivations and headroom

colocated EP4, each GPU



57 GB experts, 101 GB KV: 64 requests

disaggregated, each of 28 attention GPUs



151 GB KV: 96 requests (1.5×)

disaggregated, each of 4 expert GPUs



57 GB experts, no requests

Requests per GPU

all 32 GPUs counted; dashed: per attention GPU

colocated

64

disaggregated

84 (dashed: 96\)

84 \= 28 × 96 / 32, 1.31× the colocated 64; × 1.07× faster step \= 1.40× throughput per GPU (measured 1.41×). The step ratio is AFD-Ledger’s model, which runs the colocated all-to-all after attention; the timeline draws it overlapped.

Who works when

first 3 of 94 layers of a decode step, each row on its own time axis; busy over all 94

attention and routerexpertsdispatch and combine

Colocated expert parallelism

each GPU runs attention and 1/4 of the experts; 2 micro-batches overlap the all-to-all (as vLLM's dual-batch overlap does)

every GPU

busy 100%

network

Disaggregated, one micro-batch

the pools alternate (MegaScale-Infer: going from 1 to 2 micro-batches gives 1.9×)

attention GPUs

busy 49%

network

expert GPUs

busy 40%

Disaggregated, 2 micro-batches (FastAFD, NVLink)

slower RDMA fabrics need 3 (MegaScale-Infer, Step-3)

attention GPUs

busy 98%

network

expert GPUs

busy 81%

Busy: the share of the step a pool spends computing. The timeline is our schedule of AFD-Ledger’s per-stage times, with network time our NVLink estimate.

Moving the experts off the attention GPUs leaves room for more cached requests, but the expert GPUs serve none.

Busy: the share of the step a pool spends computing. The timeline is our schedule of AFD-Ledger’s per-stage times, with network time our NVLink estimate.

## Sample 2

Parameters: `{"t": 4.75}`

Does attention-FFN disaggregation decode more per GPU than colocated EP?

What one GPU holds

186 GB of HBM per GPU

other weightsexpertsKV cacheactivations and headroom

colocated EP4, each GPU



57 GB experts, 101 GB KV: 64 requests

disaggregated, each of 28 attention GPUs



151 GB KV: 96 requests (1.5×)

disaggregated, each of 4 expert GPUs



57 GB experts, no requests

Requests per GPU

all 32 GPUs counted; dashed: per attention GPU

colocated

64

disaggregated

84 (dashed: 96\)

84 \= 28 × 96 / 32, 1.31× the colocated 64; × 1.07× faster step \= 1.40× throughput per GPU (measured 1.41×). The step ratio is AFD-Ledger’s model, which runs the colocated all-to-all after attention; the timeline draws it overlapped.

Who works when

first 3 of 94 layers of a decode step, each row on its own time axis; busy over all 94

attention and routerexpertsdispatch and combine

Colocated expert parallelism

each GPU runs attention and 1/4 of the experts; 2 micro-batches overlap the all-to-all (as vLLM's dual-batch overlap does)

every GPU



network

Disaggregated, one micro-batch

the pools alternate (MegaScale-Infer: going from 1 to 2 micro-batches gives 1.9×)

attention GPUs



network

expert GPUs

Disaggregated, 2 micro-batches (FastAFD, NVLink)

slower RDMA fabrics need 3 (MegaScale-Infer, Step-3)

attention GPUs



network

expert GPUs

Busy: the share of the step a pool spends computing. The timeline is our schedule of AFD-Ledger’s per-stage times, with network time our NVLink estimate.

With one micro-batch the separate pools take turns; with two they compute at the same time.

Busy: the share of the step a pool spends computing. The timeline is our schedule of AFD-Ledger’s per-stage times, with network time our NVLink estimate.

## Sample 3

Parameters: `{"t": 9.5}`

Does attention-FFN disaggregation decode more per GPU than colocated EP?

What one GPU holds

186 GB of HBM per GPU

other weightsexpertsKV cacheactivations and headroom

colocated EP4, each GPU



57 GB experts, 101 GB KV: 64 requests

disaggregated, each of 28 attention GPUs



151 GB KV: 96 requests (1.5×)

disaggregated, each of 4 expert GPUs



57 GB experts, no requests

Requests per GPU

all 32 GPUs counted; dashed: per attention GPU

colocated

64

disaggregated

84 (dashed: 96\)

84 \= 28 × 96 / 32, 1.31× the colocated 64; × 1.07× faster step \= 1.40× throughput per GPU (measured 1.41×). The step ratio is AFD-Ledger’s model, which runs the colocated all-to-all after attention; the timeline draws it overlapped.

Who works when

first 3 of 94 layers of a decode step, each row on its own time axis; busy over all 94

attention and routerexpertsdispatch and combine

Colocated expert parallelism

each GPU runs attention and 1/4 of the experts; 2 micro-batches overlap the all-to-all (as vLLM's dual-batch overlap does)

every GPU

busy 100%

network

Disaggregated, one micro-batch

the pools alternate (MegaScale-Infer: going from 1 to 2 micro-batches gives 1.9×)

attention GPUs

busy 49%

network

expert GPUs

busy 40%

Disaggregated, 2 micro-batches (FastAFD, NVLink)

slower RDMA fabrics need 3 (MegaScale-Infer, Step-3)

attention GPUs

busy 98%

network

expert GPUs

busy 81%

Busy: the share of the step a pool spends computing. The timeline is our schedule of AFD-Ledger’s per-stage times, with network time our NVLink estimate.

With two micro-batches, the expert GPUs’ slack covers most of the transfers, so attention stays busy almost the whole step and its extra cached requests become throughput.

Busy: the share of the step a pool spends computing. The timeline is our schedule of AFD-Ledger’s per-stage times, with network time our NVLink estimate.
