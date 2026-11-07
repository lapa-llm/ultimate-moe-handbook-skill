# variable-compute-experts

[Interactive original](../upstream/app/public/viz/index.html?c=variable-compute-experts) · [Poster](../upstream/app/public/viz/posters/variable-compute-experts.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/variable-compute-experts-DfYmr2zR.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 4,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 14.3 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Can compute per token vary while the mean stays fixed?

experts, drawn at their width

activated width per token

selected for this tokenidentity expert, width 0

this tokenearlier tokens



homogeneous experts’ 2

Homogeneous experts

8 experts of width 1, top-2 (Mixtral, MoDSE’s baseline)

2

2

Zero-computation experts

8 FFN \+ 4 identity experts, top-3, FFN-only bias holds the mean at 2 (LongCat-Flash: 512 \+ 256, top-12, mean 8\)

2

3

mean 2.0, std 0.82 (LongCat-Flash, one layer: 2.5 around 8 of 12), range 1 to 3

Heterogeneous experts

widths 0.2 to 1.8 in pairs summing to 2, top-2, parameter penalty (MoDSE’s 300M×8 ladder, HMoE’s loss)

1.8

0.2

1.6

0.4

1.2

0.8

1

1

2

1.4

mean 2.0, std 0.97, range 0.6 to 3.4

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

Every token fills its top-k slots, yet in the lower rows what lands in them changes how much compute it gets.

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

## Sample 2

Parameters: `{"t": 7.15}`

Can compute per token vary while the mean stays fixed?

experts, drawn at their width

activated width per token

selected for this tokenidentity expert, width 0

this tokenearlier tokens



homogeneous experts’ 2

Homogeneous experts

8 experts of width 1, top-2 (Mixtral, MoDSE’s baseline)

2

2

Zero-computation experts

8 FFN \+ 4 identity experts, top-3, FFN-only bias holds the mean at 2 (LongCat-Flash: 512 \+ 256, top-12, mean 8\)

2

3

mean 2.1, std 0.83 (LongCat-Flash, one layer: 2.5 around 8 of 12), range 1 to 3

Heterogeneous experts

widths 0.2 to 1.8 in pairs summing to 2, top-2, parameter penalty (MoDSE’s 300M×8 ladder, HMoE’s loss)

1.8

0.2

1.6

0.4

1.2

0.8

1

1

2

3.4

mean 2.2, std 0.87, range 1 to 3.4

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

Every token fills its top-k slots, yet in the lower rows what lands in them changes how much compute it gets.

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

## Sample 3

Parameters: `{"t": 14.3}`

Can compute per token vary while the mean stays fixed?

experts, drawn at their width

activated width per token

selected for this tokenidentity expert, width 0

this tokenearlier tokens



homogeneous experts’ 2

Homogeneous experts

8 experts of width 1, top-2 (Mixtral, MoDSE’s baseline)

2

2

Zero-computation experts

8 FFN \+ 4 identity experts, top-3, FFN-only bias holds the mean at 2 (LongCat-Flash: 512 \+ 256, top-12, mean 8\)

2

3

mean 2.0, std 0.82 (LongCat-Flash, one layer: 2.5 around 8 of 12), range 1 to 3

Heterogeneous experts

widths 0.2 to 1.8 in pairs summing to 2, top-2, parameter penalty (MoDSE’s 300M×8 ladder, HMoE’s loss)

1.8

0.2

1.6

0.4

1.2

0.8

1

1

2

1.4

mean 2.0, std 0.97, range 0.6 to 3.4

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

Over the batch, the mean compute stays close to the homogeneous experts’, but the router decides which tokens get more of it.

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Can compute per token vary while the mean stays fixed?

experts, drawn at their width

activated width per token

selected for this tokenidentity expert, width 0

this tokenearlier tokens



homogeneous experts’ 2

Homogeneous experts

8 experts of width 1, top-2 (Mixtral, MoDSE’s baseline)

2

2

Zero-computation experts

8 FFN \+ 4 identity experts, top-3, FFN-only bias holds the mean at 2 (LongCat-Flash: 512 \+ 256, top-12, mean 8\)

2

1

mean 2.0, std 0.84 (LongCat-Flash, one layer: 2.5 around 8 of 12), range 0 to 3

Heterogeneous experts

widths 0.2 to 1.8 in pairs summing to 2, top-2, parameter penalty (MoDSE’s 300M×8 ladder, HMoE’s loss)

1.8

0.2

1.6

0.4

1.2

0.8

1

1

2

3.4

mean 2.0, std 0.95, range 0.6 to 3.4

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

Every token fills its top-k slots, yet in the lower rows what lands in them changes how much compute it gets.

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Can compute per token vary while the mean stays fixed?

experts, drawn at their width

activated width per token

selected for this tokenidentity expert, width 0

this tokenearlier tokens



homogeneous experts’ 2

Homogeneous experts

8 experts of width 1, top-2 (Mixtral, MoDSE’s baseline)

2

2

Zero-computation experts

8 FFN \+ 4 identity experts, top-3, FFN-only bias holds the mean at 2 (LongCat-Flash: 512 \+ 256, top-12, mean 8\)

2

3

mean 2.0, std 0.73 (LongCat-Flash, one layer: 2.5 around 8 of 12), range 0 to 3

Heterogeneous experts

widths 0.2 to 1.8 in pairs summing to 2, top-2, parameter penalty (MoDSE’s 300M×8 ladder, HMoE’s loss)

1.8

0.2

1.6

0.4

1.2

0.8

1

1

2

3.4

mean 2.0, std 0.98, range 0.6 to 3.4

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

Every token fills its top-k slots, yet in the lower rows what lands in them changes how much compute it gets.

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

## Sample 6

Parameters: `{"seed": 20, "t": 0}`

Can compute per token vary while the mean stays fixed?

experts, drawn at their width

activated width per token

selected for this tokenidentity expert, width 0

this tokenearlier tokens



homogeneous experts’ 2

Homogeneous experts

8 experts of width 1, top-2 (Mixtral, MoDSE’s baseline)

2

2

Zero-computation experts

8 FFN \+ 4 identity experts, top-3, FFN-only bias holds the mean at 2 (LongCat-Flash: 512 \+ 256, top-12, mean 8\)

2

2

mean 2.0, std 0.84 (LongCat-Flash, one layer: 2.5 around 8 of 12), range 0 to 3

Heterogeneous experts

widths 0.2 to 1.8 in pairs summing to 2, top-2, parameter penalty (MoDSE’s 300M×8 ladder, HMoE’s loss)

1.8

0.2

1.6

0.4

1.2

0.8

1

1

2

1.8

mean 2.0, std 0.90, range 0.6 to 3.4

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.

Every token fills its top-k slots, yet in the lower rows what lands in them changes how much compute it gets.

One bias per row, set from this batch, holds the mean at 2, and each row’s per-token lean sets its spread.
