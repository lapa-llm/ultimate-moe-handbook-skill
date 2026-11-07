# bias-update-rules

[Interactive original](../upstream/app/public/viz/index.html?c=bias-update-rules) · [Poster](../upstream/app/public/viz/posters/bias-update-rules.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/bias-update-rules-DbmmtrWt.js)

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

Animation duration: 15.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Which bias update rules drift the bias mean, and what does it cost?

Sign

DeepSeek-V3

be←be\+γ sign⁡(cˉ−ce)b\_e \\leftarrow b\_e \+ \\gamma\\,\\operatorname{sign}(\\bar c \- c\_e)

one expert mean at 0 mean off 0

0

bias

mean \+0.07

V3 checkpoint: mean 2.2 to 8.0

\+21%

step

overload

worst case \+300%

balanced

Centered sign

Moonlight, Trinity Mini

be←be\+γ (sign⁡(cˉ−ce)−sign⁡‾)b\_e \\leftarrow b\_e \+ \\gamma\\,\\big(\\operatorname{sign}(\\bar c \- c\_e) \- \\overline{\\operatorname{sign}}\\big)

mean 0

Moonlight checkpoint: mean 0.000

\+21%

Linear update

LongCat-Flash

be←be\+μ cˉ−cecˉb\_e \\leftarrow b\_e \+ \\mu\\,\\dfrac{\\bar c \- c\_e}{\\bar c}

mean 0

LongCat checkpoint: mean −0.011 to −0.005

\+4%

AdamW on the bias

ZAYA1-8B (which routes top-1)

be←be−η Adam⁡ ⁣(ce−cˉ∑c)b\_e \\leftarrow b\_e \- \\eta\\,\\operatorname{Adam}\\!\\Big(\\dfrac{c\_e \- \\bar c}{\\sum c}\\Big)

mean \+0.08

ZAYA1 checkpoint: mean 0.000

\+17%

Step 40 of 40\. Every rule balances the load. Sign and AdamW lift the bias mean while centered sign and the linear update hold it at 0, yet sign balances exactly like centered sign: a shift shared by all experts changes no selection and costs precision only where the bias is kept in bf16. ZAYA1’s released biases still average 0; LongCat-Flash’s sit just below 0, as its rule aims at a compute-budget share.

## Sample 2

Parameters: `{"t": 7.75}`

Which bias update rules drift the bias mean, and what does it cost?

Sign

DeepSeek-V3

be←be\+γ sign⁡(cˉ−ce)b\_e \\leftarrow b\_e \+ \\gamma\\,\\operatorname{sign}(\\bar c \- c\_e)

one expert mean at 0 mean off 0

0

bias

mean \+0.07

V3 checkpoint: mean 2.2 to 8.0

\+13%

step

overload

worst case \+300%

balanced

Centered sign

Moonlight, Trinity Mini

be←be\+γ (sign⁡(cˉ−ce)−sign⁡‾)b\_e \\leftarrow b\_e \+ \\gamma\\,\\big(\\operatorname{sign}(\\bar c \- c\_e) \- \\overline{\\operatorname{sign}}\\big)

mean 0

Moonlight checkpoint: mean 0.000

\+13%

Linear update

LongCat-Flash

be←be\+μ cˉ−cecˉb\_e \\leftarrow b\_e \+ \\mu\\,\\dfrac{\\bar c \- c\_e}{\\bar c}

mean 0

LongCat checkpoint: mean −0.011 to −0.005

\+8%

AdamW on the bias

ZAYA1-8B (which routes top-1)

be←be−η Adam⁡ ⁣(ce−cˉ∑c)b\_e \\leftarrow b\_e \- \\eta\\,\\operatorname{Adam}\\!\\Big(\\dfrac{c\_e \- \\bar c}{\\sum c}\\Big)

mean \+0.09

ZAYA1 checkpoint: mean 0.000

\+17%

Step 21 of 40\. Each step, every column updates the bias with its own rule on the same batch.

## Sample 3

Parameters: `{"seed": 1, "t": 0}`

Which bias update rules drift the bias mean, and what does it cost?

Sign

DeepSeek-V3

be←be\+γ sign⁡(cˉ−ce)b\_e \\leftarrow b\_e \+ \\gamma\\,\\operatorname{sign}(\\bar c \- c\_e)

one expert mean at 0 mean off 0

0

bias

mean \+0.07

V3 checkpoint: mean 2.2 to 8.0

\+17%

step

overload

worst case \+300%

balanced

Centered sign

Moonlight, Trinity Mini

be←be\+γ (sign⁡(cˉ−ce)−sign⁡‾)b\_e \\leftarrow b\_e \+ \\gamma\\,\\big(\\operatorname{sign}(\\bar c \- c\_e) \- \\overline{\\operatorname{sign}}\\big)

mean 0

Moonlight checkpoint: mean 0.000

\+17%

Linear update

LongCat-Flash

be←be\+μ cˉ−cecˉb\_e \\leftarrow b\_e \+ \\mu\\,\\dfrac{\\bar c \- c\_e}{\\bar c}

mean 0

LongCat checkpoint: mean −0.011 to −0.005

\+4%

AdamW on the bias

ZAYA1-8B (which routes top-1)

be←be−η Adam⁡ ⁣(ce−cˉ∑c)b\_e \\leftarrow b\_e \- \\eta\\,\\operatorname{Adam}\\!\\Big(\\dfrac{c\_e \- \\bar c}{\\sum c}\\Big)

mean \+0.08

ZAYA1 checkpoint: mean 0.000

\+13%

