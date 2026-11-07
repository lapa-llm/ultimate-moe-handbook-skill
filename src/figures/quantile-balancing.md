# quantile-balancing

[Interactive original](../upstream/app/public/viz/index.html?c=quantile-balancing) · [Poster](../upstream/app/public/viz/posters/quantile-balancing.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/quantile-balancing-Cg15MWEq.js)

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

Animation duration: 20.1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+158%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+158%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 2

Parameters: `{"t": 10.05}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+67%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 9\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 3

Parameters: `{"t": 20.1}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+25%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 16\. On this repeated batch the sign update still leaves the busiest expert \+25% above the mean load, while quantile balancing ends at \+8%: the solved bias needs no step size to tune, and Kimi K3 switched to it when the sign update stopped balancing its 896 experts stably.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 4

Parameters: `{"t": 0, "tokens": 16}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

one column per expert, 16 experts

\+175%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

one column per expert, 16 experts

\+175%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 5

Parameters: `{"t": 0, "tokens": 32}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+150%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+150%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 6

Parameters: `{"t": 0, "tokens": 64}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+144%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+144%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 7

Parameters: `{"t": 0, "tokens": 128}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+138%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+138%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 8

Parameters: `{"t": 0, "tokens": 144}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+147%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+147%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 9

Parameters: `{"t": 0, "tokens": 160}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+145%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+145%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 10

Parameters: `{"seed": 1, "t": 0}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+217%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+217%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 11

Parameters: `{"seed": 10.5, "t": 0}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+167%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+167%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 12

Parameters: `{"seed": 20, "t": 0}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+175%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+175%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 0\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 13

Parameters: `{"t": 0.9}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+148%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+83%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 1\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 14

Parameters: `{"t": 2}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+136%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+25%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 2\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 15

Parameters: `{"t": 3.1}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+128%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+11%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 3\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 16

Parameters: `{"t": 4.2}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+120%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 4\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 17

Parameters: `{"t": 5.3}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+111%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 5\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 18

Parameters: `{"t": 6.4}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+103%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 6\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 19

Parameters: `{"t": 7.5}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+95%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 7\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 20

Parameters: `{"t": 8.6}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+86%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 8\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 21

Parameters: `{"t": 9.7}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+73%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 9\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 22

Parameters: `{"t": 10.8}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+61%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 10\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 23

Parameters: `{"t": 11.9}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+42%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 11\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 24

Parameters: `{"t": 13}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+28%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 12\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 25

Parameters: `{"t": 14.1}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+25%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 13\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 26

Parameters: `{"t": 15.2}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+25%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 14\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 27

Parameters: `{"t": 16.3}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+25%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 15\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

## Sample 28

Parameters: `{"t": 17.4}`

Sign update or quantile balancing: which balances expert load faster?

Sign update (loss-free)

a fixed amount per update: Kimi K2

one dot per token; the joined dots are one token

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+25%

step

overload

balanced

worst case \+300%

Quantile balancing

the bias solved from the batch: Kimi K3

score \+ bias − cutoff

cutoff

mean

load

one column per expert, 16 experts

\+8%

step

overload

balanced

worst case \+300%

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.

Step 16\. Each step routes the same tokens, then each panel updates its biases: by a fixed amount, or solved from the batch.

A dot is one token’s score plus the expert’s bias, minus that token’s cutoff; an expert’s load is its dots above the line.
