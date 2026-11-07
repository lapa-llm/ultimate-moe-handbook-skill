# aux-loss-free-bias

[Interactive original](../upstream/app/public/viz/index.html?c=aux-loss-free-bias) · [Poster](../upstream/app/public/viz/posters/aux-loss-free-bias.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/aux-loss-free-bias-CLfvScbv.js)

## Controls

```json
{
  "tokens": {
    "min": 16,
    "max": 160,
    "step": 16,
    "value": 48,
    "label": "tokens per batch",
    "hidden": true
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

Animation duration: 29.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+158%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 2

Parameters: `{"t": 14.75}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.28

.22

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 16\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 3

Parameters: `{"t": 29.5}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 30\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 4

Parameters: `{"t": 0, "tokens": 16}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.25

.27

.24

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (16 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+175%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 5

Parameters: `{"t": 0, "tokens": 32}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.25

.26

.25

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (32 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+150%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 6

Parameters: `{"t": 0, "tokens": 64}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.28

.26

.23

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (64 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+144%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 7

Parameters: `{"t": 0, "tokens": 80}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.28

.23

.23

.25

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (80 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+150%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 8

Parameters: `{"t": 0, "tokens": 96}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.23

.24

.25

.28

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (96 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+158%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 9

Parameters: `{"t": 0, "tokens": 112}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.26

.26

.25

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (112 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+150%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 10

Parameters: `{"t": 0, "tokens": 128}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.26

.24

.26

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (128 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+138%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 11

Parameters: `{"t": 0, "tokens": 144}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.23

.26

.25

.26

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (144 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+147%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 12

Parameters: `{"t": 0, "tokens": 160}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.25

.26

.25

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (160 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+145%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 13

Parameters: `{"seed": 1, "t": 0}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.27

.24

.24

.25

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+217%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 14

Parameters: `{"seed": 10.5, "t": 0}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.28

.24

.23

.25

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+167%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 15

Parameters: `{"seed": 20, "t": 0}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.23

.26

.27

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+175%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 0\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 16

Parameters: `{"t": 0.8}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+143%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 1\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 17

Parameters: `{"t": 1.7}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+134%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 2\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 18

Parameters: `{"t": 2.6}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.28

.22

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+125%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 3\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 19

Parameters: `{"t": 3.5}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+117%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 4\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 20

Parameters: `{"t": 4.4}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.28

.22

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+109%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 5\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 21

Parameters: `{"t": 5.3}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+100%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 6\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 22

Parameters: `{"t": 6.2}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+92%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 7\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 23

Parameters: `{"t": 7.1}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+84%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 8\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 24

Parameters: `{"t": 8}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+68%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 9\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 25

Parameters: `{"t": 8.9}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+59%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 10\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 26

Parameters: `{"t": 9.8}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+35%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 11\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 27

Parameters: `{"t": 10.7}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+25%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 12\. After each step, overloaded experts lower their bias and underloaded ones raise it by a fixed amount, which moves tokens like the one above onto less loaded experts.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 28

Parameters: `{"t": 10.9}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+25%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 12\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 29

Parameters: `{"t": 11.6}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+17%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 13\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 30

Parameters: `{"t": 12.5}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+17%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 14\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 31

Parameters: `{"t": 13.4}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+9%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 15\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 32

Parameters: `{"t": 15.2}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 17\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 33

Parameters: `{"t": 16.1}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.28

.22

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 18\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 34

Parameters: `{"t": 17}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 19\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 35

Parameters: `{"t": 17.9}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+16%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 20\. Partway through, each bias moves a tenth as far per step, as Ling 2.0 does after context extension, which damps the back-and-forth.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 36

Parameters: `{"t": 18.1}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+17%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 20\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 37

Parameters: `{"t": 18.8}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+9%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 21\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 38

Parameters: `{"t": 19.7}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 22\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 39

Parameters: `{"t": 20.6}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 23\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 40

Parameters: `{"t": 21.5}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 24\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 41

Parameters: `{"t": 22.4}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 25\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 42

Parameters: `{"t": 23.3}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 26\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 43

Parameters: `{"t": 24.2}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 27\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 44

Parameters: `{"t": 25.1}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.28

.23

.24

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 28\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step

## Sample 45

Parameters: `{"t": 26}`

How to balance expert load without an auxiliary loss?

one token’s router scores

.24

.26

.27

.23

top-4

score

score

\+ bias

− bias

weight

the batch: each dot is one selection (48 tokens × top-4), the token above in blue

bias

mean load

one column per expert, 16 experts

\+8%

step

worst case \+300% (6 of 64: \+967%)

aux loss: \+72% (Wang et al. 1B)

loss-free: \+10%

overload

balanced

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

Step 29\. The overload settles near the loss-free level Wang et al. measured, far below their aux loss’s, while only the LM loss trains the router.

Overload: how far the busiest expert sits above the mean load. The same batch repeats every step.

next step
