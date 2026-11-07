# router-temperature

[Interactive original](../upstream/app/public/viz/index.html?c=router-temperature) · [Poster](../upstream/app/public/viz/posters/router-temperature.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/router-temperature-CDVOhRT4.js)

## Controls

```json
{
  "loud": {
    "min": 2,
    "max": 12,
    "step": 1,
    "value": 6,
    "label": "large-norm token (× usual norm)"
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

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (6×)usual token

3.9

.65

2.8

.21

1.9

.09

1.3

.05

logit

0

weight



0.65

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

3.9

.65

2.8

.21

1.9

.09

1.3

.05

logit

0

weight



0.65

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 2

Parameters: `{"t": 6}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (6×)usual token

28

1.00

20

14

9.5

logit

0

weight



1.00

0.72

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

22

.99

18

.01

13

9.2

logit

0

weight



0.99

0.71

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

4.7

.72

3.4

.18

2.3

.06

1.6

.03

logit

0

weight



0.72

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 25 of 40\. In the linear router the large-norm token reaches one expert first: its logits grow with its norm as well as with W.

## Sample 3

Parameters: `{"t": 12}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (6×)usual token

98

1.00

69

48

33

logit

0

weight



1.00

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

30

.58

29

.36

28

.06

24

logit

0

weight



0.58

0.98

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

16

.99

12

.01

7.9

5.5

logit

0

weight



0.99

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 40 of 40\. The linear router ends on one expert, soft-capping pulls the large-norm token back at its cap, the normalized input still sharpens with W, and only gating logit normalization holds a sharpness you set.

## Sample 4

Parameters: `{"loud": 2, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (2×)usual token

1.3

.38

0.9

.26

0.6

.20

0.4

.16

logit

0

weight



0.38

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

1.3

.38

0.9

.26

0.6

.20

0.4

.16

0

weight



0.38

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 5

Parameters: `{"loud": 3, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (3×)usual token

2.0

.45

1.4

.26

1.0

.17

0.7

.12

logit

0

weight



0.45

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

1.9

.45

1.4

.26

1.0

.17

0.7

.12

logit

0

weight



0.45

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 6

Parameters: `{"loud": 4, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (4×)usual token

2.6

.52

1.8

.25

1.3

.14

0.9

.09

logit

0

weight



0.52

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

2.6

.52

1.8

.25

1.3

.14

0.9

.09

logit

0

weight



0.52

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 7

Parameters: `{"loud": 5, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (5×)usual token

3.3

.59

2.3

.23

1.6

.11

1.1

.07

logit

0

weight



0.59

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

3.2

.59

2.3

.23

1.6

.11

1.1

.07

logit

0

weight



0.59

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 8

Parameters: `{"loud": 7, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (7×)usual token

4.6

.71

3.2

.19

2.2

.07

1.5

.03

logit

0

weight



0.71

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

4.5

.70

3.2

.19

2.2

.07

1.5

.04

logit

0

weight



0.70

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 9

Parameters: `{"loud": 8, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (8×)usual token

5.2

.76

3.7

.17

2.5

.05

1.7

.02

logit

0

weight



0.76

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

5.2

.75

3.7

.17

2.5

.05

1.7

.02

logit

weight



0.75

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 10

Parameters: `{"loud": 9, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (9×)usual token

5.9

.80

4.2

.15

2.9

.04

2.0

.02

logit

0

weight



0.80

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

5.8

.79

4.1

.15

2.8

.04

2.0

.02

logit

weight



0.79

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 11

Parameters: `{"loud": 10, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (10×)usual token

6.5

.83

4.6

.13

3.2

.03

2.2

.01

logit

0

weight



0.83

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

6.4

.82

4.6

.13

3.2

.03

2.2

.01

logit

weight



0.82

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 12

Parameters: `{"loud": 11, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (11×)usual token

7.2

.86

5.1

.11

3.5

.02

2.4

.01

logit

0

weight



0.86

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

7.0

.85

5.0

.12

3.5

.02

2.4

.01

logit

weight



0.85

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 13

Parameters: `{"loud": 12, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (12×)usual token

7.8

.89

5.5

.09

3.8

.02

2.6

logit

0

weight



0.89

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

7.6

.87

5.5

.10

3.8

.02

2.6

.01

logit

weight



0.87

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.7

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 14

Parameters: `{"seed": 1, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (6×)usual token

3.8

.62

2.8

.23

1.9

.09

1.3

.05

logit

0

weight



0.62

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

3.8

.62

2.8

.23

1.9

.10

1.3

.05

logit

0

weight



0.62

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.6

.31

0.5

.26

0.3

.23

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.3

.48

1.7

.26

1.2

.15

0.8

.10

logit

0

weight



0.48

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 15

Parameters: `{"seed": 10.5, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (6×)usual token

3.8

.62

2.9

.24

1.9

.10

1.2

.05

logit

0

weight



0.62

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

3.8

.61

2.8

.24

1.9

.10

1.2

.05

logit

0

weight



0.61

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.6

.31

0.5

.26

0.3

.23

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.3

.48

1.8

.27

1.2

.15

0.7

.10

logit

0

weight



0.48

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 16

Parameters: `{"seed": 20, "t": 0}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (6×)usual token

3.9

.64

2.9

.23

1.9

.09

1.2

.04

logit

0

weight



0.64

0.31

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

3.9

.63

2.9

.23

1.9

.09

1.2

.04

logit

0

weight



0.63

0.31

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

0.6

.31

0.5

.26

0.3

.22

0.2

.20

logit

0

weight



0.31

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.49

1.8

.26

1.2

.15

0.7

.09

logit

0

weight



0.49

training step

all on one

even split

Step 1 of 40\. Each step the router matrix W grows; every row routes the same two tokens with the same W.

## Sample 17

Parameters: `{"t": 5.1}`

What sets router sharpness as the token’s norm and router matrix grow?

large-norm token’s logits, top 4 in blue

top expert’s weight

Linear router

logit \= W·x (Mixtral, Qwen3)large-norm token (6×)usual token

21

1.00

15

10

6.9

logit

0

weight



1.00

0.61

training step

all on one

even split

Logit soft-capping

logit \= 30·tanh(W·x / 30\) (Grok 2, which skips the renormalization)

cap 30

18

.99

14

.01

9.7

6.8

logit

0

weight



0.99

0.61

training step

all on one

even split

Normalized router input

logit \= W·x / ‖x‖ (Gemma 4\)

3.4

.61

2.4

.23

1.7

.10

1.2

.06

logit

0

weight



0.61

training step

all on one

even split

Gating logit normalization

logit \= (W·x − μ) / σ, with μ and σ the mean and std of W·x across the token’s experts (Skywork-MoE)

2.4

.50

1.7

.25

1.2

.15

0.8

.10

logit

0

weight



0.50

training step

all on one

even split

Step 21 of 40\. In the linear router the large-norm token reaches one expert first: its logits grow with its norm as well as with W.
