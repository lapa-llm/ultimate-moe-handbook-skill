# serving-smaller-k

[Interactive original](../upstream/app/public/viz/index.html?c=serving-smaller-k) · [Poster](../upstream/app/public/viz/posters/serving-smaller-k.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/serving-smaller-k-GDURkk-8.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 19,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 7.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Serving a smaller top-k: which sum should renormalize the routing weights?

one token’s softmax, experts ranked by p (top 18 of 256\)

weight, relative to trained

MMLU vs native top-8

served top-6trained top-8, not servedranks 9 to 16, in the top-16 sum

per served expert

Qwen3.6-35B-A3B, points

Renormalize over the served top-k

weight \= p / Σtop-6 p, most stacks’ default when k is lowered (Qwen3’s norm\_topk\_prob, LExI)

.29

.18

.16

.15

.13

.09

top-6

top-6 sum 0.154

softmax p

weight

trained

1.18×

−2.60

Renormalize over the trained top-8

weight \= p / Σtop-8 p, so each served expert keeps its trained weight (Chen and Yao, 2026\)

.25

.15

.13

.13

.11

.08

top-6

top-8 sum 0.182

softmax p

weight

1.00×

−1.10

Renormalize over the top 16

weight \= p / Σtop-16 p, twice the trained k (Chen and Yao, 2026\)

.17

.10

.09

.09

.07

.05

top-6

top-16 sum 0.269

softmax p

weight

0.68×

\+0.75

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

Served top-6. Serve fewer experts than training used: each row divides the same probabilities by a different sum, so each served expert gets a different weight.

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

## Sample 2

Parameters: `{"t": 3.75}`

Serving a smaller top-k: which sum should renormalize the routing weights?

one token’s softmax, experts ranked by p (top 18 of 256\)

weight, relative to trained

MMLU vs native top-8

served top-4trained top-8, not servedranks 9 to 16, in the top-16 sum

per served expert

Qwen3.6-35B-A3B, points

Renormalize over the served top-k

weight \= p / Σtop-4 p, most stacks’ default when k is lowered (Qwen3’s norm\_topk\_prob, LExI)

.38

.23

.20

.19

top-4

top-4 sum 0.120

softmax p

weight

trained

1.52×

−4.65

Renormalize over the trained top-8

weight \= p / Σtop-8 p, so each served expert keeps its trained weight (Chen and Yao, 2026\)

.25

.15

.13

.13

top-4

top-8 sum 0.182

softmax p

weight

1.00×

−3.10

Renormalize over the top 16

weight \= p / Σtop-16 p, twice the trained k (Chen and Yao, 2026\)

.17

.10

.09

.09

top-4

top-16 sum 0.269

softmax p

weight

0.68×

−0.35

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

Served top-4. Serve fewer still: renormalizing over the served experts inflates their weights, and accuracy drops further.

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

## Sample 3

Parameters: `{"seed": 1, "t": 0}`

Serving a smaller top-k: which sum should renormalize the routing weights?

one token’s softmax, experts ranked by p (top 18 of 256\)

weight, relative to trained

MMLU vs native top-8

served top-6trained top-8, not servedranks 9 to 16, in the top-16 sum

per served expert

Qwen3.6-35B-A3B, points

Renormalize over the served top-k

weight \= p / Σtop-6 p, most stacks’ default when k is lowered (Qwen3’s norm\_topk\_prob, LExI)

.28

.19

.17

.13

.12

.12

top-6

top-6 sum 0.149

softmax p

weight

trained

1.22×

−2.60

Renormalize over the trained top-8

weight \= p / Σtop-8 p, so each served expert keeps its trained weight (Chen and Yao, 2026\)

.23

.16

.14

.10

.09

.09

top-6

top-8 sum 0.182

softmax p

weight

1.00×

−1.10

Renormalize over the top 16

weight \= p / Σtop-16 p, twice the trained k (Chen and Yao, 2026\)

.15

.10

.09

.07

.06

.06

top-6

top-16 sum 0.276

softmax p

weight

0.66×

\+0.75

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

Served top-6. Serve fewer experts than training used: each row divides the same probabilities by a different sum, so each served expert gets a different weight.

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

## Sample 4

Parameters: `{"seed": 10.5, "t": 0}`

Serving a smaller top-k: which sum should renormalize the routing weights?

one token’s softmax, experts ranked by p (top 18 of 256\)

weight, relative to trained

MMLU vs native top-8

served top-6trained top-8, not servedranks 9 to 16, in the top-16 sum

per served expert

Qwen3.6-35B-A3B, points

Renormalize over the served top-k

weight \= p / Σtop-6 p, most stacks’ default when k is lowered (Qwen3’s norm\_topk\_prob, LExI)

.28

.24

.17

.11

.10

.10

top-6

top-6 sum 0.152

softmax p

weight

trained

1.20×

−2.60

Renormalize over the trained top-8

weight \= p / Σtop-8 p, so each served expert keeps its trained weight (Chen and Yao, 2026\)

.23

.20

.14

.09

.09

.08

top-6

top-8 sum 0.182

softmax p

weight

1.00×

−1.10

Renormalize over the top 16

weight \= p / Σtop-16 p, twice the trained k (Chen and Yao, 2026\)

.16

.14

.09

.06

.06

.06

top-6

top-16 sum 0.270

softmax p

weight

0.67×

\+0.75

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

Served top-6. Serve fewer experts than training used: each row divides the same probabilities by a different sum, so each served expert gets a different weight.

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

## Sample 5

Parameters: `{"seed": 20, "t": 0}`

Serving a smaller top-k: which sum should renormalize the routing weights?

one token’s softmax, experts ranked by p (top 18 of 256\)

weight, relative to trained

MMLU vs native top-8

served top-6trained top-8, not servedranks 9 to 16, in the top-16 sum

per served expert

Qwen3.6-35B-A3B, points

Renormalize over the served top-k

weight \= p / Σtop-6 p, most stacks’ default when k is lowered (Qwen3’s norm\_topk\_prob, LExI)

.34

.15

.14

.13

.12

.12

top-6

top-6 sum 0.149

softmax p

weight

trained

1.22×

−2.60

Renormalize over the trained top-8

weight \= p / Σtop-8 p, so each served expert keeps its trained weight (Chen and Yao, 2026\)

.28

.12

.11

.11

.10

.10

top-6

top-8 sum 0.182

softmax p

weight

1.00×

−1.10

Renormalize over the top 16

weight \= p / Σtop-16 p, twice the trained k (Chen and Yao, 2026\)

.18

.08

.07

.07

.06

.06

top-6

top-16 sum 0.282

softmax p

weight

0.65×

\+0.75

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

Served top-6. Serve fewer experts than training used: each row divides the same probabilities by a different sum, so each served expert gets a different weight.

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

## Sample 6

Parameters: `{"t": 4.9}`

Serving a smaller top-k: which sum should renormalize the routing weights?

one token’s softmax, experts ranked by p (top 18 of 256\)

weight, relative to trained

MMLU vs native top-8

served top-8trained top-8, not servedranks 9 to 16, in the top-16 sum

per served expert

Qwen3.6-35B-A3B, points

Renormalize over the served top-k

weight \= p / Σtop-8 p, most stacks’ default when k is lowered (Qwen3’s norm\_topk\_prob, LExI)

.25

.15

.13

.13

.11

.08

.08

.08

top-8

top-8 sum 0.182

softmax p

weight

trained

1.00×

native

Renormalize over the trained top-8

weight \= p / Σtop-8 p, so each served expert keeps its trained weight (Chen and Yao, 2026\)

.25

.15

.13

.13

.11

.08

.08

.08

top-8

top-8 sum 0.182

softmax p

weight

1.00×

native

Renormalize over the top 16

weight \= p / Σtop-16 p, twice the trained k (Chen and Yao, 2026\)

.17

.10

.09

.09

.07

.05

.05

.05

top-8

top-16 sum 0.269

softmax p

weight

0.68×

not reported

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).

Served top-8. At the trained k the first two rows are the native model, while the top-16 sum shrinks every weight: it pays only once k is cut, where it kept MMLU closest to native.

One token whose top 8 hold 0.182 of the softmax, Qwen3.6-35B-A3B’s mean on WikiText; the MMLU changes are measured (Chen and Yao, Table 5).
