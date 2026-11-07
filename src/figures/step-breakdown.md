# step-breakdown

[Interactive original](../upstream/app/public/viz/index.html?c=step-breakdown) · [Poster](../upstream/app/public/viz/posters/step-breakdown.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/step-breakdown-Cwd2YsKw.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Where does the time go in one MoE training step?

GPU time by kernel type in one traced step

summed kernel time, as a share of the traced step

all-to-all

50.5%

GEMMs

27.4%

other kernels

10.1%

permute, scatter, gather

6.6%

attention

3.8%

other communication

1.3%

traced step 19.97 s

Each bar is the share of one traced training step that one kind of kernel took: half the step is all-to-all with no compute overlapping it on the traced rank. The router was still unbalanced, so part of that may be ranks waiting for peers that received more tokens.
