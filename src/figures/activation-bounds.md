# activation-bounds

[Interactive original](../upstream/app/public/viz/index.html?c=activation-bounds) · [Poster](../upstream/app/public/viz/posters/activation-bounds.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/activation-bounds-C_phKPYb.js)

## Controls

```json
{
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

Animation duration: 13.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Hard clamping or a smooth cap for a SwiGLU expert’s hidden units?

one token’s hidden units h, 16 of the expert’s, symmetric log scale

2 aligned unitsfactor slope \< 1%: (almost) no gradientbound ±100

largest \|h\|, same scale, against log g

g: the larger aligned unit’s gate pre-activation

SwiGLU, no bound

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

10

100

1,000

0

g \= 1

3

10

30

87

6,862

SwiGLU clamping at 10

h \= SiLU(min(g, 10)) · clip(u, −10, 10\) (DeepSeek-V4, GigaChat 3.5, GLM-5.3-Flash, Hy4-preview)

10

100

1,000

−10

−100

−1,000

0

clamped: 2 of 16 (from g \= 10 and 12.5)

10

100

1,000

0

g \= 1

3

10

30

87

100

SiTU-GLU

h \= 4·tanh(g / 4)·σ(g) · 25·tanh(u / 25\) (Kimi K3)

10

100

1,000

−10

−100

−1,000

0

saturated: 2 of 16 (from g \= 12 and 15\)

10

100

1,000

0

g \= 1

3

10

30

87

100

The no-bound row’s end value, 6,862, is K-EXAONE 2.0’s peak measured along depth with its clamp removed at inference.

Plain SwiGLU’s output ends far above both caps at the largest gate input.

The no-bound row’s end value, 6,862, is K-EXAONE 2.0’s peak measured along depth with its clamp removed at inference.

## Sample 2

Parameters: `{"t": 6.75}`

Hard clamping or a smooth cap for a SwiGLU expert’s hidden units?

one token’s hidden units h, 16 of the expert’s, symmetric log scale

2 aligned unitsfactor slope \< 1%: (almost) no gradientbound ±100

largest \|h\|, same scale, against log g

g: the larger aligned unit’s gate pre-activation

SwiGLU, no bound

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

10

100

1,000

0

g \= 1

3

10

30

87

111

SwiGLU clamping at 10

h \= SiLU(min(g, 10)) · clip(u, −10, 10\) (DeepSeek-V4, GigaChat 3.5, GLM-5.3-Flash, Hy4-preview)

10

100

1,000

−10

−100

−1,000

0

clamped: 1 of 16 (from g \= 10\)

10

100

1,000

0

g \= 1

3

10

30

87

100

SiTU-GLU

h \= 4·tanh(g / 4)·σ(g) · 25·tanh(u / 25\) (Kimi K3)

10

100

1,000

−10

−100

−1,000

0

10

100

1,000

0

g \= 1

3

10

30

87

38

The no-bound row’s end value, 6,862, is K-EXAONE 2.0’s peak measured along depth with its clamp removed at inference.

Two units’ gate and up inputs grow together: the clamp and SiTU-GLU cap them near 100, and from about the same input both stop passing gradient to those units (outlined).

The no-bound row’s end value, 6,862, is K-EXAONE 2.0’s peak measured along depth with its clamp removed at inference.

## Sample 3

Parameters: `{"t": 13.5}`

Hard clamping or a smooth cap for a SwiGLU expert’s hidden units?

one token’s hidden units h, 16 of the expert’s, symmetric log scale

2 aligned unitsfactor slope \< 1%: (almost) no gradientbound ±100

largest \|h\|, same scale, against log g

g: the larger aligned unit’s gate pre-activation

SwiGLU, no bound

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

10

100

1,000

0

g \= 1

3

10

30

87

6,862

SwiGLU clamping at 10

h \= SiLU(min(g, 10)) · clip(u, −10, 10\) (DeepSeek-V4, GigaChat 3.5, GLM-5.3-Flash, Hy4-preview)

10

100

1,000

−10

−100

−1,000

0

clamped: 2 of 16 (from g \= 10 and 12.5)

10

100

1,000

0

g \= 1

3

10

30

87

100

SiTU-GLU

h \= 4·tanh(g / 4)·σ(g) · 25·tanh(u / 25\) (Kimi K3)

10

100

1,000

−10

−100

−1,000

0

saturated: 2 of 16 (from g \= 12 and 15\)

10

100

1,000

0

g \= 1

3

10

30

87

100

The no-bound row’s end value, 6,862, is K-EXAONE 2.0’s peak measured along depth with its clamp removed at inference.

Two units’ gate and up inputs grow together: the clamp and SiTU-GLU cap them near 100, and from about the same input both stop passing gradient to those units (outlined).

The no-bound row’s end value, 6,862, is K-EXAONE 2.0’s peak measured along depth with its clamp removed at inference.

## Sample 4

Parameters: `{"t": 1.5}`

Hard clamping or a smooth cap for a SwiGLU expert’s hidden units?

one token’s hidden units h, 16 of the expert’s, symmetric log scale

2 aligned unitsfactor slope \< 1%: (almost) no gradientbound ±100

largest \|h\|, same scale, against log g

g: the larger aligned unit’s gate pre-activation

SwiGLU, no bound

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

10

100

1,000

0

g \= 1

3

10

30

87

1.8

SwiGLU clamping at 10

h \= SiLU(min(g, 10)) · clip(u, −10, 10\) (DeepSeek-V4, GigaChat 3.5, GLM-5.3-Flash, Hy4-preview)

10

100

1,000

−10

−100

−1,000

0

10

100

1,000

0

g \= 1

3

10

30

87

1.8

SiTU-GLU

h \= 4·tanh(g / 4)·σ(g) · 25·tanh(u / 25\) (Kimi K3)

10

100

1,000

−10

−100

−1,000

0

10

100

1,000

0

g \= 1

3

10

30

87

1.7

The no-bound row’s end value, 6,862, is K-EXAONE 2.0’s peak measured along depth with its clamp removed at inference.

Two units’ gate and up inputs grow together: the clamp and SiTU-GLU cap them near 100, and from about the same input both stop passing gradient to those units (outlined).

The no-bound row’s end value, 6,862, is K-EXAONE 2.0’s peak measured along depth with its clamp removed at inference.
