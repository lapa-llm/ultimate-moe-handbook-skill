# router-score-shape

[Interactive original](../upstream/app/public/viz/index.html?c=router-score-shape) · [Poster](../upstream/app/public/viz/posters/router-score-shape.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/router-score-shape-DQZKyb1t.js)

## Controls

```json
{
  "k": {
    "min": 2,
    "max": 8,
    "step": 1,
    "value": 4,
    "label": "experts picked (k)",
    "hidden": true
  },
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 2,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 12 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

16.3

11.6

7.9

5.5

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.01

.99

top-4

score

weight

0.99



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.25

.25

.25

.25

top-4

score

weight

0.25



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.27

.32

.22

.19

top-4

score

weight

0.32

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 2

Parameters: `{"t": 6}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

2.9

2.0

1.4

1.0

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.24

.55

.13

.08

top-4

score

weight

0.55



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.26

.28

.24

.22

top-4

score

weight

0.28



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.26

.31

.23

.20

top-4

score

weight

0.31

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

The logits scale up together, from an unsure router to a confident one, and the top-k stays the same in every row.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 3

Parameters: `{"k": 2, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

16.3

11.6

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.01

.99

top-2

score

weight

0.99



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.50

.50

top-2

score

weight

0.50



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.46

.54

top-2

score

weight

0.54

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 4

Parameters: `{"k": 3, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

16.3

11.6

7.9

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.01

.99

top-3

score

weight

0.99



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.33

.33

.33

top-3

score

weight

0.33



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.33

.39

.27

top-3

score

weight

0.39

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 5

Parameters: `{"k": 5, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

16.3

11.6

7.9

5.5

3.1

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.01

.99

top-5

score

weight

0.99



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.19

.20

.20

.20

.20

top-5

score

weight

0.20



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.12

.24

.28

.20

.16

top-5

score

weight

0.28

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 6

Parameters: `{"k": 6, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

16.3

11.6

7.9

5.5

3.1

1.1

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.01

.99

top-6

score

weight

0.99



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.17

.13

.18

.18

.18

.17

top-6

score

weight

0.18



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.11

.08

.22

.26

.18

.15

top-6

score

weight

0.26

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split among the experts with positive logits and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 7

Parameters: `{"k": 7, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

16.3

11.6

7.9

5.5

3.1

1.1

−0.9

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.01

.99

top-7

score

weight

0.99



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.05

.16

.13

.17

.17

.17

.17

top-7

score

weight

0.17



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.04

.11

.07

.21

.25

.17

.14

top-7

score

weight

0.25

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split among the experts with positive logits and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 8

Parameters: `{"k": 8, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

16.3

11.6

7.9

5.5

3.1

1.1

−0.9

−2.0

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.01

.99

top-8

score

weight

0.99



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.05

.16

.12

.16

.16

.16

.02

.16

top-8

score

weight

0.16



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.04

.11

.07

.21

.24

.17

.02

.14

top-8

score

weight

0.24

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split among the experts with positive logits and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 9

Parameters: `{"seed": 1, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

15.8

11.7

7.9

5.3

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.98

.02

top-4

score

weight

0.98



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.25

.25

.25

.25

top-4

score

weight

0.25



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.18

.32

.27

.23

top-4

score

weight

0.32

1

2

4

8

15.8

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 10

Parameters: `{"seed": 10.5, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

15.8

11.9

8.0

4.9

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.02

.98

top-4

score

weight

0.98



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.25

.25

.25

.25

top-4

score

weight

0.25



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.18

.23

.28

.32

top-4

score

weight

0.32

1

2

4

8

15.8

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 11

Parameters: `{"seed": 20, "t": 0}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

16.2

11.9

7.9

5.0

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.99

.01

top-4

score

weight

0.99



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.25

.25

.25

.25

top-4

score

weight

0.25



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.32

.18

.28

.22

top-4

score

weight

0.32

1

2

4

8

16.2

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

Softmax ends on one expert, sigmoid on an even split and sqrt(softplus) between, in the logits’ order: once the router is confident, the gating function alone decides whether it follows one expert or mixes its top-k.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

## Sample 12

Parameters: `{"t": 1.5}`

Gating function: how much routing weight does each top-k expert get?

One token’s router logits

0.7

0.5

0.3

0.2

logit z

0

Softmax

exp(z), renormalized over the top-k (Mixtral, Qwen3)

.26

.31

.22

.20

top-4

score

weight

0.31



top expert’s weight

even split

Sigmoid

σ(z), renormalized over the top-k (DeepSeek-V3, Kimi K2)

.26

.27

.24

.23

top-4

score

weight

0.27



top expert’s weight

even split

sqrt(softplus)

√softplus(z), renormalized over the top-k (DeepSeek-V4)

.25

.27

.24

.23

top-4

score

weight

0.27

1

2

4

8

16.3

top expert’s logit

top expert’s weight

even split

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.

The logits scale up together, from an unsure router to a confident one, and the top-k stays the same in every row.

One token’s logits, all multiplied by one scale. Weights are renormalized over the top-k, before any selection bias or routed scaling factor.