Step 40 of 40\. Every rule balances the load. Sign and AdamW lift the bias mean while centered sign and the linear update hold it at 0, yet sign balances exactly like centered sign: a shift shared by all experts changes no selection and costs precision only where the bias is kept in bf16. ZAYA1’s released biases still average 0; LongCat-Flash’s sit just below 0, as its rule aims at a compute-budget share.

## Sample 4

Parameters: `{"seed": 10.5, "t": 0}`

Which bias update rules drift the bias mean, and what does it cost?

Sign

DeepSeek-V3

be←be\+γ sign⁡(cˉ−ce)b\_e \\leftarrow b\_e \+ \\gamma\\,\\operatorname{sign}(\\bar c \- c\_e)

one expert mean at 0 mean off 0

0

bias

mean \+0.08

V3 checkpoint: mean 2.2 to 8.0

\+13%

step

overload

worst case \+300%

balanced

Centered sign

Moonlight, Trinity Mini

be←be\+γ (sign⁡(cˉ−ce)−sign⁡‾)b\_e \\leftarrow b\_e \+ \\gamma\\,\\big(\\operatorname{sign}(\\bar c \- c\_e) \- \\overline{\\operatorname{sign}}\\big)

mean 0

Moonlight checkpoint: mean 0.000

\+13%

Linear update

LongCat-Flash

be←be\+μ cˉ−cecˉb\_e \\leftarrow b\_e \+ \\mu\\,\\dfrac{\\bar c \- c\_e}{\\bar c}

mean 0

LongCat checkpoint: mean −0.011 to −0.005

\+4%

AdamW on the bias

ZAYA1-8B (which routes top-1)

be←be−η Adam⁡ ⁣(ce−cˉ∑c)b\_e \\leftarrow b\_e \- \\eta\\,\\operatorname{Adam}\\!\\Big(\\dfrac{c\_e \- \\bar c}{\\sum c}\\Big)

mean \+0.09

ZAYA1 checkpoint: mean 0.000

\+8%

Step 40 of 40\. Every rule balances the load. Sign and AdamW lift the bias mean while centered sign and the linear update hold it at 0, yet sign balances exactly like centered sign: a shift shared by all experts changes no selection and costs precision only where the bias is kept in bf16. ZAYA1’s released biases still average 0; LongCat-Flash’s sit just below 0, as its rule aims at a compute-budget share.

## Sample 5

Parameters: `{"seed": 20, "t": 0}`

Which bias update rules drift the bias mean, and what does it cost?

Sign

DeepSeek-V3

be←be\+γ sign⁡(cˉ−ce)b\_e \\leftarrow b\_e \+ \\gamma\\,\\operatorname{sign}(\\bar c \- c\_e)

one expert mean at 0 mean off 0

0

bias

mean \+0.07

V3 checkpoint: mean 2.2 to 8.0

\+21%

step

overload

worst case \+300%

balanced

Centered sign

Moonlight, Trinity Mini

be←be\+γ (sign⁡(cˉ−ce)−sign⁡‾)b\_e \\leftarrow b\_e \+ \\gamma\\,\\big(\\operatorname{sign}(\\bar c \- c\_e) \- \\overline{\\operatorname{sign}}\\big)

mean 0

Moonlight checkpoint: mean 0.000

\+21%

Linear update

LongCat-Flash

be←be\+μ cˉ−cecˉb\_e \\leftarrow b\_e \+ \\mu\\,\\dfrac{\\bar c \- c\_e}{\\bar c}

mean 0

LongCat checkpoint: mean −0.011 to −0.005

\+4%

AdamW on the bias

ZAYA1-8B (which routes top-1)

be←be−η Adam⁡ ⁣(ce−cˉ∑c)b\_e \\leftarrow b\_e \- \\eta\\,\\operatorname{Adam}\\!\\Big(\\dfrac{c\_e \- \\bar c}{\\sum c}\\Big)

mean \+0.08

ZAYA1 checkpoint: mean 0.000

\+13%

Step 40 of 40\. Every rule balances the load. Sign and AdamW lift the bias mean while centered sign and the linear update hold it at 0, yet sign balances exactly like centered sign: a shift shared by all experts changes no selection and costs precision only where the bias is kept in bf16. ZAYA1’s released biases still average 0; LongCat-Flash’s sit just below 0, as its rule aims at a compute-budget share.

## Sample 6

Parameters: `{"t": 1.5}`

Which bias update rules drift the bias mean, and what does it cost?

Sign

DeepSeek-V3

be←be\+γ sign⁡(cˉ−ce)b\_e \\leftarrow b\_e \+ \\gamma\\,\\operatorname{sign}(\\bar c \- c\_e)

one expert mean at 0 mean off 0

0

bias

V3 checkpoint: mean 2.2 to 8.0

\+246%

step

overload

worst case \+300%

balanced

Centered sign

Moonlight, Trinity Mini

be←be\+γ (sign⁡(cˉ−ce)−sign⁡‾)b\_e \\leftarrow b\_e \+ \\gamma\\,\\big(\\operatorname{sign}(\\bar c \- c\_e) \- \\overline{\\operatorname{sign}}\\big)



Moonlight checkpoint: mean 0.000

Linear update

LongCat-Flash

be←be\+μ cˉ−cecˉb\_e \\leftarrow b\_e \+ \\mu\\,\\dfrac{\\bar c \- c\_e}{\\bar c}



LongCat checkpoint: mean −0.011 to −0.005

AdamW on the bias

ZAYA1-8B (which routes top-1)

be←be−η Adam⁡ ⁣(ce−cˉ∑c)b\_e \\leftarrow b\_e \- \\eta\\,\\operatorname{Adam}\\!\\Big(\\dfrac{c\_e \- \\bar c}{\\sum c}\\Big)



ZAYA1 checkpoint: mean 0.000

Step 1 of 40\. Each step, every column updates the bias with its own rule on the same batch.
