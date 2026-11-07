# who-picks

[Interactive original](../upstream/app/public/viz/index.html?c=who-picks) · [Poster](../upstream/app/public/viz/posters/who-picks.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/who-picks-Fakuu07W.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 12,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 13.9 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.25× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

The whole sequence: token choice, drawn with no balancer, overloads expert 1; expert choice fills every expert’s quota, and the threshold comes close to it.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 2

Parameters: `{"t": 6.95}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.20× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 5

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Under expert choice this token outranks an earlier one, so that earlier token’s pick changes: the rule needs later tokens to decide.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 3

Parameters: `{"t": 13.9}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.25× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Every token in: only expert choice needed tokens that had not arrived yet, which inference cannot wait for; it and the threshold both let a token run 0 to 4 experts, where token choice always runs k.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.38× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 5

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 5

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

The whole sequence: token choice, drawn with no balancer, overloads expert 1; expert choice fills every expert’s quota, and the threshold comes close to it.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.13× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

1.88× target

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

The whole sequence: token choice, drawn with no balancer, overloads expert 1; expert choice fills every expert’s quota, and the threshold comes close to it.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 6

Parameters: `{"seed": 20, "t": 0}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.13× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 1 to 3

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 3

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

The whole sequence: token choice, drawn with no balancer, overloads expert 1; expert choice fills every expert’s quota, and the threshold comes close to it.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 7

Parameters: `{"t": 1.5}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

3.00× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 1 to 3

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

experts

per token

3.00× target

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Token choice gives this token k experts, and it clears exactly k cutoffs, so the threshold gives it k too.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 8

Parameters: `{"t": 2}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.25× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 3

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

experts

per token

2.25× target

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Under expert choice this token outranks an earlier one, so that earlier token’s pick changes: the rule needs later tokens to decide.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 9

Parameters: `{"t": 2.9}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.00× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 1 to 3

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Under expert choice this token outranks an earlier one, so that earlier token’s pick changes: the rule needs later tokens to decide.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 10

Parameters: `{"t": 3.8}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.25× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 1 to 3

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 3

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Token choice gives this token k experts, and it clears exactly k cutoffs, so the threshold gives it k too.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 11

Parameters: `{"t": 4.2}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.33× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 1 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Under expert choice this token outranks an earlier one, so that earlier token’s pick changes: the rule needs later tokens to decide.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 12

Parameters: `{"t": 5.2}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.18× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 1 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Token choice gives this token k experts, and it clears exactly k cutoffs, so the threshold gives it k too.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 13

Parameters: `{"t": 5.6}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.25× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 1 to 3

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Under expert choice this token outranks an earlier one, so that earlier token’s pick changes: the rule needs later tokens to decide.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 14

Parameters: `{"t": 6.5}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.14× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 5

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Token choice gives this token k experts; the threshold gives it more, one per cutoff it clears.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 15

Parameters: `{"t": 7.9}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.12× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 1 to 5

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Token choice gives this token k experts, and it clears exactly k cutoffs, so the threshold gives it k too.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 16

Parameters: `{"t": 8.3}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.17× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Under expert choice this token outranks an earlier one, so that earlier token’s pick changes: the rule needs later tokens to decide.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 17

Parameters: `{"t": 9.2}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.10× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Token choice gives this token k experts, and it clears exactly k cutoffs, so the threshold gives it k too.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 18

Parameters: `{"t": 9.7}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.14× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Token choice gives this token k experts; the threshold gives it fewer, one per cutoff it clears.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 19

Parameters: `{"t": 10.1}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.18× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Under expert choice this token outranks an earlier one, so that earlier token’s pick changes: the rule needs later tokens to decide.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 20

Parameters: `{"t": 10.6}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.22× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 5

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Token choice gives this token k experts; the threshold gives it fewer, one per cutoff it clears.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

## Sample 21

Parameters: `{"t": 11}`

Who selects the experts: what does each rule do to load and causality?

selections: tokens in arrival order × experts

tokens per expert

token t’s selectionsearlier selectionsselected earlier, now pushed out by a later token

Token choice (top-k)each token takes its top k experts, no balancer drawn (DeepSeek-V3.2, Qwen3.5, Kimi K2)

1

2

3

4

5

6

k

experts

per token

2.25× target

target

Expert choiceeach expert takes its top 8 tokens, 1 in 3 of the batch, here one sequence (Zhou et al., 2022\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Expert thresholdlogit above a per-expert cutoff that 1 in 3 earlier tokens clear (Expert Threshold, 2026\)

1

2

3

4

5

6

k

range 0 to 4

experts

per token

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.

Under expert choice this token outranks an earlier one, so that earlier token’s pick changes: the rule needs later tokens to decide.

Every rule gets the same budget, k \= 2 experts per token. The sequence leans toward expert 1, as do the earlier batches that set the threshold’s cutoffs.
