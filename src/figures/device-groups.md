# device-groups

[Interactive original](../upstream/app/public/viz/index.html?c=device-groups) · [Poster](../upstream/app/public/viz/posters/device-groups.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/device-groups-C-RMgA9Y.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 5,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 14.7 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 2.8

bound 4×

1

2

3

4

mean

max 1.97× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.65

device 2

sum 0.77

device 3

sum 1.52

device 4

sum 1.27

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.25× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

The whole batch, routed three ways: which rule keeps device 1’s load down?

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 2

Parameters: `{"t": 7.35}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 2.9

bound 4×

1

2

3

4

mean

max 1.82× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.47

device 2

sum 1.37

device 3

sum 1.21

device 4

sum 1.55

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.18× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

Group-limited routing keeps this token on two devices where top-k spreads it wider; one expert per device sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 3

Parameters: `{"seed": 1, "t": 0}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

2 of 4 , mean so far 2.5

bound 4×

1

2

3

4

mean

max 1.88× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.66

device 2

sum 1.59

device 3

sum 0.96

device 4

sum 0.86

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.03× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

The whole batch, routed three ways: which rule keeps device 1’s load down?

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 4

Parameters: `{"seed": 10.5, "t": 0}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

2 of 4 , mean so far 2.8

bound 4×

1

2

3

4

mean

max 1.88× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.73

device 2

sum 0.95

device 3

sum 1.22

device 4

sum 1.28

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.22× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

The whole batch, routed three ways: which rule keeps device 1’s load down?

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 5

Parameters: `{"seed": 20, "t": 0}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 2.7

bound 4×

1

2

3

4

mean

max 1.75× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.68

device 2

sum 1.68

device 3

sum 1.13

device 4

sum 1.50

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.03× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

The whole batch, routed three ways: which rule keeps device 1’s load down?

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 6

Parameters: `{"t": 1.5}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 3.0

bound 4×

1

2

3

4

mean

max 2.00× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.51

device 2

sum 1.24

device 3

sum 1.44

device 4

sum 1.23

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.00× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

Group-limited routing keeps this token on two devices where top-k spreads it wider; one expert per device sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 7

Parameters: `{"t": 4}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

2 of 4 , mean so far 3.0

bound 4×

1

2

3

4

mean

max 1.88× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.76

device 2

sum 1.67

device 3

sum 1.25

device 4

sum 0.72

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.25× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

This token reaches as many devices either way, though group-limited routing may pick other ones; one expert per device still sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 8

Parameters: `{"t": 4.7}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 2.9

bound 4×

1

2

3

4

mean

max 1.90× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.75

device 2

sum 1.43

device 3

sum 1.25

device 4

sum 1.55

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.20× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

Group-limited routing keeps this token on two devices where top-k spreads it wider; one expert per device sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 9

Parameters: `{"t": 5.8}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

2 of 4 , mean so far 2.8

bound 4×

1

2

3

4

mean

max 2.00× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.61

device 2

sum 0.97

device 3

sum 1.46

device 4

sum 1.26

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.23× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

This token reaches as many devices either way, though group-limited routing may pick other ones; one expert per device still sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 10

Parameters: `{"t": 6.1}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

4 of 4 , mean so far 2.9

bound 4×

1

2

3

4

mean

max 1.93× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.56

device 2

sum 1.22

device 3

sum 1.09

device 4

sum 1.12

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.29× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

Group-limited routing keeps this token on two devices where top-k spreads it wider; one expert per device sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 11

Parameters: `{"t": 6.8}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

2 of 4 , mean so far 2.9

bound 4×

1

2

3

4

mean

max 1.88× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.87

device 2

sum 1.81

device 3

sum 1.20

device 4

sum 1.49

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.19× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

This token reaches as many devices either way, though group-limited routing may pick other ones; one expert per device still sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 12

Parameters: `{"t": 9.3}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

2 of 4 , mean so far 2.9

bound 4×

1

2

3

4

mean

max 1.87× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.78

device 2

sum 0.78

device 3

sum 1.12

device 4

sum 1.43

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.26× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

This token reaches as many devices either way, though group-limited routing may pick other ones; one expert per device still sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 13

Parameters: `{"t": 9.6}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 2.9

bound 4×

1

2

3

4

mean

max 1.88× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.65

device 2

sum 1.22

device 3

sum 1.08

device 4

sum 1.21

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.25× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

Group-limited routing keeps this token on two devices where top-k spreads it wider; one expert per device sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 14

Parameters: `{"t": 10.7}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

2 of 4 , mean so far 2.9

bound 4×

1

2

3

4

mean

max 1.93× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.82

device 2

sum 1.50

device 3

sum 1.20

device 4

sum 1.37

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.26× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

This token reaches as many devices either way, though group-limited routing may pick other ones; one expert per device still sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 15

Parameters: `{"t": 11.4}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 2.9

bound 4×

1

2

3

4

mean

max 1.90× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.35

device 2

sum 1.35

device 3

sum 1.57

device 4

sum 1.50

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.21× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

Group-limited routing keeps this token on two devices where top-k spreads it wider; one expert per device sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 16

Parameters: `{"t": 11.7}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

2 of 4 , mean so far 2.8

bound 4×

1

2

3

4

mean

max 1.93× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.77

device 2

sum 0.78

device 3

sum 1.33

device 4

sum 1.46

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.23× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

This token reaches as many devices either way, though group-limited routing may pick other ones; one expert per device still sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 17

Parameters: `{"t": 12.4}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 2.8

bound 4×

1

2

3

4

mean

max 1.97× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.65

device 2

sum 0.77

device 3

sum 1.52

device 4

sum 1.27

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.25× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

Group-limited routing keeps this token on two devices where top-k spreads it wider; one expert per device sends it to all of them.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

## Sample 18

Parameters: `{"t": 12.8}`

Expert-parallel routing: fewer devices per token, or even load?

this token’s scores:  selected,  masked device

devices it is sent to

load per device, tokens so far: busiest

expert combinations allowed

Standard top-k

top-k over all N experts (DeepSeek-V4, Kimi K2, GLM-4.5)

device 1

device 2

device 3

device 4

uniform at V3’s shape: 5.3 of 8

3 of 4 , mean so far 2.8

bound 4×

1

2

3

4

mean

max 1.97× mean

1,820

Group-limited

top-M devices by the sum of their top-k/M scores, then top-k inside them (DeepSeek-V3, Ling 2.0)

device 1

sum 1.65

device 2

sum 0.77

device 3

sum 1.52

device 4

sum 1.27

at V3’s shape: at most 4 of 8

2 of 4 , mean so far 2.0

bound 4×

1

2

3

4

mean

max 2.25× mean

at V3’s shape: 17.5%

412 of 1,820

Grouped experts (MoGE)

top-k/G inside every device (Pangu Pro MoE, Intern-S1-Pro)

device 1

device 2

device 3

device 4

4 of 4 , mean so far 4.0

bound 4×

1

2

3

4

max 1.00× mean

at Pangu’s shape: 1/264

256 of 1,820

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.

On this batch, limiting the devices does not relieve device 1, while one expert per device gives every device the same load on any batch; both rules shrink the expert combinations a token can choose from.

N \= 16 experts on G \= 4 devices, k \= 4 experts per token and M \= 2 devices kept (M \= G/2 and k \= 2M, as in DeepSeek-V3). The batch leans toward device 1’s experts.
