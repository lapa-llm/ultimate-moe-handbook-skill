# device-level-balance-loss

[Interactive original](../upstream/app/public/viz/index.html?c=device-level-balance-loss) · [Poster](../upstream/app/public/viz/posters/device-level-balance-loss.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/device-level-balance-loss-BCohHM-q.js)

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

Expert-level or device-level balance loss: which moves the router less?

No balancing

LM loss only

Expert-level loss

OLMoE, Switch

Device-level loss

DeepSeekMoE 145B, DeepSeek-V2

Load per GPU: a training step waits for the busiest GPU

busiest GPU 1.33× mean

GPU 1

GPU 2

GPU 3

GPU 4

mean load

GPU 1

GPU 2

GPU 3

GPU 4

GPU 1

GPU 2

GPU 3

GPU 4

Load per expert, framed by the GPU that hosts it

busiest expert 2.58× mean

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

One token: router probabilitiesrouter probabilitywhat the LM loss wants

prob

Router distortion: share of router probability moved off what the LM loss wants

step

40%

none

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

Step 1 of 40\. Each step routes the same batch with no balancing, with a loss that counts load per expert, or with one that counts it per GPU.

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

## Sample 2

Parameters: `{"t": 8}`

Expert-level or device-level balance loss: which moves the router less?

No balancing

LM loss only

Expert-level loss

OLMoE, Switch

Device-level loss

DeepSeekMoE 145B, DeepSeek-V2

Load per GPU: a training step waits for the busiest GPU

busiest GPU 1.33× mean

GPU 1

GPU 2

GPU 3

GPU 4

mean load

busiest GPU 1.06× mean

GPU 1

GPU 2

GPU 3

GPU 4

busiest GPU 1.08× mean

GPU 1

GPU 2

GPU 3

GPU 4

Load per expert, framed by the GPU that hosts it

busiest expert 2.58× mean

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

busiest expert 1.38× mean

1

2

3

4

5

6

7

8

busiest expert 2.13× mean

1

2

3

4

5

6

7

8

One token: router probabilitiesrouter probabilitywhat the LM loss wants

prob

Router distortion: share of router probability moved off what the LM loss wants

step

40%

none

38%

11%

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

Step 23 of 40\. Both losses balance the GPUs; the device-level loss, which sees only each GPU’s total, moves the router less but leaves the experts within each GPU uneven.

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

## Sample 3

Parameters: `{"t": 16}`

Expert-level or device-level balance loss: which moves the router less?

No balancing

LM loss only

Expert-level loss

OLMoE, Switch

Device-level loss

DeepSeekMoE 145B, DeepSeek-V2

Load per GPU: a training step waits for the busiest GPU

busiest GPU 1.33× mean

GPU 1

GPU 2

GPU 3

GPU 4

mean load

busiest GPU 1.04× mean

GPU 1

GPU 2

GPU 3

GPU 4

busiest GPU 1.08× mean

GPU 1

GPU 2

GPU 3

GPU 4

Load per expert, framed by the GPU that hosts it

busiest expert 2.58× mean

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

busiest expert 1.25× mean

1

2

3

4

5

6

7

8

busiest expert 2.17× mean

1

2

3

4

5

6

7

8

One token: router probabilitiesrouter probabilitywhat the LM loss wants

prob

Router distortion: share of router probability moved off what the LM loss wants

step

40%

none

35%

11%

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

Step 40 of 40\. Both losses balance the GPUs; the device-level loss, which sees only each GPU’s total, moves the router less but leaves the experts within each GPU uneven.

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Expert-level or device-level balance loss: which moves the router less?

No balancing

LM loss only

Expert-level loss

OLMoE, Switch

Device-level loss

DeepSeekMoE 145B, DeepSeek-V2

Load per GPU: a training step waits for the busiest GPU

busiest GPU 1.31× mean

GPU 1

GPU 2

GPU 3

GPU 4

mean load

