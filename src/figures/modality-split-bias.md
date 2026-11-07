# modality-split-bias

[Interactive original](../upstream/app/public/viz/index.html?c=modality-split-bias) · [Poster](../upstream/app/public/viz/posters/modality-split-bias.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/modality-split-bias-BGiKrKui.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 6,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 15.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Does one bias over all tokens balance each modality’s expert load?

text tokenimage token

One shared bias

from all tokens together (DeepSeek-VL2, Kimi-VL)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

One bias for all tokens

bias

Overload (MaxVio) within each modality

\+117%



worst case \+300%

text

balanced

\+108%

step

image

balanced

One bias per modality

text and image each from their own counts (DeepSeek-V4.1-Flash)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

Two biases, one per modality

text bias

image bias

Overload (MaxVio) within each modality

\+17%



text

balanced

\+25%



image

balanced

Step 40 of 40\. The end of training: with text leaning toward experts 1 to 4 and images toward 5 to 8, the shared bias balances the total load while each modality stays uneven; a bias per modality balances each one, at the price of pushing every expert to take its share of each modality.

## Sample 2

Parameters: `{"t": 7.75}`

Does one bias over all tokens balance each modality’s expert load?

text tokenimage token

One shared bias

from all tokens together (DeepSeek-VL2, Kimi-VL)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

One bias for all tokens

bias

Overload (MaxVio) within each modality

\+117%



worst case \+300%

text

balanced

\+117%

step

image

balanced

One bias per modality

text and image each from their own counts (DeepSeek-V4.1-Flash)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

Two biases, one per modality

text bias

image bias

Overload (MaxVio) within each modality

\+17%



text

balanced

\+33%



image

balanced

Step 21 of 40\. Each step, the bias moves expert load toward even, from all tokens together or from each modality’s own.

## Sample 3

Parameters: `{"seed": 1, "t": 0}`

Does one bias over all tokens balance each modality’s expert load?

text tokenimage token

One shared bias

from all tokens together (DeepSeek-VL2, Kimi-VL)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

One bias for all tokens

bias

Overload (MaxVio) within each modality

\+117%



worst case \+300%

text

balanced

\+125%

step

image

balanced

One bias per modality

text and image each from their own counts (DeepSeek-V4.1-Flash)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

Two biases, one per modality

text bias

image bias

Overload (MaxVio) within each modality

\+42%



text

balanced

\+42%



image

balanced

Step 40 of 40\. The end of training: with text leaning toward experts 1 to 4 and images toward 5 to 8, the shared bias balances the total load while each modality stays uneven; a bias per modality balances each one, at the price of pushing every expert to take its share of each modality.

## Sample 4

Parameters: `{"seed": 10.5, "t": 0}`

Does one bias over all tokens balance each modality’s expert load?

text tokenimage token

One shared bias

from all tokens together (DeepSeek-VL2, Kimi-VL)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

One bias for all tokens

bias

Overload (MaxVio) within each modality

\+117%



worst case \+300%

text

balanced

\+133%

step

image

balanced

One bias per modality

text and image each from their own counts (DeepSeek-V4.1-Flash)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

Two biases, one per modality

text bias

image bias

Overload (MaxVio) within each modality

\+25%



text

balanced

\+8%



image

balanced

Step 40 of 40\. The end of training: with text leaning toward experts 1 to 4 and images toward 5 to 8, the shared bias balances the total load while each modality stays uneven; a bias per modality balances each one, at the price of pushing every expert to take its share of each modality.

## Sample 5

Parameters: `{"seed": 20, "t": 0}`

Does one bias over all tokens balance each modality’s expert load?

text tokenimage token

One shared bias

from all tokens together (DeepSeek-VL2, Kimi-VL)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

One bias for all tokens

bias

Overload (MaxVio) within each modality

\+125%



worst case \+300%

text

balanced

\+125%

step

image

balanced

One bias per modality

text and image each from their own counts (DeepSeek-V4.1-Flash)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

Two biases, one per modality

text bias

image bias

Overload (MaxVio) within each modality

\+42%



text

balanced

\+25%



image

balanced

Step 40 of 40\. The end of training: with text leaning toward experts 1 to 4 and images toward 5 to 8, the shared bias balances the total load while each modality stays uneven; a bias per modality balances each one, at the price of pushing every expert to take its share of each modality.

## Sample 6

Parameters: `{"t": 1.5}`

Does one bias over all tokens balance each modality’s expert load?

text tokenimage token

One shared bias

from all tokens together (DeepSeek-VL2, Kimi-VL)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

One bias for all tokens

bias

Overload (MaxVio) within each modality

\+150%



worst case \+300%

text

balanced

\+200%

step

image

balanced

One bias per modality

text and image each from their own counts (DeepSeek-V4.1-Flash)

All tokens, piled on the experts they selected

mean load

1

2

3

4

5

6

7

8

expert

Two biases, one per modality

text bias

image bias

Overload (MaxVio) within each modality

\+150%



text

balanced

\+200%



image

balanced

Step 1 of 40\. Each step, the bias moves expert load toward even, from all tokens together or from each modality’s own.
