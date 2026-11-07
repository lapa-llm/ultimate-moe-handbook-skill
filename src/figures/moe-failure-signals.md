# moe-failure-signals

[Interactive original](../upstream/app/public/viz/index.html?c=moe-failure-signals) · [Poster](../upstream/app/public/viz/posters/moe-failure-signals.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/moe-failure-signals-CivK0B7B.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 1,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 15.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

2.23

\+25%

2.7×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

2.36

\+371%

alarm at step 27

2.7×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

2.24

\+25%

2.7×

0.017×

alarm at step 36

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

2.23

\+25%

5,700×

alarm at step 29

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

Here each failure trips only its own signal and the loss alarm never fires, so a loss alarm alone misses all three: alarm on MaxVio and both norm ratios, per layer.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

## Sample 2

Parameters: `{"t": 7.75}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

2.36

\+35%

2.6×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

2.40

\+138%

alarm at step 27

2.6×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

2.37

\+35%

2.6×

0.13×

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

2.36

\+35%

159×

alarm at step 29

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

The rogue expert shows only in the largest output norm.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

## Sample 3

Parameters: `{"seed": 10.5, "t": 0}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

2.23

\+19%

2.6×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

2.37

\+361%

alarm at step 27

2.6×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

2.25

\+19%

2.6×

0.053×

alarm at step 53

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

2.23

\+19%

5,700×

alarm at step 29

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

Here each failure trips only its own signal and the loss alarm never fires, so a loss alarm alone misses all three: alarm on MaxVio and both norm ratios, per layer.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

## Sample 4

Parameters: `{"seed": 20, "t": 0}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

2.24

\+35%

2.7×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

2.39

\+397%

alarm at step 28

2.7×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

2.26

\+35%

2.7×

0.025×

alarm at step 42

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

2.24

\+35%

5,700×

alarm at step 29

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

Here each failure trips only its own signal and the loss alarm never fires, so a loss alarm alone misses all three: alarm on MaxVio and both norm ratios, per layer.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

## Sample 5

Parameters: `{"t": 1.5}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

3.10

\+21%

2.7×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

3.10

\+21%

2.7×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

3.10

\+21%

2.7×

0.5×

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

3.10

\+21%

14×

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

Before the failures begin, no signal crosses its alarm, though the expert that later goes rogue already runs larger than the rest.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

## Sample 6

Parameters: `{"t": 3.9}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

2.68

\+24%

2.7×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

2.68

\+24%

2.7×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

2.68

\+24%

2.7×

0.5×

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

2.68

\+24%

14×

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

Before the failures begin, no signal crosses its alarm, though the expert that later goes rogue already runs larger than the rest.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

## Sample 7

Parameters: `{"t": 6.8}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

2.43

\+19%

2.7×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

2.45

\+104%

alarm at step 27

2.7×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

2.44

\+19%

2.7×

0.19×

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

2.43

\+19%

84×

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

Routing collapse shows in MaxVio, the busiest expert’s overload.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

## Sample 8

Parameters: `{"t": 7.2}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

2.39

\+21%

2.6×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

2.42

\+108%

alarm at step 27

2.6×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

2.40

\+21%

2.6×

0.16×

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

2.39

\+21%

108×

alarm at step 29

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

The rogue expert shows only in the largest output norm.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

## Sample 9

Parameters: `{"t": 8.6}`

What to monitor in MoE training: loss, MaxVio or per-expert output norms

loss

alarm: 0.1 above its lowest so far (dashed)

MaxVio \= (max − mean) ÷ mean load

alarm: above \+100% (dashed)

max ÷ median expert output norm

alarm: above 100× (dashed)

min ÷ median expert output norm

alarm: below 0.1× (dashed)

Healthy run no failure; each row below adds one

2.34

\+22%

2.7×

0.5×

Routing collapse the router drifts toward one expert, which most tokens select

2.40

\+161%

alarm at step 27

2.7×

0.5×

Dead expert one expert’s output decays to zero while the router keeps sending it tokens

2.36

\+22%

2.7×

0.099×

alarm at step 36

Rogue expert one expert’s SwiGLU output runs away, from 14× to 5,700× the median

2.34

\+22%

265×

alarm at step 29

0.5×

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.

The dead expert shows only in the smallest output norm.

Each failure is drawn leaving the loss within its noise. The alarm levels are ours, except the loss’s 0.1 margin, which follows Qwen3.8-Next’s spike criterion.
