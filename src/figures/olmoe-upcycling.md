# olmoe-upcycling

[Interactive original](../upstream/app/public/viz/index.html?c=olmoe-upcycling) · [Poster](../upstream/app/public/viz/posters/olmoe-upcycling.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/olmoe-upcycling-CAVUymK8.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Upcycled vs from scratch: how long did OLMoE’s head start last?

upcycled from dense OLMo-1B after its 2T tokenstrained from scratch

Training loss, median per 2.1B tokens

2.3

2.4

2.5

0

200

400

600

authors’ catch-up estimate

Validation loss on C4

2.6

2.8

3.0

0

200

400

600

HellaSwag accuracy (%)

30

50

70

0

200

400

600

MMLU Var accuracy (%)

24

28

32

36

0

200

400

600

tokens since the MoE started (billions)

OLMoE’s upcycled MoE against the same MoE trained from scratch, redrawn from its training logs. The run from scratch starts behind on all four metrics and catches up gradually; the authors place the catch-up at the dashed line.
