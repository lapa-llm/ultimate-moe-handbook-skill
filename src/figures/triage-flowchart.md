# triage-flowchart

[Interactive original](../upstream/app/public/viz/index.html?c=triage-flowchart) · [Poster](../upstream/app/public/viz/posters/triage-flowchart.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/triage-flowchart-DB-vSyk-.js)

## Controls

```json
{
  "tag": {
    "min": 0,
    "max": 4,
    "step": 1,
    "value": 2,
    "label": "run (0 blows up, 1 learns badly, 2 slow, 3 OOM, 4 won't start)",
    "hidden": true
  },
  "sig": {
    "min": -1,
    "max": 14,
    "step": 1,
    "value": -1,
    "label": "signal (-1 none)",
    "hidden": true
  }
}
```

Animation duration: 0.5 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Your run

First signal that moved

Go to section

z-loss climbing

Top-k weights flat or not renormalized

Imbalance or collapse in the first MoE layers

Grad norm and balancing loss jump before a NaN

Expert outputs or activations growing

NaN with nothing unusual before it, or exit code 16

Spikes or collapse under Muon

Training and inference disagree

MaxVio high

Slower or OOM right after a config change

Loss or specialization behind a comparison run

TFLOP/s down, or short of the target

All-to-all exposed, or slow across nodes

One rank OOMs

Error at startup

blows up

learns badly

is slow

OOMs

won't start

Go to 3.1 Router scoring

3.1 Router scoring →

Go to 3.2 Routing strategy

3.2 Routing strategy →

Go to 3.3 Load balancing

3.3 Load balancing →

Go to 3.4 Experts

3.4 Experts →

Go to 3.5 Block layout

3.5 Block layout →

Go to 3.6 Training

3.6 Training →

Go to 3.7 Systems

3.7 Systems →

Go to 4 RL routing

4 RL routing →

Pick how your run fails, or the first signal that moved, to light up the sections that explain it, then click a section to jump there. Appendix A.2 has the same index as a table.
