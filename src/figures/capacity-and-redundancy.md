# capacity-and-redundancy

[Interactive original](../upstream/app/public/viz/index.html?c=capacity-and-redundancy) · [Poster](../upstream/app/public/viz/posters/capacity-and-redundancy.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/capacity-and-redundancy-BwkHD2LT.js)

## Controls

```json
{
  "cf": {
    "min": 1,
    "max": 2,
    "step": 0.25,
    "value": 1.25,
    "label": "capacity factor"
  },
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 7,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 13.1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 26 \= 1.63× mean

cost: 38% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 13.5

max 17 \= 1.26× mean

cost: 21% of rank time idle, 10 of 64 selections dropped (16%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 18 \= 1.13× mean

cost: 11% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

The whole batch: expert 1 stays the busiest, and each row deals with its overflow in its own way.

## Sample 2

Parameters: `{"t": 6.55}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 8.5

max 15 \= 1.76× mean

cost: 43% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 8.5

max 15 \= 1.76× mean

cost: 43% of rank time idle, 0 of 34 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 8.5

max 9 \= 1.06× mean

cost: 6% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

This token’s selection of expert 1 runs on the replica, so the original rank gets no work from it.

## Sample 3

Parameters: `{"t": 13.1}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 26 \= 1.63× mean

cost: 38% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 13.5

max 17 \= 1.26× mean

cost: 21% of rank time idle, 10 of 64 selections dropped (16%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 18 \= 1.13× mean

cost: 11% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

With every token in, the cap shortens the step by dropping selections, which changes the model’s output, while the replica balances the ranks with every selection kept, at the price of copying expert 1’s weights.

## Sample 4

Parameters: `{"cf": 1, "t": 0}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 26 \= 1.63× mean

cost: 38% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 12.5

max 15 \= 1.20× mean

