# expert-upcycling

[Interactive original](../upstream/app/public/viz/index.html?c=expert-upcycling) · [Poster](../upstream/app/public/viz/posters/expert-upcycling.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/expert-upcycling-C9mXVjmq.js)

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

Animation duration: 12 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How to initialize the new experts when growing a trained MoE

one token’s router logits, top-2 in blue

the trained 8the 8 added

tokens selecting an expert and its copy

routing weight on untrained experts, right after growing

Copy

expert i and its router row copied to i \+ 8: Expert Upcycling (32 → 64\)

.50

.50

top-2

logit

weight

training step after growing

chance 7%

100%

0%

0%

Copy, perturb the copy

copy’s FFN perturbed, router row still copied: Drop-Upcycling r \= 0.5 (half re-initialized, as Expert Upcycling tested it), K-EXAONE 2.0 (rotation noise, 128 → 256\)

.50

.50

top-2

logit

weight

training step after growing

100%

0%

25% (Drop-Upcycling)

Random experts

new experts and router rows drawn from a Gaussian, router biases reset to 0: EMO (8 → 16 → … → 128\)

.43

.57

top-2

logit

weight

no copies

54%

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

Right after growing, an exact copy scores like its original, so tokens pick an expert and its copy together.

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

## Sample 2

Parameters: `{"t": 6}`

How to initialize the new experts when growing a trained MoE

one token’s router logits, top-2 in blue

the trained 8the 8 added

tokens selecting an expert and its copy

routing weight on untrained experts, right after growing

Copy

expert i and its router row copied to i \+ 8: Expert Upcycling (32 → 64\)

.46

.54

top-2

logit

weight

95%

training step after growing

chance 7%

100%

0%

0%

Copy, perturb the copy

copy’s FFN perturbed, router row still copied: Drop-Upcycling r \= 0.5 (half re-initialized, as Expert Upcycling tested it), K-EXAONE 2.0 (rotation noise, 128 → 256\)

.83

.17

top-2

logit

weight

9%

training step after growing

100%

0%

25% (Drop-Upcycling)

Random experts

new experts and router rows drawn from a Gaussian, router biases reset to 0: EMO (8 → 16 → … → 128\)

.43

.57

top-2

logit

weight

no copies

54%

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

Training pulls the pairs apart: the perturbed copies split first, the exact ones only once noise has grown.

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

## Sample 3

Parameters: `{"t": 12}`

How to initialize the new experts when growing a trained MoE

one token’s router logits, top-2 in blue

the trained 8the 8 added

tokens selecting an expert and its copy

routing weight on untrained experts, right after growing

Copy

expert i and its router row copied to i \+ 8: Expert Upcycling (32 → 64\)

.13

.87

top-2

logit

weight

58%

training step after growing

chance 7%

100%

0%

0%

Copy, perturb the copy

copy’s FFN perturbed, router row still copied: Drop-Upcycling r \= 0.5 (half re-initialized, as Expert Upcycling tested it), K-EXAONE 2.0 (rotation noise, 128 → 256\)

.80

.20

top-2

logit

weight

9%

training step after growing

100%

0%

25% (Drop-Upcycling)

Random experts

new experts and router rows drawn from a Gaussian, router biases reset to 0: EMO (8 → 16 → … → 128\)

.43

.57

top-2

logit

weight

no copies

54%

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

Once split, pairs route like distinct experts and the added capacity counts; the price of splitting early is untrained weight, half of each Drop-Upcycling copy and all of each random expert.

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

How to initialize the new experts when growing a trained MoE

one token’s router logits, top-2 in blue

the trained 8the 8 added

tokens selecting an expert and its copy

routing weight on untrained experts, right after growing

Copy

expert i and its router row copied to i \+ 8: Expert Upcycling (32 → 64\)

.50

.50

top-2

logit

weight

training step after growing

chance 7%

100%

0%

0%

Copy, perturb the copy

copy’s FFN perturbed, router row still copied: Drop-Upcycling r \= 0.5 (half re-initialized, as Expert Upcycling tested it), K-EXAONE 2.0 (rotation noise, 128 → 256\)

.50

.50

top-2

logit

weight

training step after growing

100%

0%

25% (Drop-Upcycling)

Random experts

new experts and router rows drawn from a Gaussian, router biases reset to 0: EMO (8 → 16 → … → 128\)

.96

.04

top-2

logit

weight

no copies

39%

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

