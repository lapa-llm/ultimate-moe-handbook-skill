# shared-expert-weight

[Interactive original](../upstream/app/public/viz/index.html?c=shared-expert-weight) · [Poster](../upstream/app/public/viz/posters/shared-expert-weight.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/shared-expert-weight-Dv2PDBKS.js)

## Controls

```json
{
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

Animation duration: 10.4 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How should shared experts be weighted against the routed experts?

weight on each FFN’s output

always-on share: a / (a \+ Σ routed weights)

token copies dispatched

Routed experts only
top-4, weights renormalized to sum to 1 (gpt-oss; Qwen3 at top-8)

.13

.32

.34

.20

routed experts

0%

4

Shared expert
one expert at weight 1 \+ top-3 sigmoid scores renormalized, ×2.5 (DeepSeek-V3, GLM-4.5: 1 \+ top-8)

.87

.89

.74

routed experts

1

shared

λ \= 1 (GLM-4.5-Air, Mistral Large 3): 50%

29%

3

Gated shared expert
shared expert at weight σ(w·x) \+ top-3 renormalized (Qwen3-Next: 1 \+ top-10; Qwen3.5)

.37

.39

.24

routed experts

.19

shared

ticks: all 8 tokens

16%

3

Jointly normalized shared experts
2 shared \+ top-2, sigmoid scores normalized together to sum to 8g (Inkling: 2 \+ top-6)

1.16

1.19

routed experts

1.07

.58

2 shared

ticks: all 8 tokens

dashed: Inkling’s 2 \+ top-6 of 256, 15%

41%

2

Parallel dense FFN
dense FFN two experts wide \+ top-2 of 8 not renormalized, both ×1/√2 (Grok 2\)

.20

.21

routed experts

.71

dense FFN

ticks: all 8 tokens

63%

2

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

The always-on share stays fixed in the second row; under a gate, joint scoring or unrenormalized routed weights it moves with each token. Always-on experts are never dispatched, so each row sends only its top-k copies.

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

## Sample 2

Parameters: `{"t": 5.2}`

How should shared experts be weighted against the routed experts?

weight on each FFN’s output

always-on share: a / (a \+ Σ routed weights)

token copies dispatched

Routed experts only
top-4, weights renormalized to sum to 1 (gpt-oss; Qwen3 at top-8)

.17

.31

.10

.42

routed experts

0%

4

Shared expert
one expert at weight 1 \+ top-3 sigmoid scores renormalized, ×2.5 (DeepSeek-V3, GLM-4.5: 1 \+ top-8)

.68

.87

.96

routed experts

1

shared

λ \= 1 (GLM-4.5-Air, Mistral Large 3): 50%

29%

3

Gated shared expert
shared expert at weight σ(w·x) \+ top-3 renormalized (Qwen3-Next: 1 \+ top-10; Qwen3.5)

.19

.34

.47

routed experts

.77

shared

ticks: all 8 tokens

43%

3

Jointly normalized shared experts
2 shared \+ top-2, sigmoid scores normalized together to sum to 8g (Inkling: 2 \+ top-6)

1.04

1.14

routed experts

1.52

.30

2 shared

ticks: all 8 tokens

dashed: Inkling’s 2 \+ top-6 of 256, 15%

46%

2

Parallel dense FFN
dense FFN two experts wide \+ top-2 of 8 not renormalized, both ×1/√2 (Grok 2\)

.18

.24

routed experts

.71

dense FFN

ticks: all 8 tokens

63%

2

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

The always-on share stays fixed in the second row; under a gate, joint scoring or unrenormalized routed weights it moves with each token. Always-on experts are never dispatched, so each row sends only its top-k copies.

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

## Sample 3

Parameters: `{"seed": 1, "t": 0}`

How should shared experts be weighted against the routed experts?

weight on each FFN’s output

always-on share: a / (a \+ Σ routed weights)

token copies dispatched

Routed experts only
top-4, weights renormalized to sum to 1 (gpt-oss; Qwen3 at top-8)

.05

.03

.17

.75

routed experts

0%

4

Shared expert
one expert at weight 1 \+ top-3 sigmoid scores renormalized, ×2.5 (DeepSeek-V3, GLM-4.5: 1 \+ top-8)

.50

.85

1.15

routed experts

1

shared

λ \= 1 (GLM-4.5-Air, Mistral Large 3): 50%

29%

3

Gated shared expert
shared expert at weight σ(w·x) \+ top-3 renormalized (Qwen3-Next: 1 \+ top-10; Qwen3.5)

.06

.17

.77

routed experts

.44

shared

ticks: all 8 tokens

31%

3

Jointly normalized shared experts
2 shared \+ top-2, sigmoid scores normalized together to sum to 8g (Inkling: 2 \+ top-6)

1.16

1.56

routed experts

1.22

.07

2 shared

ticks: all 8 tokens

dashed: Inkling’s 2 \+ top-6 of 256, 15%

32%

2

Parallel dense FFN
dense FFN two experts wide \+ top-2 of 8 not renormalized, both ×1/√2 (Grok 2\)

.11

.50

routed experts

.71

dense FFN

ticks: all 8 tokens

54%

2

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

The always-on share stays fixed in the second row; under a gate, joint scoring or unrenormalized routed weights it moves with each token. Always-on experts are never dispatched, so each row sends only its top-k copies.

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

## Sample 4

Parameters: `{"seed": 10.5, "t": 0}`

How should shared experts be weighted against the routed experts?

weight on each FFN’s output

always-on share: a / (a \+ Σ routed weights)

token copies dispatched

Routed experts only
top-4, weights renormalized to sum to 1 (gpt-oss; Qwen3 at top-8)

.14

.23

.46

.17

routed experts

0%

4

Shared expert
one expert at weight 1 \+ top-3 sigmoid scores renormalized, ×2.5 (DeepSeek-V3, GLM-4.5: 1 \+ top-8)

.80

1

.70

routed experts

1

shared

λ \= 1 (GLM-4.5-Air, Mistral Large 3): 50%

29%

3

Gated shared expert
shared expert at weight σ(w·x) \+ top-3 renormalized (Qwen3-Next: 1 \+ top-10; Qwen3.5)

.27

.54

.20

routed experts

.68

shared

ticks: all 8 tokens

40%

3

Jointly normalized shared experts
2 shared \+ top-2, sigmoid scores normalized together to sum to 8g (Inkling: 2 \+ top-6)

.87

1.09

routed experts

.89

1.15

2 shared

ticks: all 8 tokens

dashed: Inkling’s 2 \+ top-6 of 256, 15%

51%

2

Parallel dense FFN
dense FFN two experts wide \+ top-2 of 8 not renormalized, both ×1/√2 (Grok 2\)

.12

.24

routed experts

.71

dense FFN

ticks: all 8 tokens

67%

2

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

The always-on share stays fixed in the second row; under a gate, joint scoring or unrenormalized routed weights it moves with each token. Always-on experts are never dispatched, so each row sends only its top-k copies.

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

## Sample 5

Parameters: `{"seed": 20, "t": 0}`

How should shared experts be weighted against the routed experts?

weight on each FFN’s output

always-on share: a / (a \+ Σ routed weights)

token copies dispatched

Routed experts only
top-4, weights renormalized to sum to 1 (gpt-oss; Qwen3 at top-8)

.33

.07

.49

.11

routed experts

0%

4

Shared expert
one expert at weight 1 \+ top-3 sigmoid scores renormalized, ×2.5 (DeepSeek-V3, GLM-4.5: 1 \+ top-8)

.88

.93

.69

routed experts

1

shared

λ \= 1 (GLM-4.5-Air, Mistral Large 3): 50%

29%

3

Gated shared expert
shared expert at weight σ(w·x) \+ top-3 renormalized (Qwen3-Next: 1 \+ top-10; Qwen3.5)

.35

.53

.12

routed experts

.38

shared

ticks: all 8 tokens

28%

3

Jointly normalized shared experts
2 shared \+ top-2, sigmoid scores normalized together to sum to 8g (Inkling: 2 \+ top-6)

1.03

1.08

routed experts

.84

1.04

2 shared

ticks: all 8 tokens

dashed: Inkling’s 2 \+ top-6 of 256, 15%

47%

2

Parallel dense FFN
dense FFN two experts wide \+ top-2 of 8 not renormalized, both ×1/√2 (Grok 2\)

.21

.31

routed experts

.71

dense FFN

ticks: all 8 tokens

58%

2

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.

The always-on share stays fixed in the second row; under a gate, joint scoring or unrenormalized routed weights it moves with each token. Always-on experts are never dispatched, so each row sends only its top-k copies.

Router logits are random draws, and Qwen’s gate logit is drawn at its initialization spread, so the ticks show how each share moves, not trained values. The dashed 15% averages random logits of the same spread at Inkling’s shape.
