# aux-load-balancing-loss

[Interactive original](../upstream/app/public/viz/index.html?c=aux-load-balancing-loss) · [Poster](../upstream/app/public/viz/posters/aux-load-balancing-loss.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/aux-load-balancing-loss-B3u1hN4Y.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 5,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 16 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Aux loss or loss-free bias: what does each give up to balance the load?

No balancing

LM loss only: no aux loss, no bias

Aux loss, small coefficient

DeepSeek-V2-Lite, Sigma-MoE-Tiny

Aux loss, large coefficient

OLMoE, Switch

Loss-free bias

sigmoid scores, no aux loss: Wang et al.

Load per expert

1

2

3

4

5

6

7

8

mean load

expert

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

One token: router scoresrouter scorewhat the LM loss wants

\+ bias− bias, used only to pick experts

score

Overload (MaxVio): how far the busiest expert sits above the mean load

\+158%

step



\+300%

balanced

Router distortion: share of router probability moved off what the LM loss wants

0%

step

40%

none

Rerouted: share of selected experts outside the top-2 that the LM loss wants

0%

step

50%

none

Measured in 1B runs with 64 experts, top-6, aux loss per sequence (Wang et al., 2024): validation-set overload, perplexity

α \= 0: ≈ \+507%, PPL ≈ 9.54

α \= 0.001: \+72%, PPL 9.56

α \= 0.01: ≈ \+10%, PPL ≈ 9.69

bias: \+4%, PPL 9.50

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

Step 1 of 40\. Each step routes the same batch. Without balancing the load stays piled on four experts; the aux loss changes router scores, while the bias changes only which experts are selected.

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

## Sample 2

Parameters: `{"t": 8}`

Aux loss or loss-free bias: what does each give up to balance the load?

No balancing

LM loss only: no aux loss, no bias

Aux loss, small coefficient

DeepSeek-V2-Lite, Sigma-MoE-Tiny

Aux loss, large coefficient

OLMoE, Switch

Loss-free bias

sigmoid scores, no aux loss: Wang et al.

Load per expert

1

2

3

4

5

6

7

8

mean load

expert

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

One token: router scoresrouter scorewhat the LM loss wants

\+ bias− bias, used only to pick experts

score

Overload (MaxVio): how far the busiest expert sits above the mean load

\+158%

step



\+300%

balanced

\+71%

\+38%

\+38%

Router distortion: share of router probability moved off what the LM loss wants

0%

step

40%

none

12%

38%

0%

Rerouted: share of selected experts outside the top-2 that the LM loss wants

0%

step

50%

none

27%

38%

41%

Measured in 1B runs with 64 experts, top-6, aux loss per sequence (Wang et al., 2024): validation-set overload, perplexity

α \= 0: ≈ \+507%, PPL ≈ 9.54

α \= 0.001: \+72%, PPL 9.56

α \= 0.01: ≈ \+10%, PPL ≈ 9.69

bias: \+4%, PPL 9.50

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

Step 23 of 40\. Each step routes the same batch. Without balancing the load stays piled on four experts; the aux loss changes router scores, while the bias changes only which experts are selected.

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

## Sample 3

Parameters: `{"t": 16}`

Aux loss or loss-free bias: what does each give up to balance the load?

No balancing

LM loss only: no aux loss, no bias

Aux loss, small coefficient

DeepSeek-V2-Lite, Sigma-MoE-Tiny

Aux loss, large coefficient

OLMoE, Switch

Loss-free bias

sigmoid scores, no aux loss: Wang et al.

Load per expert

1

2

3

4

5

6

7

8

mean load

expert

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

One token: router scoresrouter scorewhat the LM loss wants

\+ bias− bias, used only to pick experts

score

Overload (MaxVio): how far the busiest expert sits above the mean load

\+158%

step



\+300%

balanced

\+63%

\+25%

\+4%

Router distortion: share of router probability moved off what the LM loss wants

0%

step

40%

none

13%

35%

0%

Rerouted: share of selected experts outside the top-2 that the LM loss wants

0%

step

50%

none

29%

41%

48%

Measured in 1B runs with 64 experts, top-6, aux loss per sequence (Wang et al., 2024): validation-set overload, perplexity

α \= 0: ≈ \+507%, PPL ≈ 9.54

α \= 0.001: \+72%, PPL 9.56

α \= 0.01: ≈ \+10%, PPL ≈ 9.69

bias: \+4%, PPL 9.50

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

Step 40 of 40\. Both methods balance the load, each at a cost: the aux loss pulls router scores off what the LM wants, further at the large coefficient, while the bias leaves them in place but reroutes the most selections.

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Aux loss or loss-free bias: what does each give up to balance the load?

No balancing

LM loss only: no aux loss, no bias

Aux loss, small coefficient

DeepSeek-V2-Lite, Sigma-MoE-Tiny

Aux loss, large coefficient

OLMoE, Switch

Loss-free bias

sigmoid scores, no aux loss: Wang et al.

Load per expert

1

2

3

4

5

6

7

8

mean load

expert

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

One token: router scoresrouter scorewhat the LM loss wants

\+ bias− bias, used only to pick experts

score

Overload (MaxVio): how far the busiest expert sits above the mean load

\+154%

step



\+300%

balanced

Router distortion: share of router probability moved off what the LM loss wants

0%

step

40%

none

Rerouted: share of selected experts outside the top-2 that the LM loss wants

0%

step

50%

none

Measured in 1B runs with 64 experts, top-6, aux loss per sequence (Wang et al., 2024): validation-set overload, perplexity

α \= 0: ≈ \+507%, PPL ≈ 9.54

α \= 0.001: \+72%, PPL 9.56

α \= 0.01: ≈ \+10%, PPL ≈ 9.69

bias: \+4%, PPL 9.50

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

Step 1 of 40\. Each step routes the same batch. Without balancing the load stays piled on four experts; the aux loss changes router scores, while the bias changes only which experts are selected.

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Aux loss or loss-free bias: what does each give up to balance the load?

No balancing

LM loss only: no aux loss, no bias

Aux loss, small coefficient

DeepSeek-V2-Lite, Sigma-MoE-Tiny

Aux loss, large coefficient

OLMoE, Switch

Loss-free bias

sigmoid scores, no aux loss: Wang et al.

Load per expert

1

2

3

4

5

6

7

8

mean load

expert

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

One token: router scoresrouter scorewhat the LM loss wants

\+ bias− bias, used only to pick experts

score

Overload (MaxVio): how far the busiest expert sits above the mean load

\+150%

step



\+300%

balanced

Router distortion: share of router probability moved off what the LM loss wants

0%

step

40%

none

Rerouted: share of selected experts outside the top-2 that the LM loss wants

0%

step

50%

none

Measured in 1B runs with 64 experts, top-6, aux loss per sequence (Wang et al., 2024): validation-set overload, perplexity

α \= 0: ≈ \+507%, PPL ≈ 9.54

α \= 0.001: \+72%, PPL 9.56

α \= 0.01: ≈ \+10%, PPL ≈ 9.69

bias: \+4%, PPL 9.50

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

Step 1 of 40\. Each step routes the same batch. Without balancing the load stays piled on four experts; the aux loss changes router scores, while the bias changes only which experts are selected.

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

## Sample 6

Parameters: `{"t": 8.5}`

Aux loss or loss-free bias: what does each give up to balance the load?

No balancing

LM loss only: no aux loss, no bias

Aux loss, small coefficient

DeepSeek-V2-Lite, Sigma-MoE-Tiny

Aux loss, large coefficient

OLMoE, Switch

Loss-free bias

sigmoid scores, no aux loss: Wang et al.

Load per expert

1

2

3

4

5

6

7

8

mean load

expert

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

One token: router scoresrouter scorewhat the LM loss wants

\+ bias− bias, used only to pick experts

score

Overload (MaxVio): how far the busiest expert sits above the mean load

\+158%

step



\+300%

balanced

\+67%

\+33%

\+25%

Router distortion: share of router probability moved off what the LM loss wants

0%

step

40%

none

12%

38%

0%

Rerouted: share of selected experts outside the top-2 that the LM loss wants

0%

step

50%

none

28%

38%

46%

Measured in 1B runs with 64 experts, top-6, aux loss per sequence (Wang et al., 2024): validation-set overload, perplexity

α \= 0: ≈ \+507%, PPL ≈ 9.54

α \= 0.001: \+72%, PPL 9.56

α \= 0.01: ≈ \+10%, PPL ≈ 9.69

bias: \+4%, PPL 9.50

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.

Step 25 of 40\. Both methods balance the load, each at a cost: the aux loss pulls router scores off what the LM wants, further at the large coefficient, while the bias leaves them in place but reroutes the most selections.

The two coefficients and the bias step are set so that the final overloads follow the measured order in the last row, the bias step also so that this order shows by step 24\.
