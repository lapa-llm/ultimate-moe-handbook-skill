# offload-recompute

[Interactive original](../upstream/app/public/viz/index.html?c=offload-recompute) · [Poster](../upstream/app/public/viz/posters/offload-recompute.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/offload-recompute-B3QjI8lR.js)

## Controls

```json
{
  "bw": {
    "min": 1,
    "max": 8,
    "step": 0.5,
    "value": 6,
    "label": "host link speed"
  }
}
```

Animation duration: 9.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How do recomputation and offloading trade memory for time?

three MoE layers, forward then backward
forwardbackwardrecomputecopy

Keep every saved input

layer 1

layer 2

layer 3

layer 3

layer 2

layer 1

compute

saved inputs on GPU

Full recompute

keep each layer’s input, rerun the layer’s forward before its backward

compute

saved inputs on GPU

Fine-grained recompute and offload

recompute the norms and the expert activation, offload the attention and expert inputs; fast host link

compute

to the CPU

back to the GPU

saved inputs on GPU

time

Forward: keeping every input fills memory layer by layer, full recompute keeps only each layer’s input, and the fine-grained split copies the large inputs to the CPU.

## Sample 2

Parameters: `{"t": 4.75}`

How do recomputation and offloading trade memory for time?

three MoE layers, forward then backward
forwardbackwardrecomputecopy

Keep every saved input

layer 1

layer 2

layer 3

layer 3

layer 2

layer 1

compute

saved inputs on GPU

Full recompute

keep each layer’s input, rerun the layer’s forward before its backward

compute

saved inputs on GPU

Fine-grained recompute and offload

recompute the norms and the expert activation, offload the attention and expert inputs; fast host link

compute

to the CPU

back to the GPU

saved inputs on GPU

time

Backward: full recompute runs each layer’s forward again, while the fine-grained split reloads its copies and recomputes only cheap modules.

## Sample 3

Parameters: `{"t": 9.5}`

How do recomputation and offloading trade memory for time?

three MoE layers, forward then backward
forwardbackwardrecomputecopy

Keep every saved input

layer 1

layer 2

layer 3

layer 3

layer 2

layer 1

compute

saved inputs on GPU

peak 100% of keeping all

Full recompute

keep each layer’s input, rerun the layer’s forward before its backward

compute

saved inputs on GPU

peak 36% of keeping all

Fine-grained recompute and offload

recompute the norms and the expert activation, offload the attention and expert inputs; fast host link

compute

to the CPU

back to the GPU

saved inputs on GPU

peak 48% of keeping all

time

Full recompute reaches the lowest peak but pays with a second forward pass; the fine-grained split holds more and pays in host-link copies, which cost no time only while they hide under compute.

## Sample 4

Parameters: `{"bw": 1, "t": 0}`

How do recomputation and offloading trade memory for time?

three MoE layers, forward then backward
forwardbackwardrecomputecopy

Keep every saved input

layer 1

layer 2

layer 3

layer 3

layer 2

layer 1

compute

saved inputs on GPU

Full recompute

keep each layer’s input, rerun the layer’s forward before its backward

compute

saved inputs on GPU

Fine-grained recompute and offload

recompute the norms and the expert activation, offload the attention and expert inputs; slow host link: the backward waits for its reloads

compute

to the CPU

back to the GPU

saved inputs on GPU

time

Forward: keeping every input fills memory layer by layer, full recompute keeps only each layer’s input, and the fine-grained split copies the large inputs to the CPU.