GPU 1

GPU 2

GPU 3

GPU 4

GPU 1

GPU 2

GPU 3

GPU 4

Load per expert, framed by the GPU that hosts it

busiest expert 2.54× mean

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

One token: router probabilitiesrouter probabilitywhat the LM loss wants

prob

Router distortion: share of router probability moved off what the LM loss wants

step

40%

none

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

Step 1 of 40\. Each step routes the same batch with no balancing, with a loss that counts load per expert, or with one that counts it per GPU.

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Expert-level or device-level balance loss: which moves the router less?

No balancing

LM loss only

Expert-level loss

OLMoE, Switch

Device-level loss

DeepSeekMoE 145B, DeepSeek-V2

Load per GPU: a training step waits for the busiest GPU

busiest GPU 1.29× mean

GPU 1

GPU 2

GPU 3

GPU 4

mean load

GPU 1

GPU 2

GPU 3

GPU 4

GPU 1

GPU 2

GPU 3

GPU 4

Load per expert, framed by the GPU that hosts it

busiest expert 2.50× mean

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

One token: router probabilitiesrouter probabilitywhat the LM loss wants

prob

Router distortion: share of router probability moved off what the LM loss wants

step

40%

none

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

Step 1 of 40\. Each step routes the same batch with no balancing, with a loss that counts load per expert, or with one that counts it per GPU.

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

## Sample 6

Parameters: `{"seed": 20, "t": 0}`

Expert-level or device-level balance loss: which moves the router less?

No balancing

LM loss only

Expert-level loss

OLMoE, Switch

Device-level loss

DeepSeekMoE 145B, DeepSeek-V2

Load per GPU: a training step waits for the busiest GPU

busiest GPU 1.31× mean

GPU 1

GPU 2

GPU 3

GPU 4

mean load

GPU 1

GPU 2

GPU 3

GPU 4

GPU 1

GPU 2

GPU 3

GPU 4

Load per expert, framed by the GPU that hosts it

busiest expert 2.50× mean

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

One token: router probabilitiesrouter probabilitywhat the LM loss wants

prob

Router distortion: share of router probability moved off what the LM loss wants

step

40%

none

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

Step 1 of 40\. Each step routes the same batch with no balancing, with a loss that counts load per expert, or with one that counts it per GPU.

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

## Sample 7

Parameters: `{"t": 1.8}`

Expert-level or device-level balance loss: which moves the router less?

No balancing

LM loss only

Expert-level loss

OLMoE, Switch

Device-level loss

DeepSeekMoE 145B, DeepSeek-V2

Load per GPU: a training step waits for the busiest GPU

busiest GPU 1.33× mean

GPU 1

GPU 2

GPU 3

GPU 4

mean load

busiest GPU 1.02× mean

GPU 1

GPU 2

GPU 3

GPU 4

busiest GPU 1.08× mean

GPU 1

GPU 2

GPU 3

GPU 4

Load per expert, framed by the GPU that hosts it

busiest expert 2.58× mean

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

busiest expert 1.38× mean

1

2

3

4

5

6

7

8

busiest expert 2.08× mean

1

2

3

4

5

6

7

8

One token: router probabilitiesrouter probabilitywhat the LM loss wants

prob

Router distortion: share of router probability moved off what the LM loss wants

step

40%

none

21%

9%

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.

Step 6 of 40\. Both losses balance the GPUs; the device-level loss, which sees only each GPU’s total, moves the router less but leaves the experts within each GPU uneven.

Both losses run at one coefficient, standing for 0.01, and each GPU holds one of the four experts the LM favours. Which loss balances the GPUs better depends on that coefficient: with both weaker, the device-level loss balances them worse than the expert-level one, while still moving the router less. DeepSeekMoE 145B and DeepSeek-V2 run the device-level loss at 0.05, beside an expert-level loss at 0.003, and Step 3.5 Flash at 0.001, beside a loss-free bias.