Right after growing, an exact copy scores like its original, so tokens pick an expert and its copy together.

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

How to initialize the new experts when growing a trained MoE

one token’s router logits, top-2 in blue

the trained 8the 8 added

tokens selecting an expert and its copy

routing weight on untrained experts, right after growing

Copy

expert i and its router row copied to i \+ 8: Expert Upcycling (32 → 64\)

.50

.50

top-2

logit

weight

training step after growing

chance 7%

100%

0%

0%

Copy, perturb the copy

copy’s FFN perturbed, router row still copied: Drop-Upcycling r \= 0.5 (half re-initialized, as Expert Upcycling tested it), K-EXAONE 2.0 (rotation noise, 128 → 256\)

.50

.50

top-2

logit

weight

training step after growing

100%

0%

25% (Drop-Upcycling)

Random experts

new experts and router rows drawn from a Gaussian, router biases reset to 0: EMO (8 → 16 → … → 128\)

.69

.31

top-2

logit

weight

no copies

41%

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

Right after growing, an exact copy scores like its original, so tokens pick an expert and its copy together.

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

## Sample 6

Parameters: `{"seed": 20, "t": 0}`

How to initialize the new experts when growing a trained MoE

one token’s router logits, top-2 in blue

the trained 8the 8 added

tokens selecting an expert and its copy

routing weight on untrained experts, right after growing

Copy

expert i and its router row copied to i \+ 8: Expert Upcycling (32 → 64\)

.50

.50

top-2

logit

weight

training step after growing

chance 7%

100%

0%

0%

Copy, perturb the copy

copy’s FFN perturbed, router row still copied: Drop-Upcycling r \= 0.5 (half re-initialized, as Expert Upcycling tested it), K-EXAONE 2.0 (rotation noise, 128 → 256\)

.50

.50

top-2

logit

weight

training step after growing

100%

0%

25% (Drop-Upcycling)

Random experts

new experts and router rows drawn from a Gaussian, router biases reset to 0: EMO (8 → 16 → … → 128\)

.86

.14

top-2

logit

weight

no copies

45%

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

Right after growing, an exact copy scores like its original, so tokens pick an expert and its copy together.

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

## Sample 7

Parameters: `{"t": 2.5}`

How to initialize the new experts when growing a trained MoE

one token’s router logits, top-2 in blue

the trained 8the 8 added

tokens selecting an expert and its copy

routing weight on untrained experts, right after growing

Copy

expert i and its router row copied to i \+ 8: Expert Upcycling (32 → 64\)

.50

.50

top-2

logit

weight

training step after growing

chance 7%

100%

0%

0%

Copy, perturb the copy

copy’s FFN perturbed, router row still copied: Drop-Upcycling r \= 0.5 (half re-initialized, as Expert Upcycling tested it), K-EXAONE 2.0 (rotation noise, 128 → 256\)

.48

.52

top-2

logit

weight

98%

training step after growing

100%

0%

25% (Drop-Upcycling)

Random experts

new experts and router rows drawn from a Gaussian, router biases reset to 0: EMO (8 → 16 → … → 128\)

.43

.57

top-2

logit

weight

no copies

54%

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

Training pulls the pairs apart: the perturbed copies split first, the exact ones only once noise has grown.

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

## Sample 8

Parameters: `{"t": 7.5}`

How to initialize the new experts when growing a trained MoE

one token’s router logits, top-2 in blue

the trained 8the 8 added

tokens selecting an expert and its copy

routing weight on untrained experts, right after growing

Copy

expert i and its router row copied to i \+ 8: Expert Upcycling (32 → 64\)

.39

.61

top-2

logit

weight

88%

training step after growing

chance 7%

100%

0%

0%

Copy, perturb the copy

copy’s FFN perturbed, router row still copied: Drop-Upcycling r \= 0.5 (half re-initialized, as Expert Upcycling tested it), K-EXAONE 2.0 (rotation noise, 128 → 256\)

.80

.20

top-2

logit

weight

9%

training step after growing

100%

0%

25% (Drop-Upcycling)

Random experts

new experts and router rows drawn from a Gaussian, router biases reset to 0: EMO (8 → 16 → … → 128\)

.43

.57

top-2

logit

weight

no copies

54%

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.

Once split, pairs route like distinct experts and the added capacity counts; the price of splitting early is untrained weight, half of each Drop-Upcycling copy and all of each random expert.

The pairs’ split rates are assumed, and the random experts’ router rows start at the trained rows’ scale.
