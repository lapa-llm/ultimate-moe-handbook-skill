# hero-anatomy-zoom

[Interactive original](../upstream/app/public/viz/index.html?c=hero-anatomy-zoom) · [Poster](../upstream/app/public/viz/posters/hero-anatomy-zoom.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/hero-anatomy-zoom-BJ3pyKeL.js)

## Controls

```json
{
  "stage": {
    "min": 0,
    "max": 8,
    "step": 1,
    "value": 0,
    "hidden": true
  },
  "mini": {
    "min": 0,
    "max": 1,
    "step": 1,
    "value": 0,
    "hidden": true
  }
}
```

Animation duration: 76.49393822393823 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

A router sends each token to a few of the experts.

## Sample 2

Parameters: `{"t": 38.246969111969115}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

Σ

attention

all-to-all

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Usually the MoE waits for attention’s output.

## Sample 3

Parameters: `{"t": 76.49393822393823}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Every part has its own section in this chapter: click one to go there.

## Sample 4

Parameters: `{"stage": 2, "t": 0}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

top-4

score

weight

.28

.26

.23

.23

one bar per expert

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Those scores are renormalized into the weights for the experts’ outputs.

## Sample 5

Parameters: `{"stage": 3, "t": 0}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Some experts receive picks from many tokens.

## Sample 6

Parameters: `{"stage": 4, "t": 0}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

mean over all experts

Σ

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

The busiest expert sits far above the mean, and its GPU sets the step time.

## Sample 7

Parameters: `{"stage": 5, "t": 0}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

up

activation

down

shared expert

routed expert

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Experts (3.4)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Each expert is a small MLP; a shared one runs on every token, a routed one only on the tokens that pick it.

## Sample 8

Parameters: `{"stage": 6, "t": 0}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

Σ

attention

all-to-all

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Other layouts overlap communication with compute: reading the block’s input, the MoE sends its tokens while attention computes.

## Sample 9

Parameters: `{"stage": 7, "t": 0}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

Σ

output norm

median

dead

rogue

loss

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Training (3.6)

Here one expert’s norm falls to zero and another’s climbs far above the median, yet the loss gives no signal of either, as with Step 3.5 Flash’s rogue experts.

## Sample 10

Parameters: `{"stage": 8, "t": 0}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

Σ

output

node 1

node 2

GPU 1

GPU 2

GPU 3

GPU 4

GPU 5

GPU 6

GPU 7

GPU 8

shared expert

slower link between nodes

NVLink

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Experts (3.4)

Block layout (3.5)

The shared expert needs no copy: it runs on the token’s own GPU, and its output joins the same sum.

## Sample 11

Parameters: `{"mini": 1, "t": 0}`

tokens

router

shared expert

routed experts

Σ

output

A router sends each token to a few of the experts.

## Sample 12

Parameters: `{"t": 2.8}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

The router scores every routed expert for the blue token and keeps the top 4\.

## Sample 13

Parameters: `{"t": 12.3}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Each token picks its own experts, independently of the others.

## Sample 14

Parameters: `{"t": 20.4}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Each square is one token’s pick, stacked in the expert it went to.

## Sample 15

Parameters: `{"t": 28.8}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Experts (3.4)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Each expert is a small MLP; a shared one runs on every token, a routed one only on the tokens that pick it.

## Sample 16

Parameters: `{"t": 34.5}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Usually the MoE waits for attention’s output.

## Sample 17

Parameters: `{"t": 45.1}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Training (3.6)

While training runs, every expert’s output norm should stay near the layer’s median.

## Sample 18

Parameters: `{"t": 49.8}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

Σ

output norm

median

dead

loss

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Block layout (3.5)

Training (3.6)

Here one expert’s norm falls to zero and another’s climbs far above the median, yet the loss gives no signal of either, as with Step 3.5 Flash’s rogue experts.

## Sample 19

Parameters: `{"t": 57}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

shared expert

routed experts

Σ

output

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Experts (3.4)

Block layout (3.5)

A copy of the token travels to each GPU that holds one of its experts.

## Sample 20

Parameters: `{"t": 61}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

Σ

output

node 1

node 2

GPU 1

GPU 2

GPU 3

GPU 4

GPU 5

GPU 6

GPU 7

GPU 8

slower link between nodes

NVLink

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Experts (3.4)

Block layout (3.5)

Copies for the other node cross the slower link between nodes.

## Sample 21

Parameters: `{"t": 63.8}`

Chapter 3 at a glance

Layer3.13.23.33.43.53.63.7

tokens

router

Σ

output

node 1

node 2

GPU 1

GPU 2

GPU 3

GPU 4

GPU 5

GPU 6

GPU 7

GPU 8

slower link between nodes

NVLink

Router scoring (3.1)

Routing strategy (3.2)

Load balancing (3.3)

Experts (3.4)

Systems (3.7)

Experts (3.4)

Block layout (3.5)

The routed experts’ outputs come back the same way and are summed on the token’s GPU.
