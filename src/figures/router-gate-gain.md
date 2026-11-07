# router-gate-gain

[Interactive original](../upstream/app/public/viz/index.html?c=router-gate-gain) · [Poster](../upstream/app/public/viz/posters/router-gate-gain.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/router-gate-gain-CUC2B_iY.js)

## Controls

```json
{
  "k": {
    "min": 1,
    "max": 8,
    "step": 1,
    "value": 4,
    "label": "experts picked (k)"
  },
  "experts": {
    "min": 8,
    "max": 32,
    "step": 8,
    "value": 16,
    "label": "experts",
    "hidden": true
  },
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 3,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 11.100000000000001 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.30

.11

.24

.14

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.42

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.37

.14

.31

.18

top-4

softmax

weight

0.53

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.53

.47

.52

.49

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 2

Parameters: `{"t": 5.550000000000001}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.17

.20

.15

.13

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.33

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.26

.30

.23

.21

top-4

softmax

weight

0.51

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.51

.52

.49

.48

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.65

top-1

sigmoid

weight

0.65

Expert outputs are taken as uncorrelated, with equal RMS.

As the router grows confident, the unrenormalized output follows the probability the top-k hold, while renormalizing keeps it between an even split and one expert’s.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 3

Parameters: `{"k": 1, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 1 is dropped (Switch, OLMoE, Grok-1)

.30

top-1

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.30

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-1 probabilities (Mixtral, Qwen3)

1.00

top-1

softmax

weight

1.00

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-1 scores (Kimi K2, Moonlight)

1.00

top-1

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

At top-1, renormalizing sets the one weight to 1, so the output is one expert’s RMS with or without the factor (√1 \= 1); without renormalization it follows the top expert’s probability.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 4

Parameters: `{"k": 2, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 2 is dropped (Switch, OLMoE, Grok-1)

.30

.24

top-2

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.38

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-2 probabilities (Mixtral, Qwen3)

.55

.45

top-2

softmax

weight

0.71

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-2 scores (Kimi K2, Moonlight)

.71

.70

top-2

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 5

Parameters: `{"k": 3, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 3 is dropped (Switch, OLMoE, Grok-1)

.30

.24

.14

top-3

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.41

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-3 probabilities (Mixtral, Qwen3)

.43

.36

.21

top-3

softmax

weight

0.60

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-3 scores (Kimi K2, Moonlight)

.59

.59

.55

top-3

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 6

Parameters: `{"k": 5, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 5 is dropped (Switch, OLMoE, Grok-1)

.30

.11

.24

.14

.09

top-5

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.43

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-5 probabilities (Mixtral, Qwen3)

.33

.12

.28

.16

.10

top-5

softmax

weight

0.49

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-5 scores (Kimi K2, Moonlight)

.48

.43

.47

.45

.41

top-5

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 7

Parameters: `{"k": 6, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 6 is dropped (Switch, OLMoE, Grok-1)

.30

.11

.24

.04

.14

.09

top-6

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.44

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-6 probabilities (Mixtral, Qwen3)

.32

.12

.26

.04

.16

.10

top-6

softmax

weight

0.47

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-6 scores (Kimi K2, Moonlight)

.46

.41

.45

.31

.43

.39

top-6

sigmoid

weight

1.01

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 8

Parameters: `{"k": 7, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 7 is dropped (Switch, OLMoE, Grok-1)

.03

.30

.11

.24

.04

.14

.09

top-7

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.44

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-7 probabilities (Mixtral, Qwen3)

.03

.31

.12

.26

.04

.15

.10

top-7

softmax

weight

0.46

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-7 scores (Kimi K2, Moonlight)

.27

.44

.40

.44

.30

.41

.38

top-7

sigmoid

weight

1.01

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 9

Parameters: `{"k": 8, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 8 is dropped (Switch, OLMoE, Grok-1)

.03

.30

.02

.11

.24

.04

.14

.09

top-8

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.44

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-8 probabilities (Mixtral, Qwen3)

.03

.30

.02

.11

.25

.04

.15

.09

top-8

softmax

weight

0.45

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-8 scores (Kimi K2, Moonlight)

.27

.44

.23

.39

.43

.30

.40

.37

top-8

sigmoid

weight

1.02

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 10

Parameters: `{"experts": 8, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.42

.03

.13

.37

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.58

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.44

.03

.14

.39

top-4

softmax

weight

0.60

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.59

.32

.51

.58

top-4

sigmoid

weight

1.02

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.87

top-1

sigmoid

weight

0.87

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 11

Parameters: `{"experts": 24, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.20

.10

.11

.22

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.33

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.31

.16

.18

.36

top-4

softmax

weight

0.53

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.51

.48

.49

.52

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.88

top-1

sigmoid

weight

0.88

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 12

Parameters: `{"experts": 32, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.06

.03

.03

.70

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.71

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.07

.04

.04

.85

top-4

softmax

weight

0.86

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.50

.48

.49

.53

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.99

top-1

sigmoid

weight

0.99

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 13

Parameters: `{"seed": 1, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.02

.59

.36

.02

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.69

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.02

.60

.36

.02

top-4

softmax

weight

0.70

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.46

.56

.56

.42

top-4

sigmoid

weight

1.01

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.98

top-1

sigmoid

weight

0.98

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 14

Parameters: `{"seed": 10.5, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.14

.15

.30

.24

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.44

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.17

.18

.36

.29

top-4

softmax

weight

0.52

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.49

.49

.51

.51

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.93

top-1

sigmoid

weight

0.93

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 15

Parameters: `{"seed": 20, "t": 0}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.12

.60

.10

.15

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.64

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.12

.62

.10

.16

top-4

softmax

weight

0.66

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.50

.50

.50

.50

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.99

top-1

sigmoid

weight

0.99

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 16

Parameters: `{"t": 1.5}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.08

.08

.10

.09

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.18

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.23

.23

.27

.26

top-4

softmax

weight

0.50

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.48

.49

.52

.51

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.32

top-1

sigmoid

weight

0.32

Expert outputs are taken as uncorrelated, with equal RMS.

An unsure router spreads its probability, so without renormalization the top-k weights sum to less than one and the routed output shrinks.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 17

Parameters: `{"t": 4.6}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.17

.18

.16

.13

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.32

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.26

.28

.25

.21

top-4

softmax

weight

0.51

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.51

.51

.50

.48

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.55

top-1

sigmoid

weight

0.64

Expert outputs are taken as uncorrelated, with equal RMS.

As the router grows confident, the unrenormalized output follows the probability the top-k hold, while renormalizing keeps it between an even split and one expert’s.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 18

Parameters: `{"t": 7.8}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.34

.13

.13

.13

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.41

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.47

.18

.18

.18

top-4

softmax

weight

0.56

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.55

.48

.48

.48

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.84

top-1

sigmoid

weight

0.84

Expert outputs are taken as uncorrelated, with equal RMS.

Llama 4’s top-1 has no split to renormalize: its output shrinks with the square of its one sigmoid score.

Expert outputs are taken as uncorrelated, with equal RMS.

## Sample 19

Parameters: `{"t": 9.4}`

How to normalize routing weights before combining the experts’ outputs

Softmax, not renormalized

weight \= probability; the probability outside the top 4 is dropped (Switch, OLMoE, Grok-1)

.31

.09

.23

.14

top-4

softmax

weight

Routed output RMS, relative to one expert’s

this tokenearlier tokens

0.42

one expert

OLMoE at init: 0.15

Softmax, renormalized

weight \= probability / Σ top-4 probabilities (Mixtral, Qwen3)

.39

.12

.29

.18

top-4

softmax

weight

0.54

Sigmoid, renormalized, routed scaling factor √k

weight \= √k × score / Σ top-4 scores (Kimi K2, Moonlight)

.53

.40

.51

.49

top-4

sigmoid

weight

1.00

Sigmoid on the input, top-1

the score scales the expert’s input: output × score², and its SiLU gate softens (Llama 4\)

.86

top-1

sigmoid

weight

0.86

Expert outputs are taken as uncorrelated, with equal RMS.

Only the routed scaling factor √k keeps the output near one expert’s RMS on every token, since these top-k sigmoid scores are nearly equal; without a factor, what the MoE adds to the residual stream changes size with the split.

Expert outputs are taken as uncorrelated, with equal RMS.
