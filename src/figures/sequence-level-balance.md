# sequence-level-balance

[Interactive original](../upstream/app/public/viz/index.html?c=sequence-level-balance) · [Poster](../upstream/app/public/viz/posters/sequence-level-balance.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/sequence-level-balance-Bl3RcXhn.js)

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

Animation duration: 13.1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Can a bias balance each sequence’s expert load without future tokens?

prose tokencode token

Global-batch bias only

global quantile balancing, fitted on this batch (Kimi K3)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

2.3× mean

bias

added to

the score

expert 4

set once for the whole batch: flat within a sequence

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

\+ causal bias from this sequence’s past

Causal Dual Bias on top (Chang, “Causal Routing Bias”, 2026\)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

1.3× mean

bias

added to

the score

expert 4

each token lowers the bias of the experts it selected, raises the others

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

Both columns balance the whole batch, but with the global-batch bias alone this sequence’s code half piles onto expert 4, while the causal bias keeps it much closer to the mean load.

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

## Sample 2

Parameters: `{"t": 6.55}`

Can a bias balance each sequence’s expert load without future tokens?

prose tokencode token

Global-batch bias only

global quantile balancing, fitted on this batch (Kimi K3)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

1.6× mean

bias

added to

the score

expert 4

set once for the whole batch: flat within a sequence

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

\+ causal bias from this sequence’s past

Causal Dual Bias on top (Chang, “Causal Routing Bias”, 2026\)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

1.2× mean

bias

added to

the score

expert 4

each token lowers the bias of the experts it selected, raises the others

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

In the code half, the global bias stays flat, while the causal bias lowers expert 4 a little after each of its picks.

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

## Sample 3

Parameters: `{"t": 13.1}`

Can a bias balance each sequence’s expert load without future tokens?

prose tokencode token

Global-batch bias only

global quantile balancing, fitted on this batch (Kimi K3)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

2.3× mean

bias

added to

the score

expert 4

set once for the whole batch: flat within a sequence

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

\+ causal bias from this sequence’s past

Causal Dual Bias on top (Chang, “Causal Routing Bias”, 2026\)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

1.3× mean

bias

added to

the score

expert 4

each token lowers the bias of the experts it selected, raises the others

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

What it costs: to balance this sequence without seeing its future tokens, the causal bias sends 34% of the batch’s picks to experts outside the router’s own top-2, against 20% with the global-batch bias alone.

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Can a bias balance each sequence’s expert load without future tokens?

prose tokencode token

Global-batch bias only

global quantile balancing, fitted on this batch (Kimi K3)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

1.9× mean

bias

added to

the score

expert 4

set once for the whole batch: flat within a sequence

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

\+ causal bias from this sequence’s past

Causal Dual Bias on top (Chang, “Causal Routing Bias”, 2026\)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

1.2× mean

bias

added to

the score

expert 4

each token lowers the bias of the experts it selected, raises the others

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

Both columns balance the whole batch, but with the global-batch bias alone this sequence’s code half piles onto expert 4, while the causal bias keeps it much closer to the mean load.

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Can a bias balance each sequence’s expert load without future tokens?

prose tokencode token

Global-batch bias only

global quantile balancing, fitted on this batch (Kimi K3)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

2.3× mean

bias

added to

the score

expert 4

set once for the whole batch: flat within a sequence

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

\+ causal bias from this sequence’s past

Causal Dual Bias on top (Chang, “Causal Routing Bias”, 2026\)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

1.2× mean

bias

added to

the score

expert 4

each token lowers the bias of the experts it selected, raises the others

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

Both columns balance the whole batch, but with the global-batch bias alone this sequence’s code half piles onto expert 4, while the causal bias keeps it much closer to the mean load.

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

## Sample 6

Parameters: `{"seed": 20, "t": 0}`

Can a bias balance each sequence’s expert load without future tokens?

prose tokencode token

Global-batch bias only

global quantile balancing, fitted on this batch (Kimi K3)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

2.0× mean

bias

added to

the score

expert 4

set once for the whole batch: flat within a sequence

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

\+ causal bias from this sequence’s past

Causal Dual Bias on top (Chang, “Causal Routing Bias”, 2026\)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

1.3× mean

bias

added to

the score

expert 4

each token lowers the bias of the experts it selected, raises the others

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

Both columns balance the whole batch, but with the global-batch bias alone this sequence’s code half piles onto expert 4, while the causal bias keeps it much closer to the mean load.

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

## Sample 7

Parameters: `{"t": 1.5}`

Can a bias balance each sequence’s expert load without future tokens?

prose tokencode token

Global-batch bias only

global quantile balancing, fitted on this batch (Kimi K3)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

bias

added to

the score

expert 4

set once for the whole batch: flat within a sequence

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

\+ causal bias from this sequence’s past

Causal Dual Bias on top (Chang, “Causal Routing Bias”, 2026\)

The whole batch (6 sequences)

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

mean load

This sequence (prose, then code)

prose

code

mean load

tokens

so far

position in the sequence

expert 4

bias

added to

the score

expert 4

each token lowers the bias of the experts it selected, raises the others

This sequence, picks per expert

mean load

expert 1

expert 2

expert 3

expert 4

expert 5

expert 6

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.

Prose first: the global bias, fitted once on the whole batch, stays fixed, while the causal bias updates after every token of this sequence.

Pairing quantile balancing with Chang’s Causal Dual Bias is our combination: Chang tested that bias alone, and paired quantile balancing only with his simpler causal bias.
