# dense-layer-placement

[Interactive original](../upstream/app/public/viz/index.html?c=dense-layer-placement) · [Poster](../upstream/app/public/viz/posters/dense-layer-placement.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/dense-layer-placement-BYlDYMjn.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 4,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 13.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Where should an MoE model’s dense FFN layers go?

overload (MaxVio) per layer

worst MoE layer over training

all-to-alls per forward pass

MoE in every layer

every FFN is a routed MoE (Qwen3, gpt-oss, MiniMax M2, Llama 4 Scout)

layer 1

\+31%

layer 2

\+10%

layer 3

\+4%

layer 4

\+6%

layer 5

\+6%

layer 6

\+6%

layer 7

\+10%

layer 8

\+4%

training step



balanced

mean \+65%

\+31%, layer 1

16 \= 8 MoE layers × 2

Llama 4 Scout: 96 \= 48 × 2

Leading dense layers

first 2 FFNs dense, as wide as a token’s active experts (DeepSeek-V3: 3 of 61, 18432 \= 9 × 2048; Kimi K2: 1 of 61\)

layer 1

dense FFN

layer 2

dense FFN

layer 3

\+4%

layer 4

\+6%

layer 5

\+6%

layer 6

\+6%

layer 7

\+10%

layer 8

\+4%

training step



balanced

mean \+15%

\+10%, layer 7

12 \= 6 MoE layers × 2

DeepSeek-V3: 116 \= 58 × 2

MoE every other layer

odd layers dense, as wide as shared \+ top-1 expert (Llama 4 Maverick: 24 of 48, 16384 \= 2 × 8192\)

layer 1

dense FFN

layer 2

\+10%

layer 3

dense FFN

layer 4

\+6%

layer 5

dense FFN

layer 6

\+6%

layer 7

dense FFN

layer 8

\+4%

training step



balanced

mean \+31%

\+10%, layer 2

8 \= 4 MoE layers × 2

Llama 4 Maverick: 48 \= 24 × 2

Routing follows the token id less with depth, which is why the first layers balance slowest.

Leading dense layers give the lowest overload over training, while MoE every other layer needs the fewest all-to-alls: the layout trades early-layer balance against communication.

Routing follows the token id less with depth, which is why the first layers balance slowest.

## Sample 2

Parameters: `{"t": 6.75}`

Where should an MoE model’s dense FFN layers go?

overload (MaxVio) per layer

worst MoE layer over training

all-to-alls per forward pass

MoE in every layer

every FFN is a routed MoE (Qwen3, gpt-oss, MiniMax M2, Llama 4 Scout)

layer 1

\+63%

layer 2

\+19%

layer 3

\+4%

layer 4

\+6%

layer 5

\+6%

layer 6

\+6%

layer 7

\+10%

layer 8

\+4%

training step



balanced

mean \+80%

\+63%, layer 1

16 \= 8 MoE layers × 2

Llama 4 Scout: 96 \= 48 × 2

Leading dense layers

first 2 FFNs dense, as wide as a token’s active experts (DeepSeek-V3: 3 of 61, 18432 \= 9 × 2048; Kimi K2: 1 of 61\)

layer 1

dense FFN

layer 2

dense FFN

layer 3

\+4%

layer 4

\+6%

layer 5

\+6%

layer 6

\+6%

layer 7

\+10%

layer 8

\+4%

training step



balanced

mean \+19%

\+10%, layer 7

12 \= 6 MoE layers × 2

DeepSeek-V3: 116 \= 58 × 2

MoE every other layer

odd layers dense, as wide as shared \+ top-1 expert (Llama 4 Maverick: 24 of 48, 16384 \= 2 × 8192\)

layer 1

dense FFN

layer 2

\+19%

layer 3

dense FFN

layer 4

\+6%

layer 5

dense FFN

layer 6

\+6%

layer 7

dense FFN

layer 8

\+4%

training step



balanced

mean \+48%

\+19%, layer 2

8 \= 4 MoE layers × 2

Llama 4 Maverick: 48 \= 24 × 2

Routing follows the token id less with depth, which is why the first layers balance slowest.

Deeper layers settle sooner, and the first layer balances slowest, which leading dense layers skip.

Routing follows the token id less with depth, which is why the first layers balance slowest.

## Sample 3

Parameters: `{"seed": 1, "t": 0}`

Where should an MoE model’s dense FFN layers go?

overload (MaxVio) per layer

worst MoE layer over training

all-to-alls per forward pass

MoE in every layer

every FFN is a routed MoE (Qwen3, gpt-oss, MiniMax M2, Llama 4 Scout)

layer 1

\+40%

layer 2

\+33%

layer 3

\+6%

layer 4

\+8%

layer 5

\+6%

layer 6

\+13%

layer 7

\+6%

layer 8

\+10%

training step



balanced

mean \+55%

\+40%, layer 1

16 \= 8 MoE layers × 2

Llama 4 Scout: 96 \= 48 × 2

Leading dense layers

first 2 FFNs dense, as wide as a token’s active experts (DeepSeek-V3: 3 of 61, 18432 \= 9 × 2048; Kimi K2: 1 of 61\)

layer 1

dense FFN

layer 2

dense FFN

layer 3

\+6%

layer 4

\+8%

layer 5

\+6%

layer 6

\+13%

layer 7

\+6%

layer 8

\+10%

training step



balanced

mean \+28%

\+13%, layer 6

12 \= 6 MoE layers × 2

DeepSeek-V3: 116 \= 58 × 2

MoE every other layer

odd layers dense, as wide as shared \+ top-1 expert (Llama 4 Maverick: 24 of 48, 16384 \= 2 × 8192\)

layer 1

dense FFN

layer 2

\+33%

layer 3

dense FFN

layer 4

\+8%

layer 5

dense FFN

layer 6

\+13%

layer 7

dense FFN

layer 8

\+10%

training step



balanced

mean \+47%

\+33%, layer 2

8 \= 4 MoE layers × 2

Llama 4 Maverick: 48 \= 24 × 2

Routing follows the token id less with depth, which is why the first layers balance slowest.

Leading dense layers give the lowest overload over training, while MoE every other layer needs the fewest all-to-alls: the layout trades early-layer balance against communication.

Routing follows the token id less with depth, which is why the first layers balance slowest.

## Sample 4

Parameters: `{"seed": 10.5, "t": 0}`

Where should an MoE model’s dense FFN layers go?

overload (MaxVio) per layer

worst MoE layer over training

all-to-alls per forward pass

MoE in every layer

every FFN is a routed MoE (Qwen3, gpt-oss, MiniMax M2, Llama 4 Scout)

layer 1

\+56%

layer 2

\+23%

layer 3

\+10%

layer 4

\+10%

layer 5

\+8%

layer 6

\+8%

layer 7

\+10%

layer 8

\+8%

training step



balanced

mean \+72%

\+56%, layer 1

16 \= 8 MoE layers × 2

Llama 4 Scout: 96 \= 48 × 2

Leading dense layers

first 2 FFNs dense, as wide as a token’s active experts (DeepSeek-V3: 3 of 61, 18432 \= 9 × 2048; Kimi K2: 1 of 61\)

layer 1

dense FFN

layer 2

dense FFN

layer 3

\+10%

layer 4

\+10%

layer 5

\+8%

layer 6

\+8%

layer 7

\+10%

layer 8

\+8%

training step



balanced

mean \+30%

\+10%, layer 3

12 \= 6 MoE layers × 2

DeepSeek-V3: 116 \= 58 × 2

MoE every other layer

odd layers dense, as wide as shared \+ top-1 expert (Llama 4 Maverick: 24 of 48, 16384 \= 2 × 8192\)

layer 1

dense FFN

layer 2

\+23%

layer 3

dense FFN

layer 4

\+10%

layer 5

dense FFN

layer 6

\+8%

layer 7

dense FFN

layer 8

\+8%

training step



balanced

mean \+61%

\+23%, layer 2

8 \= 4 MoE layers × 2

Llama 4 Maverick: 48 \= 24 × 2

Routing follows the token id less with depth, which is why the first layers balance slowest.

Leading dense layers give the lowest overload over training, while MoE every other layer needs the fewest all-to-alls: the layout trades early-layer balance against communication.

Routing follows the token id less with depth, which is why the first layers balance slowest.

## Sample 5

Parameters: `{"seed": 20, "t": 0}`

Where should an MoE model’s dense FFN layers go?

overload (MaxVio) per layer

worst MoE layer over training

all-to-alls per forward pass

MoE in every layer

every FFN is a routed MoE (Qwen3, gpt-oss, MiniMax M2, Llama 4 Scout)

layer 1

\+38%

layer 2

\+8%

layer 3

\+8%

layer 4

\+10%

layer 5

\+8%

layer 6

\+8%

layer 7

\+8%

layer 8

\+8%

training step



balanced

mean \+60%

\+38%, layer 1

16 \= 8 MoE layers × 2

Llama 4 Scout: 96 \= 48 × 2

Leading dense layers

first 2 FFNs dense, as wide as a token’s active experts (DeepSeek-V3: 3 of 61, 18432 \= 9 × 2048; Kimi K2: 1 of 61\)

layer 1

dense FFN

layer 2

dense FFN

layer 3

\+8%

layer 4

\+10%

layer 5

\+8%

layer 6

\+8%

layer 7

\+8%

layer 8

\+8%

training step



balanced

mean \+19%

\+10%, layer 4

12 \= 6 MoE layers × 2

DeepSeek-V3: 116 \= 58 × 2

MoE every other layer

odd layers dense, as wide as shared \+ top-1 expert (Llama 4 Maverick: 24 of 48, 16384 \= 2 × 8192\)

layer 1

dense FFN

layer 2

\+8%

layer 3

dense FFN

layer 4

\+10%

layer 5

dense FFN

layer 6

\+8%

layer 7

dense FFN

layer 8

\+8%

training step



balanced

mean \+34%

\+10%, layer 4

8 \= 4 MoE layers × 2

Llama 4 Maverick: 48 \= 24 × 2

Routing follows the token id less with depth, which is why the first layers balance slowest.

Leading dense layers give the lowest overload over training, while MoE every other layer needs the fewest all-to-alls: the layout trades early-layer balance against communication.

Routing follows the token id less with depth, which is why the first layers balance slowest.

## Sample 6

Parameters: `{"t": 1.5}`

Where should an MoE model’s dense FFN layers go?

overload (MaxVio) per layer

worst MoE layer over training

all-to-alls per forward pass

MoE in every layer

every FFN is a routed MoE (Qwen3, gpt-oss, MiniMax M2, Llama 4 Scout)

layer 1

\+96%

layer 2

\+75%

layer 3

\+40%

layer 4

\+46%

layer 5

\+31%

layer 6

\+35%

layer 7

\+40%

layer 8

\+33%

training step



balanced

\+96%, layer 1

16 \= 8 MoE layers × 2

Llama 4 Scout: 96 \= 48 × 2

Leading dense layers

first 2 FFNs dense, as wide as a token’s active experts (DeepSeek-V3: 3 of 61, 18432 \= 9 × 2048; Kimi K2: 1 of 61\)

layer 1

dense FFN

layer 2

dense FFN

layer 3

\+40%

layer 4

\+46%

layer 5

\+31%

layer 6

\+35%

layer 7

\+40%

layer 8

\+33%

training step



balanced

\+46%, layer 4

12 \= 6 MoE layers × 2

DeepSeek-V3: 116 \= 58 × 2

MoE every other layer

odd layers dense, as wide as shared \+ top-1 expert (Llama 4 Maverick: 24 of 48, 16384 \= 2 × 8192\)

layer 1

dense FFN

layer 2

\+75%

layer 3

dense FFN

layer 4

\+46%

layer 5

dense FFN

layer 6

\+35%

layer 7

dense FFN

layer 8

\+33%

training step



balanced

\+75%, layer 2

8 \= 4 MoE layers × 2

Llama 4 Maverick: 48 \= 24 × 2

Routing follows the token id less with depth, which is why the first layers balance slowest.

Each row runs the same toy, and its bars show every layer’s overload at the current step.

Routing follows the token id less with depth, which is why the first layers balance slowest.

## Sample 7

Parameters: `{"t": 5.1}`

Where should an MoE model’s dense FFN layers go?

overload (MaxVio) per layer

worst MoE layer over training

all-to-alls per forward pass

MoE in every layer

every FFN is a routed MoE (Qwen3, gpt-oss, MiniMax M2, Llama 4 Scout)

layer 1

\+79%

layer 2

\+35%

layer 3

\+8%

layer 4

\+8%

layer 5

\+10%

layer 6

\+6%

layer 7

\+6%

layer 8

\+6%

training step



balanced

mean \+86%

\+79%, layer 1

16 \= 8 MoE layers × 2

Llama 4 Scout: 96 \= 48 × 2

Leading dense layers

first 2 FFNs dense, as wide as a token’s active experts (DeepSeek-V3: 3 of 61, 18432 \= 9 × 2048; Kimi K2: 1 of 61\)

layer 1

dense FFN

layer 2

dense FFN

layer 3

\+8%

layer 4

\+8%

layer 5

\+10%

layer 6

\+6%

layer 7

\+6%

layer 8

\+6%

training step



balanced

mean \+23%

\+10%, layer 5

12 \= 6 MoE layers × 2

DeepSeek-V3: 116 \= 58 × 2

MoE every other layer

odd layers dense, as wide as shared \+ top-1 expert (Llama 4 Maverick: 24 of 48, 16384 \= 2 × 8192\)

layer 1

dense FFN

layer 2

\+35%

layer 3

dense FFN

layer 4

\+8%

layer 5

dense FFN

layer 6

\+6%

layer 7

dense FFN

layer 8

\+6%

training step



balanced

mean \+58%

\+35%, layer 2

8 \= 4 MoE layers × 2

Llama 4 Maverick: 48 \= 24 × 2

Routing follows the token id less with depth, which is why the first layers balance slowest.

Deeper layers settle sooner, and the first layer balances slowest, which leading dense layers skip.

Routing follows the token id less with depth, which is why the first layers balance slowest.
