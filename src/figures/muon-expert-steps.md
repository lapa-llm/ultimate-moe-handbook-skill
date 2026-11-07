# muon-expert-steps

[Interactive original](../upstream/app/public/viz/index.html?c=muon-expert-steps) · [Poster](../upstream/app/public/viz/posters/muon-expert-steps.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/muon-expert-steps-D3TmndiW.js)

## Controls

```json
{}
```

Animation duration: 11.8 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Does Muon update a rarely routed expert as much as the busiest one?

each expert’s update RMS, relative to the busiest expert’s

balanced router

0.25

2

16

128

1,024

0

tokens this expert gets per step (log scale)

same as the busiest

half

no update

Muon per expert (DeepSeek-V4)

AdamW (DeepSeek-V3)

Muon over all experts as one matrix

16 tokens

0.61

0.17

Per-expert Muon ignores the gradient’s size, so a rarely routed expert keeps pace with busy ones: with far fewer tokens than the busiest it still gets the busiest’s step, while AdamW’s has shrunk as the gradient turns to noise.

## Sample 2

Parameters: `{"t": 5.9}`

Does Muon update a rarely routed expert as much as the busiest one?

each expert’s update RMS, relative to the busiest expert’s

balanced router

0.25

2

16

128

1,024

0

tokens this expert gets per step (log scale)

same as the busiest

half

no update

Muon per expert (DeepSeek-V4)

AdamW (DeepSeek-V3)

Muon over all experts as one matrix

1.3 tokens

0.68

0.35

0.06

Each token adds one direction to an expert’s gradient, and momentum keeps those of recent steps; with very few tokens per step they no longer fill the expert’s matrix, so per-expert Muon’s step shrinks too.

## Sample 3

Parameters: `{"t": 2.7}`

Does Muon update a rarely routed expert as much as the busiest one?

each expert’s update RMS, relative to the busiest expert’s

balanced router

0.25

2

16

128

1,024

0

tokens this expert gets per step (log scale)

same as the busiest

half

no update

Muon per expert (DeepSeek-V4)

AdamW (DeepSeek-V3)

Muon over all experts as one matrix

1,024 tokens

In the shaded band, where a balanced router keeps its experts, AdamW stays near the busiest’s step, while Muon over all experts as one matrix already shrinks each expert’s step with the size of its gradient.

## Sample 4

Parameters: `{"t": 5.5}`

Does Muon update a rarely routed expert as much as the busiest one?

each expert’s update RMS, relative to the busiest expert’s

balanced router

0.25

2

16

128

1,024

0

tokens this expert gets per step (log scale)

same as the busiest

half

no update

Muon per expert (DeepSeek-V4)

AdamW (DeepSeek-V3)

Muon over all experts as one matrix

3.6 tokens

0.97

0.44

0.11

Each token adds one direction to an expert’s gradient, and momentum keeps those of recent steps; with very few tokens per step they no longer fill the expert’s matrix, so per-expert Muon’s step shrinks too.

## Sample 5

Parameters: `{"t": 7.7}`

Does Muon update a rarely routed expert as much as the busiest one?

each expert’s update RMS, relative to the busiest expert’s

balanced router

0.25

2

16

128

1,024

0

tokens this expert gets per step (log scale)

same as the busiest

half

no update

Muon per expert (DeepSeek-V4)

AdamW (DeepSeek-V3)

Muon over all experts as one matrix

no tokens this step

0.32

0.23

0.01

With no tokens this step, the rarest expert still moves along the momentum of its past tokens, under AdamW and per-expert Muon alike; that momentum holds few directions, so even Muon’s step stays well below the busiest’s.

## Sample 6

Parameters: `{"t": 8.9}`

Does Muon update a rarely routed expert as much as the busiest one?

each expert’s update RMS, relative to the busiest expert’s

balanced router

0.25

2

16

128

1,024

0

tokens this expert gets per step (log scale)

same as the busiest

half

no update

Muon per expert (DeepSeek-V4)

AdamW (DeepSeek-V3)

Muon over all experts as one matrix



0.32

0.23

0.02

Per-expert Muon ignores the gradient’s size, so a rarely routed expert keeps pace with busy ones: with far fewer tokens than the busiest it still gets the busiest’s step, while AdamW’s has shrunk as the gradient turns to noise.
