# router-mode-5way

[Interactive original](../upstream/app/public/viz/index.html?c=router-mode-5way) · [Poster](../upstream/app/public/viz/posters/router-mode-5way.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/router-mode-5way-DZ-RV4tE.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Which balancer runs fastest, by median over iterations 101 to 120?

Model TFLOP/s per GPU

Training LM loss

the other four configurationshighest median throughput

Aux loss  coefficient 1e-3, counted per micro-batch

80

100

120

140

160

median 125

7.0

7.5

8.0

6.84

Aux loss plus sequence-wise aux loss  both at coefficient 1e-3, in every layer

127

6.89

Expert bias only  sigmoid scores, bias update rate 1e-3, bf16 token counts

99

6.81

Quantile balancing  each expert’s bias solved per micro-batch, the solutions averaged across the global batch

139

6.94

Quantile balancing, EMA 0.9  each step keeps 0.9 of the previous bias and takes 0.1 of the solved one

20

40

60

80

100

120

121

20

120

iteration

6.80

Five router configurations of the same MoE trained from init on one node, one seed each, each row highlighting one run against the others. Quantile balancing has the highest median throughput over the last 20 iterations (dashed) but also ends with the highest training loss, so this does not show faster training to equal quality.
