# expert-activations

[Interactive original](../upstream/app/public/viz/index.html?c=expert-activations) · [Poster](../upstream/app/public/viz/posters/expert-activations.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/expert-activations-DkpeLVTN.js)

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

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,562 (1,112×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2,851 (900×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

51 (30×)

Input scale c \= 30.0. At the largest input scale, the largest hidden unit (blue) reaches thousands under SwiGLU and ReLU², tens under PolyNorm.

## Sample 2

Parameters: `{"t": 6.75}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

67 (48×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

123 (39×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

11 (6.2×)

Input scale c \= 6.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 3

Parameters: `{"t": 13.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,562 (1,112×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2,851 (900×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

51 (30×)

Input scale c \= 30.0. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

689 (1,125×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,607 (900×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

15 (30×)

Input scale c \= 30.0. At the largest input scale, the largest hidden unit (blue) reaches thousands under SwiGLU and ReLU², tens under PolyNorm.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,041 (1,238×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,253 (900×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.63 for every c, bound 1.75

19 (30×)

Input scale c \= 30.0. At the largest input scale, the largest hidden unit (blue) reaches thousands under SwiGLU and ReLU², tens under PolyNorm.

## Sample 6

Parameters: `{"seed": 20, "t": 0}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

3,243 (1,121×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

5,934 (900×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.64 for every c, bound 1.75

74 (30×)

Input scale c \= 30.0. At the largest input scale, the largest hidden unit (blue) reaches thousands under SwiGLU and ReLU², tens under PolyNorm.

## Sample 7

Parameters: `{"t": 1.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1.4

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

3.2

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

1.7

Input scale c \= 1.0. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 8

Parameters: `{"t": 1.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1.7 (1.2×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

3.7 (1.2×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

1.8 (1.1×)

Input scale c \= 1.1. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 9

Parameters: `{"t": 2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2.1 (1.5×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

4.5 (1.4×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

2.0 (1.2×)

Input scale c \= 1.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 10

Parameters: `{"t": 2.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2.4 (1.7×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

5.2 (1.6×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

2.2 (1.3×)

Input scale c \= 1.3. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 11

Parameters: `{"t": 2.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2.7 (1.9×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

5.8 (1.8×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

2.3 (1.4×)

Input scale c \= 1.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 12

Parameters: `{"t": 2.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

3.5 (2.5×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

7.4 (2.3×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

2.6 (1.5×)

Input scale c \= 1.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 13

Parameters: `{"t": 2.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

3.9 (2.8×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

8.3 (2.6×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

2.8 (1.6×)

Input scale c \= 1.6. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 14

Parameters: `{"t": 3}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

4.3 (3.1×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

9.0 (2.8×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

2.9 (1.7×)

Input scale c \= 1.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 15

Parameters: `{"t": 3.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

5.0 (3.6×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

10 (3.3×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

3.1 (1.8×)

Input scale c \= 1.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 16

Parameters: `{"t": 3.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

5.6 (4.0×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

12 (3.7×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

3.3 (1.9×)

Input scale c \= 1.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 17

Parameters: `{"t": 3.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

6.2 (4.4×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

13 (4.0×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

3.4 (2.0×)

Input scale c \= 2.0. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 18

Parameters: `{"t": 3.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

7.2 (5.2×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

15 (4.7×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

3.7 (2.2×)

Input scale c \= 2.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 19

Parameters: `{"t": 3.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

8.2 (5.9×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

17 (5.2×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

3.9 (2.3×)

Input scale c \= 2.3. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 20

Parameters: `{"t": 4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

9.1 (6.4×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

18 (5.7×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

4.1 (2.4×)

Input scale c \= 2.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 21

Parameters: `{"t": 4.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

11 (7.6×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

21 (6.6×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

4.4 (2.6×)

Input scale c \= 2.6. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 22

Parameters: `{"t": 4.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

12 (8.6×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

24 (7.4×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

4.7 (2.7×)

Input scale c \= 2.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 23

Parameters: `{"t": 4.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

13 (9.4×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

26 (8.1×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

4.9 (2.8×)

Input scale c \= 2.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 24

Parameters: `{"t": 4.6}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

14 (9.7×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

26 (8.3×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

5.0 (2.9×)

Input scale c \= 2.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 25

Parameters: `{"t": 4.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

16 (11×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

30 (9.4×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

5.3 (3.1×)

Input scale c \= 3.1. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 26

Parameters: `{"t": 4.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

18 (12×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

33 (11×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

5.6 (3.2×)

Input scale c \= 3.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 27

Parameters: `{"t": 5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

19 (14×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

36 (11×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

5.8 (3.4×)

Input scale c \= 3.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 28

Parameters: `{"t": 5.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

22 (16×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

42 (13×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

6.3 (3.6×)

Input scale c \= 3.6. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 29

Parameters: `{"t": 5.3}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

23 (16×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

43 (14×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

6.3 (3.7×)

Input scale c \= 3.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 30

Parameters: `{"t": 5.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

25 (18×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

47 (15×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

6.6 (3.9×)

Input scale c \= 3.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 31

Parameters: `{"t": 5.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

28 (20×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

52 (16×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

6.9 (4.0×)

Input scale c \= 4.0. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 32

Parameters: `{"t": 5.6}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

29 (20×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

53 (17×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

7.0 (4.1×)

Input scale c \= 4.1. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 33

Parameters: `{"t": 5.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

32 (23×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

60 (19×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

7.5 (4.3×)

Input scale c \= 4.3. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 34

Parameters: `{"t": 5.8}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

33 (24×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

61 (19×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

7.6 (4.4×)

Input scale c \= 4.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 35

Parameters: `{"t": 5.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

36 (26×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

67 (21×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

7.9 (4.6×)

Input scale c \= 4.6. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 36

Parameters: `{"t": 6}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

40 (28×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

73 (23×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

8.2 (4.8×)

Input scale c \= 4.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 37

Parameters: `{"t": 6.1}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

41 (29×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

75 (24×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

8.4 (4.9×)

Input scale c \= 4.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 38

Parameters: `{"t": 6.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

46 (33×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

85 (27×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

8.9 (5.2×)

Input scale c \= 5.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 39

Parameters: `{"t": 6.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

52 (37×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

95 (30×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

9.4 (5.5×)

Input scale c \= 5.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 40

Parameters: `{"t": 6.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

57 (40×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

104 (33×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

9.8 (5.7×)

Input scale c \= 5.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 41

Parameters: `{"t": 6.6}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

58 (41×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

107 (34×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

9.9 (5.8×)

Input scale c \= 5.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 42

Parameters: `{"t": 6.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

66 (47×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

120 (38×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

11 (6.2×)

Input scale c \= 6.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 43

Parameters: `{"t": 6.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

74 (52×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

135 (43×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

11 (6.5×)

Input scale c \= 6.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 44

Parameters: `{"t": 7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

80 (57×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

147 (46×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

12 (6.8×)

Input scale c \= 6.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 45

Parameters: `{"t": 7.1}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

83 (59×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

151 (48×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

12 (6.9×)

Input scale c \= 6.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 46

Parameters: `{"t": 7.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

93 (66×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

170 (54×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

13 (7.3×)

Input scale c \= 7.3. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 47

Parameters: `{"t": 7.3}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

96 (68×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

175 (55×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

13 (7.4×)

Input scale c \= 7.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 48

Parameters: `{"t": 7.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

105 (74×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

191 (60×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

13 (7.8×)

Input scale c \= 7.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 49

Parameters: `{"t": 7.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

114 (81×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

208 (66×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

14 (8.1×)

Input scale c \= 8.1. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 50

Parameters: `{"t": 7.6}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

117 (83×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

214 (68×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

14 (8.2×)

Input scale c \= 8.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 51

Parameters: `{"t": 7.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

132 (94×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

241 (76×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

15 (8.7×)

Input scale c \= 8.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 52

Parameters: `{"t": 7.8}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

136 (97×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

248 (78×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

15 (8.8×)

Input scale c \= 8.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 53

Parameters: `{"t": 7.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

148 (106×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

271 (85×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

16 (9.2×)

Input scale c \= 9.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 54

Parameters: `{"t": 8}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

162 (115×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

295 (93×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

17 (9.7×)

Input scale c \= 9.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 55

Parameters: `{"t": 8.1}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

166 (118×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

303 (96×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

17 (9.8×)

Input scale c \= 9.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 56

Parameters: `{"t": 8.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

187 (133×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

342 (108×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

18 (10×)

Input scale c \= 10.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 57

Parameters: `{"t": 8.3}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

193 (137×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

352 (111×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

18 (11×)

Input scale c \= 10.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 58

Parameters: `{"t": 8.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

210 (150×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

384 (121×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

19 (11×)

Input scale c \= 11.0. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 59

Parameters: `{"t": 8.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

229 (163×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

419 (132×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

20 (11×)

Input scale c \= 11.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 60

Parameters: `{"t": 8.6}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

236 (168×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

430 (136×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

20 (12×)

Input scale c \= 11.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 61

Parameters: `{"t": 8.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

266 (189×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

485 (153×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

21 (12×)

Input scale c \= 12.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 62

Parameters: `{"t": 8.8}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

273 (194×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

498 (157×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

22 (13×)

Input scale c \= 12.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 63

Parameters: `{"t": 8.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

298 (212×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

544 (172×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

22 (13×)

Input scale c \= 13.1. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 64

Parameters: `{"t": 9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

325 (231×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

593 (187×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

23 (14×)

Input scale c \= 13.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 65

Parameters: `{"t": 9.1}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

334 (238×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

610 (192×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

24 (14×)

Input scale c \= 13.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 66

Parameters: `{"t": 9.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

377 (268×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

687 (217×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

25 (15×)

Input scale c \= 14.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 67

Parameters: `{"t": 9.3}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

387 (276×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

706 (223×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

26 (15×)

Input scale c \= 14.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 68

Parameters: `{"t": 9.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

422 (301×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

771 (243×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

27 (16×)

Input scale c \= 15.6. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 69

Parameters: `{"t": 9.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

461 (328×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

841 (265×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

28 (16×)

Input scale c \= 16.3. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 70

Parameters: `{"t": 9.6}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

473 (337×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

864 (273×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

28 (17×)

Input scale c \= 16.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 71

Parameters: `{"t": 9.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

534 (380×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

974 (308×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

30 (18×)

Input scale c \= 17.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 72

Parameters: `{"t": 9.8}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

549 (391×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,001 (316×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

30 (18×)

Input scale c \= 17.8. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 73

Parameters: `{"t": 9.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

598 (426×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,092 (345×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

32 (19×)

Input scale c \= 18.6. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 74

Parameters: `{"t": 10}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

653 (465×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,192 (376×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

33 (19×)

Input scale c \= 19.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 75

Parameters: `{"t": 10.1}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

671 (478×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,225 (387×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

34 (20×)

Input scale c \= 19.7. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 76

Parameters: `{"t": 10.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

757 (539×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,381 (436×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

36 (21×)

Input scale c \= 20.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 77

Parameters: `{"t": 10.3}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

777 (554×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,419 (448×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

36 (21×)

Input scale c \= 21.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 78

Parameters: `{"t": 10.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

848 (604×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,548 (489×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

38 (22×)

Input scale c \= 22.1. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 79

Parameters: `{"t": 10.5}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

926 (659×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,690 (533×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

40 (23×)

Input scale c \= 23.1. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 80

Parameters: `{"t": 10.6}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

951 (677×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,736 (548×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

40 (23×)

Input scale c \= 23.4. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 81

Parameters: `{"t": 10.7}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,072 (764×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,957 (618×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

43 (25×)

Input scale c \= 24.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 82

Parameters: `{"t": 10.8}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,102 (785×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2,012 (635×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

43 (25×)

Input scale c \= 25.2. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 83

Parameters: `{"t": 10.9}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,202 (856×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2,195 (693×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

45 (26×)

Input scale c \= 26.3. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 84

Parameters: `{"t": 11}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,312 (934×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2,395 (756×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

47 (27×)

Input scale c \= 27.5. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 85

Parameters: `{"t": 11.1}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,348 (960×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2,461 (777×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

48 (28×)

Input scale c \= 27.9. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 86

Parameters: `{"t": 11.2}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,520 (1,082×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2,775 (876×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

51 (30×)

Input scale c \= 29.6. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.

## Sample 87

Parameters: `{"t": 11.4}`

Which expert activations grow with the square of the input scale?

16 of one token’s hidden units h, same g and u in every row

symmetric log scale, largest \|h\|, plotted right

largest \|h\| against input scale c, log-log

in brackets: growth since c \= 1

SwiGLU

h \= SiLU(g) · u (DeepSeek-V3, Qwen3, Kimi K2)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

1,562 (1,112×)

ReLU²

h \= ReLU(u)², no gate matrix, so 1.5× wider at equal parameters (Nemotron 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

2,851 (900×)

Expert-Specific PolyNorm

h \= 0.5 · (Σn an gn / RMS(gn) \+ b) · u, n \= 1 to 3, a and b learned per expert (Motif 3\)

10

100

1,000

−10

−100

−1,000

0

1

10

100

1,000

c \= 1

3

10

30

c²

gate RMS at init 0.65 for every c, bound 1.75

51 (30×)

Input scale c \= 31.3. As the token’s inputs scale up, ReLU² grows with the square of the scale, SwiGLU about as fast, and PolyNorm only linearly, so a growing input scale hits SwiGLU and ReLU² experts hardest.