cost: 17% of rank time idle, 14 of 64 selections dropped (22%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 18 \= 1.13× mean

cost: 11% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

The whole batch: expert 1 stays the busiest, and each row deals with its overflow in its own way.

## Sample 5

Parameters: `{"cf": 1.5, "t": 0}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 26 \= 1.63× mean

cost: 38% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 14

max 18 \= 1.29× mean

cost: 22% of rank time idle, 8 of 64 selections dropped (13%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 18 \= 1.13× mean

cost: 11% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

The whole batch: expert 1 stays the busiest, and each row deals with its overflow in its own way.

## Sample 6

Parameters: `{"cf": 1.75, "t": 0}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 26 \= 1.63× mean

cost: 38% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 14.5

max 20 \= 1.38× mean

cost: 28% of rank time idle, 6 of 64 selections dropped (9%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 18 \= 1.13× mean

cost: 11% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

The whole batch: expert 1 stays the busiest, and each row deals with its overflow in its own way.

## Sample 7

Parameters: `{"cf": 2, "t": 0}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 26 \= 1.63× mean

cost: 38% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 15

max 22 \= 1.47× mean

cost: 32% of rank time idle, 4 of 64 selections dropped (6%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 18 \= 1.13× mean

cost: 11% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

The whole batch: expert 1 stays the busiest, and each row deals with its overflow in its own way.

## Sample 8

Parameters: `{"seed": 1, "t": 0}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 29 \= 1.81× mean

cost: 45% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 12.3

max 18 \= 1.47× mean

cost: 32% of rank time idle, 15 of 64 selections dropped (23%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 18 \= 1.13× mean

cost: 11% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

The whole batch: expert 1 stays the busiest, and each row deals with its overflow in its own way.

## Sample 9

Parameters: `{"seed": 10.5, "t": 0}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 30 \= 1.88× mean

cost: 47% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 13.3

max 19 \= 1.43× mean

cost: 30% of rank time idle, 11 of 64 selections dropped (17%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 21 \= 1.31× mean

cost: 24% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

The whole batch: expert 1 stays the busiest, and each row deals with its overflow in its own way.

## Sample 10

Parameters: `{"seed": 20, "t": 0}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 29 \= 1.81× mean

cost: 45% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 12.8

max 18 \= 1.41× mean

cost: 29% of rank time idle, 13 of 64 selections dropped (20%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 16

max 18 \= 1.13× mean

cost: 11% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

The whole batch: expert 1 stays the busiest, and each row deals with its overflow in its own way.

## Sample 11

Parameters: `{"t": 1.5}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 0.5

max 1

cost: the other ranks wait for ranks 1 and 2

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 0.5

max 1

cost: the other ranks wait for ranks 1 and 2, 0 of 2 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 0.5

max 1

cost: the other ranks wait for ranks 1 and 2, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

Tokens arrive one at a time, and each sends its selections to the ranks that hold those experts.

## Sample 12

Parameters: `{"t": 2.1}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 1.5

max 3

cost: the other ranks wait for ranks 1 and 2

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 1.5

max 3

cost: the other ranks wait for ranks 1 and 2, 0 of 6 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 1.5

max 3

cost: the other ranks wait for rank 2, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

This token’s selection of expert 1 runs on the replica, so the original rank gets no work from it.

## Sample 13

Parameters: `{"t": 2.7}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 2.5

max 5

cost: the other ranks wait for rank 2

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 2.5

max 5

cost: the other ranks wait for rank 2, 0 of 10 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 2.5

max 5

cost: the other ranks wait for rank 2, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

Tokens arrive one at a time, and each sends its selections to the ranks that hold those experts.

## Sample 14

Parameters: `{"t": 3.9}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 4.5

max 8 \= 1.78× mean

cost: 44% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 4.5

max 8 \= 1.78× mean

cost: 44% of rank time idle, 0 of 18 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 4.5

max 5 \= 1.11× mean

cost: 10% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

This token’s selection of expert 1 runs on the replica, so the original rank gets no work from it.

## Sample 15

Parameters: `{"t": 4.5}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 5.5

max 10 \= 1.82× mean

cost: 45% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 5.5

max 10 \= 1.82× mean

cost: 45% of rank time idle, 0 of 22 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 5.5

max 6 \= 1.09× mean

cost: 8% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

Tokens arrive one at a time, and each sends its selections to the ranks that hold those experts.

## Sample 16

Parameters: `{"t": 4.9}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 6

max 11 \= 1.83× mean

cost: 45% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 6

max 11 \= 1.83× mean

cost: 45% of rank time idle, 0 of 24 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 6

max 6 \= 1.00× mean

cost: 0% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

This token’s selection of expert 1 runs on the replica, so the original rank gets no work from it.

## Sample 17

Parameters: `{"t": 5.2}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 6.5

max 12 \= 1.85× mean

cost: 46% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 6.5

max 12 \= 1.85× mean

cost: 46% of rank time idle, 0 of 26 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 6.5

max 7 \= 1.08× mean

cost: 7% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

Tokens arrive one at a time, and each sends its selections to the ranks that hold those experts.

## Sample 18

Parameters: `{"t": 6.7}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 9

max 15 \= 1.67× mean

cost: 40% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 9

max 15 \= 1.67× mean

cost: 40% of rank time idle, 0 of 36 selections dropped

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 9

max 10 \= 1.11× mean

cost: 10% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

Tokens arrive one at a time, and each sends its selections to the ranks that hold those experts.

## Sample 19

Parameters: `{"t": 7}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 9.5

max 16 \= 1.68× mean

cost: 41% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 9.3

max 15 \= 1.62× mean

cost: 38% of rank time idle, 1 of 38 selections dropped (3%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 9.5

max 11 \= 1.16× mean

cost: 14% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

One of this token’s experts is already full under the cap, so that selection is dropped.

## Sample 20

Parameters: `{"t": 8.2}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 11.5

max 19 \= 1.65× mean

cost: 39% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 10.5

max 15 \= 1.43× mean

cost: 30% of rank time idle, 4 of 46 selections dropped (9%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 11.5

max 13 \= 1.13× mean

cost: 12% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

Tokens arrive one at a time, and each sends its selections to the ranks that hold those experts.

## Sample 21

Parameters: `{"t": 8.5}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 12

max 20 \= 1.67× mean

cost: 40% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 10.8

max 15 \= 1.40× mean

cost: 28% of rank time idle, 5 of 48 selections dropped (10%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 12

max 13 \= 1.08× mean

cost: 8% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

One of this token’s experts is already full under the cap, so that selection is dropped.

## Sample 22

Parameters: `{"t": 9.1}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 13

max 21 \= 1.62× mean

cost: 38% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 11.5

max 15 \= 1.30× mean

cost: 23% of rank time idle, 6 of 52 selections dropped (12%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 13

max 15 \= 1.15× mean

cost: 13% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

Tokens arrive one at a time, and each sends its selections to the ranks that hold those experts.

## Sample 23

Parameters: `{"t": 9.4}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 13.5

max 22 \= 1.63× mean

cost: 39% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 11.8

max 15 \= 1.28× mean

cost: 22% of rank time idle, 7 of 54 selections dropped (13%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 13.5

max 15 \= 1.11× mean

cost: 10% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

One of this token’s experts is already full under the cap, so that selection is dropped.

## Sample 24

Parameters: `{"t": 9.7}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 14

max 22 \= 1.57× mean

cost: 36% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 12.3

max 16 \= 1.31× mean

cost: 23% of rank time idle, 7 of 56 selections dropped (13%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 14

max 16 \= 1.14× mean

cost: 13% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

Tokens arrive one at a time, and each sends its selections to the ranks that hold those experts.

## Sample 25

Parameters: `{"t": 10.3}`

How to handle a hot expert under expert parallelism

selections per expert, grouped by EP rank

selections per EP rank; the busiest (blue) sets the step time

this token’s selections earlier selectionsdropped selection

Dropless

no cap, variable-size expert batches (DeepSeek-V3, MegaBlocks)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 15

max 23 \= 1.53× mean

cost: 35% of rank time idle

UltraEP training, before balancing: 1.30 to 2.86× mean

Capacity factor

fixed expert capacity, overflow selections dropped in arrival order (GShard, Switch)

1

2

3

4

5

6

7

8

rank 1

rank 2

rank 3

rank 4

cap

1

2

3

4

mean 13

max 16 \= 1.23× mean

cost: 19% of rank time idle, 8 of 60 selections dropped (13%)

Pangu Ultra MoE paper: 6 to 8% dropped at cf 1.5

Dropless with a redundant expert

hot expert replicated on the idlest rank, selections sent to the less loaded replica (ECHO, Megatron Core report)

1

2

3

4

5

6

7

8

1′

rank 1

rank 2

rank 3

rank 4

1

2

3

4

mean 15

max 16 \= 1.07× mean

cost: 6% of rank time idle, a replica of expert 1’s weights

UltraEP training, after balancing: 1.01 to 1.03× mean

One of this token’s experts is already full under the cap, so that selection is dropped.
