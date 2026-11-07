# all-to-all-overlap

[Interactive original](../upstream/app/public/viz/index.html?c=all-to-all-overlap) · [Poster](../upstream/app/public/viz/posters/all-to-all-overlap.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/all-to-all-overlap-CM-BD8Ws.js)

## Controls

```json
{}
```

Animation duration: 8.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Which block wiring overlaps the expert-parallel all-to-all with compute?

one MoE layer on one GPU
computeexposed all-to-alloverlapped all-to-all

exposed all-to-all / layer time

MoE block

router reads N(x \+ Attn(N(x))); Qwen3, gpt-oss, MiniMax M2

x

y

attention

MoE

compute

all-to-all

Parallel attention and MoE

router reads N(x), as attention does: y \= x \+ Attn(N(x)) \+ MoE(N(x)); North Mini Code, Moondream 3

x

y

\+

MoE

attention

compute

all-to-all

Shortcut-connected MoE

one MoE activating as many experts as two MoE blocks, as LongCat compares it; LongCat-Flash, ScMoE’s Pos-2

x

y

\+

MoE

attention 1

dense FFN 1

attention 2

dense FFN 2

compute

all-to-all

0

20

40

60

80

100

120

140

160

time

Compute runs on the top lane and the all-to-all below; any all-to-all that compute cannot cover is exposed.

## Sample 2

Parameters: `{"t": 4.25}`

Which block wiring overlaps the expert-parallel all-to-all with compute?

one MoE layer on one GPU
computeexposed all-to-alloverlapped all-to-all

exposed all-to-all / layer time

MoE block

router reads N(x \+ Attn(N(x))); Qwen3, gpt-oss, MiniMax M2

x

y

attention

MoE

compute

all-to-all

attention

router

dispatch

experts

combine

33%

32 of 96 time units

Parallel attention and MoE

router reads N(x), as attention does: y \= x \+ Attn(N(x)) \+ MoE(N(x)); North Mini Code, Moondream 3

x

y

\+

MoE

attention

compute

all-to-all

router

attention

dispatch

experts

combine

20%

16 of 80 time units

Shortcut-connected MoE

one MoE activating as many experts as two MoE blocks, as LongCat compares it; LongCat-Flash, ScMoE’s Pos-2

x

y

\+

MoE

attention 1

dense FFN 1

attention 2

dense FFN 2

compute

all-to-all

attention 1

router

dispatch

dispatch

dense FFN 1

0

20

40

60

80

100

120

140

160

time

The MoE block waits for attention before it can dispatch, and waits again on combine.

## Sample 3

Parameters: `{"t": 8.5}`

Which block wiring overlaps the expert-parallel all-to-all with compute?

one MoE layer on one GPU
computeexposed all-to-alloverlapped all-to-all

exposed all-to-all / layer time

MoE block

router reads N(x \+ Attn(N(x))); Qwen3, gpt-oss, MiniMax M2

x

y

attention

MoE

compute

all-to-all

attention

router

dispatch

experts

combine

33%

32 of 96 time units

Parallel attention and MoE

router reads N(x), as attention does: y \= x \+ Attn(N(x)) \+ MoE(N(x)); North Mini Code, Moondream 3

x

y

\+

MoE

attention

compute

all-to-all

router

attention

dispatch

experts

combine

20%

16 of 80 time units

Shortcut-connected MoE

one MoE activating as many experts as two MoE blocks, as LongCat compares it; LongCat-Flash, ScMoE’s Pos-2

x

y

\+

MoE

attention 1

dense FFN 1

attention 2

dense FFN 2

compute

all-to-all

attention 1

router

dispatch

dispatch

dense FFN 1

experts

combine

attention 2

dense FFN 2

0

20

40

60

80

100

120

140

160

time

7%

12 of 172 time units

LongCat-Flash measured

25.3% → 8.4% in training

at EP 32, 2 token chunks,

pipelined all-gather/reduce-scatter

The shortcut wiring hides combine too, because the sublayers after it do not read the MoE output, so the exposed share falls from 33% to 7%.

## Sample 4

Parameters: `{"t": 2.8}`

Which block wiring overlaps the expert-parallel all-to-all with compute?

one MoE layer on one GPU
computeexposed all-to-alloverlapped all-to-all

exposed all-to-all / layer time

MoE block

router reads N(x \+ Attn(N(x))); Qwen3, gpt-oss, MiniMax M2

x

y

attention

MoE

compute

all-to-all

attention

router

dispatch

experts

Parallel attention and MoE

router reads N(x), as attention does: y \= x \+ Attn(N(x)) \+ MoE(N(x)); North Mini Code, Moondream 3

x

y

\+

MoE

attention

compute

all-to-all

router

attention

dispatch

experts

combine

20%

16 of 80 time units

Shortcut-connected MoE

one MoE activating as many experts as two MoE blocks, as LongCat compares it; LongCat-Flash, ScMoE’s Pos-2

x

y

\+

MoE

attention 1

dense FFN 1

attention 2

dense FFN 2

compute

all-to-all

attention 1

router

dispatch

dispatch

dense FFN 1

0

20

40

60

80

100

120

140

160

time

In the parallel wiring the router reads the layer’s input, so dispatch hides behind attention, but combine stays exposed.
