# sequence-wise-aux-complement

[Interactive original](../upstream/app/public/viz/index.html?c=sequence-wise-aux-complement) · [Poster](../upstream/app/public/viz/posters/sequence-wise-aux-complement.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/sequence-wise-aux-complement-BxpFwhWq.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 2,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 15.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How large a sequence-wise aux loss should complement the loss-free bias?

Bias only

loss-free bias on batch counts, no loss

\+ small sequence-wise loss

small coefficient: weak gradient

\+ large sequence-wise loss

large coefficient: strong gradient

An ordinary sequencemildly uneven, like the rest of the batch

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+117%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+50%

6%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+33%

11%

An extreme sequencethe LM wants almost all of it on expert 3

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+300%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+300%

12%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+100%

71%

Step 40 of 40\. The bias alone leaves both sequences uneven. A small coefficient brings the ordinary one closer to even but leaves the extreme one piled onto expert 3; only the large one spreads it, and it also moves the router further on the ordinary sequence.

## Sample 2

Parameters: `{"t": 7.75}`

How large a sequence-wise aux loss should complement the loss-free bias?

Bias only

loss-free bias on batch counts, no loss

\+ small sequence-wise loss

small coefficient: weak gradient

\+ large sequence-wise loss

large coefficient: strong gradient

An ordinary sequencemildly uneven, like the rest of the batch

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+100%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+50%

5%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+17%

10%

An extreme sequencethe LM wants almost all of it on expert 3

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+300%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+300%

4%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+50%

74%

Step 21 of 40\. Each step, every column updates the bias from batch counts; the added loss’s gradient pulls each sequence toward balance, harder at the larger coefficient.

## Sample 3

Parameters: `{"seed": 1, "t": 0}`

How large a sequence-wise aux loss should complement the loss-free bias?

Bias only

loss-free bias on batch counts, no loss

\+ small sequence-wise loss

small coefficient: weak gradient

\+ large sequence-wise loss

large coefficient: strong gradient

An ordinary sequencemildly uneven, like the rest of the batch

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+133%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+83%

7%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+33%

11%

An extreme sequencethe LM wants almost all of it on expert 3

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+300%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+300%

12%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+67%

65%

Step 40 of 40\. The bias alone leaves both sequences uneven. A small coefficient brings the ordinary one closer to even but leaves the extreme one piled onto expert 3; only the large one spreads it, and it also moves the router further on the ordinary sequence.

## Sample 4

Parameters: `{"seed": 10.5, "t": 0}`

How large a sequence-wise aux loss should complement the loss-free bias?

Bias only

loss-free bias on batch counts, no loss

\+ small sequence-wise loss

small coefficient: weak gradient

\+ large sequence-wise loss

large coefficient: strong gradient

An ordinary sequencemildly uneven, like the rest of the batch

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+100%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+67%

5%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+33%

9%

An extreme sequencethe LM wants almost all of it on expert 3

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+300%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+300%

12%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+67%

68%

Step 40 of 40\. The bias alone leaves both sequences uneven. A small coefficient brings the ordinary one closer to even but leaves the extreme one piled onto expert 3; only the large one spreads it, and it also moves the router further on the ordinary sequence.

## Sample 5

Parameters: `{"seed": 20, "t": 0}`

How large a sequence-wise aux loss should complement the loss-free bias?

Bias only

loss-free bias on batch counts, no loss

\+ small sequence-wise loss

small coefficient: weak gradient

\+ large sequence-wise loss

large coefficient: strong gradient

An ordinary sequencemildly uneven, like the rest of the batch

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+117%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+83%

7%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+17%

14%

An extreme sequencethe LM wants almost all of it on expert 3

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+300%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+300%

12%

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss



\+100%

66%

Step 40 of 40\. The bias alone leaves both sequences uneven. A small coefficient brings the ordinary one closer to even but leaves the extreme one piled onto expert 3; only the large one spreads it, and it also moves the router further on the ordinary sequence.

## Sample 6

Parameters: `{"t": 1.5}`

How large a sequence-wise aux loss should complement the loss-free bias?

Bias only

loss-free bias on batch counts, no loss

\+ small sequence-wise loss

small coefficient: weak gradient

\+ large sequence-wise loss

large coefficient: strong gradient

An ordinary sequencemildly uneven, like the rest of the batch

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+83%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss

An extreme sequencethe LM wants almost all of it on expert 3

load per expert

1

2

3

4

5

6

7

8

mean load

no sequence-wise loss, no gradient

pushed

down

\+300%



overload

worst case \+300%

balanced

step

router distortion

none

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss

load per expert

1

2

3

4

5

6

7

8

gradient from the sequence-wise loss

Step 1 of 40\. Each step, every column updates the bias from batch counts; the added loss’s gradient pulls each sequence toward balance, harder at the larger coefficient.
