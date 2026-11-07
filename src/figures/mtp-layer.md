# mtp-layer

[Interactive original](../upstream/app/public/viz/index.html?c=mtp-layer) · [Poster](../upstream/app/public/viz/posters/mtp-layer.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/mtp-layer-D5RMG5gK.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

How is a multi-token prediction module wired into the model?

MTP module

can be dropped

at inference

token t

token t\+1

embedding

embedding

shared

main model

h t

RMSNorm

RMSNorm

concatenate

projection, 2d → d

transformer block

output head

output head

shared

predicts token t\+1

predicts token t\+2

× λ

\+

training loss

One position during training, following DeepSeek-V3: the multi-token prediction module joins the main model’s hidden state with the next token’s embedding, runs one transformer block and predicts the token after it through the shared output head. At inference the module can be dropped or kept as a draft model for speculative decoding.
