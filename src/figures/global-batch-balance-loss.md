# global-batch-balance-loss

[Interactive original](../upstream/app/public/viz/index.html?c=global-batch-balance-loss) · [Poster](../upstream/app/public/viz/posters/global-batch-balance-loss.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/global-batch-balance-loss-DtkrHtam.js)

## Controls

```json
{
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

Animation duration: 16 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Load-balancing scope: experts per domain, or even load per GPU?

Sequence-wise loss fi counted over each sequence: DeepSeek-V2-Lite

node 1

node 2

GPU 1

load 1.00× mean

code

math

1

2

3

4

GPU 2

load 1.00× mean

math

prose

5

6

7

8

GPU 3

load 0.99× mean

prose

chat

1

2

3

4

GPU 4

load 1.01× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 25% of selections on experts 1, 2

each expert’s load, mean of both nodes

1

2

3

4

5

6

7

8

mean load

Micro-batch loss fi counted on each GPU’s own tokens: Switch Transformer

GPU 1

load 1.00× mean

code

math

1

2

3

4

GPU 2

load 1.00× mean

math

prose

5

6

7

8

GPU 3

load 0.99× mean

prose

chat

1

2

3

4

GPU 4

load 1.01× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 25% of selections on experts 1, 2

1

2

3

4

5

6

7

8

Global-batch loss fi all-reduced over the 4 GPUs: Qwen3, Mellum2

GPU 1

load 1.00× mean

code

math

1

2

3

4

GPU 2

load 1.00× mean

math

prose

5

6

7

8

GPU 3

load 0.99× mean

prose

chat

1

2

3

4

GPU 4

load 1.01× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 25% of selections on experts 1, 2

1

2

3

4

5

6

7

8

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

Step 1 of 40\. Each step trains the same loss in every row; only where expert load is counted differs.

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

## Sample 2

Parameters: `{"t": 8}`

Load-balancing scope: experts per domain, or even load per GPU?

Sequence-wise loss fi counted over each sequence: DeepSeek-V2-Lite

node 1

node 2

GPU 1

load 1.08× mean

code

math

1

2

3

4

GPU 2

load 0.92× mean

math

prose

5

6

7

8

GPU 3

load 0.88× mean

prose

chat

1

2

3

4

GPU 4

load 1.12× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 38% of selections on experts 1, 2

each expert’s load, mean of both nodes

1

2

3

4

5

6

7

8

mean load

Micro-batch loss fi counted on each GPU’s own tokens: Switch Transformer

GPU 1

load 1.14× mean

code

math

1

2

3

4

GPU 2

load 0.86× mean

math

prose

5

6

7

8

GPU 3

load 0.85× mean

prose

chat

1

2

3

4

GPU 4

load 1.15× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 59% of selections on experts 1, 2

1

2

3

4

5

6

7

8

Global-batch loss fi all-reduced over the 4 GPUs: Qwen3, Mellum2

GPU 1

load 1.46× mean

code

math

1

2

3

4

GPU 2

load 0.54× mean

math

prose

5

6

7

8

GPU 3

load 0.54× mean

prose

chat

1

2

3

4

GPU 4

load 1.46× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 93% of selections on experts 1, 2

1

2

3

4

5

6

7

8

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

Step 23 of 40\. Every row keeps each expert’s load over both nodes near even, but only the global-batch loss keeps nearly all of GPU 1’s code sequence on experts 1 and 2, at the price of the most uneven load per GPU.

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

## Sample 3

Parameters: `{"t": 16}`

Load-balancing scope: experts per domain, or even load per GPU?

Sequence-wise loss fi counted over each sequence: DeepSeek-V2-Lite

node 1

node 2

GPU 1

load 1.12× mean

code

math

1

2

3

4

GPU 2

load 0.88× mean

math

prose

5

6

7

8

GPU 3

load 0.90× mean

prose

chat

1

2

3

4

GPU 4

load 1.10× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 40% of selections on experts 1, 2

each expert’s load, mean of both nodes

1

2

3

4

5

6

7

8

mean load

Micro-batch loss fi counted on each GPU’s own tokens: Switch Transformer

GPU 1

load 1.12× mean

code

math

1

2

3

4

GPU 2

load 0.88× mean

math

prose

5

6

7

8

GPU 3

load 0.87× mean

prose

chat

1

2

3

4

GPU 4

load 1.13× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 62% of selections on experts 1, 2

1

2

3

4

5

6

7

8

Global-batch loss fi all-reduced over the 4 GPUs: Qwen3, Mellum2

GPU 1

load 1.46× mean

code

math

1

2

3

4

GPU 2

load 0.54× mean

math

prose

5

6

7

8

GPU 3

load 0.54× mean

prose

chat

1

2

3

4

GPU 4

load 1.46× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 94% of selections on experts 1, 2

1

2

3

4

5

6

7

8

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

Step 40 of 40\. Every row keeps each expert’s load over both nodes near even, but only the global-batch loss keeps nearly all of GPU 1’s code sequence on experts 1 and 2, at the price of the most uneven load per GPU.

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Load-balancing scope: experts per domain, or even load per GPU?

Sequence-wise loss fi counted over each sequence: DeepSeek-V2-Lite

node 1

node 2

GPU 1

load 1.01× mean

code

math

1

2

3

4

GPU 2

load 0.99× mean

math

prose

5

6

7

8

GPU 3

load 1.01× mean

prose

chat

1

2

3

4

GPU 4

load 0.99× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 26% of selections on experts 1, 2

each expert’s load, mean of both nodes

1

2

3

4

5

6

7

8

mean load

Micro-batch loss fi counted on each GPU’s own tokens: Switch Transformer

GPU 1

load 1.01× mean

code

math

1

2

3

4

GPU 2

load 0.99× mean

math

prose

5

6

7

8

GPU 3

load 1.01× mean

prose

chat

1

2

3

4

GPU 4

load 0.99× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 26% of selections on experts 1, 2

1

2

3

4

5

6

7

8

Global-batch loss fi all-reduced over the 4 GPUs: Qwen3, Mellum2

GPU 1

load 1.01× mean

code

math

1

2

3

4

GPU 2

load 0.99× mean

math

prose

5

6

7

8

GPU 3

load 1.01× mean

prose

chat

1

2

3

4

GPU 4

load 0.99× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 26% of selections on experts 1, 2

1

2

3

4

5

6

7

8

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

Step 1 of 40\. Each step trains the same loss in every row; only where expert load is counted differs.

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Load-balancing scope: experts per domain, or even load per GPU?

Sequence-wise loss fi counted over each sequence: DeepSeek-V2-Lite

node 1

node 2

GPU 1

load 0.99× mean

code

math

1

2

3

4

GPU 2

load 1.01× mean

math

prose

5

6

7

8

GPU 3

load 0.98× mean

prose

chat

1

2

3

4

GPU 4

load 1.02× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 24% of selections on experts 1, 2

each expert’s load, mean of both nodes

1

2

3

4

5

6

7

8

mean load

Micro-batch loss fi counted on each GPU’s own tokens: Switch Transformer

GPU 1

load 0.99× mean

code

math

1

2

3

4

GPU 2

load 1.01× mean

math

prose

5

6

7

8

GPU 3

load 0.98× mean

prose

chat

1

2

3

4

GPU 4

load 1.02× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 24% of selections on experts 1, 2

1

2

3

4

5

6

7

8

Global-batch loss fi all-reduced over the 4 GPUs: Qwen3, Mellum2

GPU 1

load 0.99× mean

code

math

1

2

3

4

GPU 2

load 1.01× mean

math

prose

5

6

7

8

GPU 3

load 0.98× mean

prose

chat

1

2

3

4

GPU 4

load 1.02× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 24% of selections on experts 1, 2

1

2

3

4

5

6

7

8

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

Step 1 of 40\. Each step trains the same loss in every row; only where expert load is counted differs.

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

## Sample 6

Parameters: `{"seed": 20, "t": 0}`

Load-balancing scope: experts per domain, or even load per GPU?

Sequence-wise loss fi counted over each sequence: DeepSeek-V2-Lite

node 1

node 2

GPU 1

load 1.00× mean

code

math

1

2

3

4

GPU 2

load 1.00× mean

math

prose

5

6

7

8

GPU 3

load 0.98× mean

prose

chat

1

2

3

4

GPU 4

load 1.02× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 25% of selections on experts 1, 2

each expert’s load, mean of both nodes

1

2

3

4

5

6

7

8

mean load

Micro-batch loss fi counted on each GPU’s own tokens: Switch Transformer

GPU 1

load 1.00× mean

code

math

1

2

3

4

GPU 2

load 1.00× mean

math

prose

5

6

7

8

GPU 3

load 0.98× mean

prose

chat

1

2

3

4

GPU 4

load 1.02× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 25% of selections on experts 1, 2

1

2

3

4

5

6

7

8

Global-batch loss fi all-reduced over the 4 GPUs: Qwen3, Mellum2

GPU 1

load 1.00× mean

code

math

1

2

3

4

GPU 2

load 1.00× mean

math

prose

5

6

7

8

GPU 3

load 0.98× mean

prose

chat

1

2

3

4

GPU 4

load 1.02× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 25% of selections on experts 1, 2

1

2

3

4

5

6

7

8

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

Step 1 of 40\. Each step trains the same loss in every row; only where expert load is counted differs.

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

## Sample 7

Parameters: `{"t": 3.9}`

Load-balancing scope: experts per domain, or even load per GPU?

Sequence-wise loss fi counted over each sequence: DeepSeek-V2-Lite

node 1

node 2

GPU 1

load 1.13× mean

code

math

1

2

3

4

GPU 2

load 0.87× mean

math

prose

5

6

7

8

GPU 3

load 0.91× mean

prose

chat

1

2

3

4

GPU 4

load 1.09× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 40% of selections on experts 1, 2

each expert’s load, mean of both nodes

1

2

3

4

5

6

7

8

mean load

Micro-batch loss fi counted on each GPU’s own tokens: Switch Transformer

GPU 1

load 1.15× mean

code

math

1

2

3

4

GPU 2

load 0.85× mean

math

prose

5

6

7

8

GPU 3

load 0.85× mean

prose

chat

1

2

3

4

GPU 4

load 1.15× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 59% of selections on experts 1, 2

1

2

3

4

5

6

7

8

Global-batch loss fi all-reduced over the 4 GPUs: Qwen3, Mellum2

GPU 1

load 1.44× mean

code

math

1

2

3

4

GPU 2

load 0.56× mean

math

prose

5

6

7

8

GPU 3

load 0.58× mean

prose

chat

1

2

3

4

GPU 4

load 1.42× mean

chat

code

5

6

7

8

GPU 1’s code sequence: 90% of selections on experts 1, 2

1

2

3

4

5

6

7

8

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.

Step 12 of 40\. Every row keeps each expert’s load over both nodes near even, but only the global-batch loss keeps nearly all of GPU 1’s code sequence on experts 1 and 2, at the price of the most uneven load per GPU.

The LM loss favours two experts per domain, and each node holds one domain twice, whose two favourites sit on one GPU.
