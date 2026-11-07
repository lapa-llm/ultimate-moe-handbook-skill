# cluster-optimal-sparsity

[Interactive original](../upstream/app/public/viz/index.html?c=cluster-optimal-sparsity) · [Poster](../upstream/app/public/viz/posters/cluster-optimal-sparsity.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/cluster-optimal-sparsity-BVAbzF8s.js)

## Controls

```json
{
  "state": {
    "min": 1,
    "max": 3,
    "step": 1,
    "value": 3,
    "label": "Animation step",
    "wide": true
  }
}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Compute-optimal or cluster-optimal: how sparse should an MoE be?

Predicted training loss at a fixed 3.3×10²¹ model FLOPs

1.58

1.62

1.66

0.80

0.85

0.90

0.95

1.00

sparsity S

compute optimum

Predicted model FLOPs delivered in 5 days

10²¹

10²²

0.80

0.85

0.90

0.95

1.00

sparsity S

budget 3.3×10²¹

short of the budget past S \= 0.96

Predicted training loss after 5 days on the cluster

1.58

1.62

1.66

0.80

0.85

0.90

0.95

1.00

sparsity S

\+0.031 nats

cluster optimum, S ≈ 0.90

Sparsity: the share of parameters a token does not use. Every point is a prediction from Sarkar et al.’s MOSAIC study for one cluster of 4 AWS B200 nodes.

Fixed cluster time. With the cluster’s time as the budget, the best sparsity moves inside the range and ends 0.031 nats below the sparsest model, so choosing sparsity by model FLOPs alone costs loss on a fixed cluster.

Sparsity: the share of parameters a token does not use. Every point is a prediction from Sarkar et al.’s MOSAIC study for one cluster of 4 AWS B200 nodes.

## Sample 2

Parameters: `{"state": 1, "t": 0}`

Compute-optimal or cluster-optimal: how sparse should an MoE be?

Predicted training loss at a fixed 3.3×10²¹ model FLOPs

1.58

1.62

1.66

0.80

0.85

0.90

0.95

1.00

sparsity S

compute optimum

Predicted model FLOPs delivered in 5 days

10²¹

10²²

0.80

0.85

0.90

0.95

1.00

sparsity S

budget 3.3×10²¹

short of the budget past S \= 0.96

Predicted training loss after 5 days on the cluster

1.58

1.62

1.66

0.80

0.85

0.90

0.95

1.00

sparsity S

\+0.031 nats

cluster optimum, S ≈ 0.90

Sparsity: the share of parameters a token does not use. Every point is a prediction from Sarkar et al.’s MOSAIC study for one cluster of 4 AWS B200 nodes.

Fixed model FLOPs. At a fixed compute budget, the predicted loss keeps falling as the model gets sparser.

Sparsity: the share of parameters a token does not use. Every point is a prediction from Sarkar et al.’s MOSAIC study for one cluster of 4 AWS B200 nodes.

## Sample 3

Parameters: `{"state": 2, "t": 0}`

Compute-optimal or cluster-optimal: how sparse should an MoE be?

Predicted training loss at a fixed 3.3×10²¹ model FLOPs

1.58

1.62

1.66

0.80

0.85

0.90

0.95

1.00

sparsity S

compute optimum

Predicted model FLOPs delivered in 5 days

10²¹

10²²

0.80

0.85

0.90

0.95

1.00

sparsity S

budget 3.3×10²¹

short of the budget past S \= 0.96

Predicted training loss after 5 days on the cluster

1.58

1.62

1.66

0.80

0.85

0.90

0.95

1.00

sparsity S

\+0.031 nats

cluster optimum, S ≈ 0.90

Sparsity: the share of parameters a token does not use. Every point is a prediction from Sarkar et al.’s MOSAIC study for one cluster of 4 AWS B200 nodes.

Model FLOPs the cluster delivers. The sparsest models run less efficiently, so the cluster cannot give them that budget in time.

Sparsity: the share of parameters a token does not use. Every point is a prediction from Sarkar et al.’s MOSAIC study for one cluster of 4 AWS B200 nodes.
