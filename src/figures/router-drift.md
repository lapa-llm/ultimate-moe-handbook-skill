# router-drift

[Interactive original](../upstream/app/public/viz/index.html?c=router-drift) · [Poster](../upstream/app/public/viz/posters/router-drift.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/router-drift-BOeh_-Iq.js)

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

Animation duration: 14 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.03

.20

.08

.69

softmax

weight

38%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.21

.25

.44

.11

softmax

weight

32%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.02

.20

.08

.70

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 30 of 30\. The last step: routing replay runs the rollout’s experts, while freezing the router leaves part of the mismatch, so only replay trains the experts the rollout actually ran.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 2

Parameters: `{"t": 7}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.07

.06

.08

.79

softmax

weight

34%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.09

.53

.26

.12

softmax

weight

33%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.06

.83

.06

.05

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 16 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 3

Parameters: `{"t": 14}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.03

.20

.08

.69

softmax

weight

38%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.21

.25

.44

.11

softmax

weight

32%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.02

.20

.08

.70

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 30 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 4

Parameters: `{"seed": 1, "t": 0}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.02

.93

.02

.04

softmax

weight

37%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.17

.63

.10

.11

softmax

weight

27%

RL step

numerics alone 9%



0%

mean 28%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.93

.02

.04

.01

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 30 of 30\. The last step: routing replay runs the rollout’s experts, while freezing the router leaves part of the mismatch, so only replay trains the experts the rollout actually ran.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 5

Parameters: `{"seed": 10.5, "t": 0}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.10

.69

.13

.09

softmax

weight

40%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.20

.17

.17

.46

softmax

weight

36%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.71

.13

.07

.09

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 30 of 30\. The last step: routing replay runs the rollout’s experts, while freezing the router leaves part of the mismatch, so only replay trains the experts the rollout actually ran.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 6

Parameters: `{"seed": 20, "t": 0}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.81

.04

.09

.06

softmax

weight

41%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.72

.09

.12

.07

softmax

weight

25%

RL step

numerics alone 10%



0%

mean 29%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.81

.04

.09

.06

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 30 of 30\. The last step: routing replay runs the rollout’s experts, while freezing the router leaves part of the mismatch, so only replay trains the experts the rollout actually ran.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 7

Parameters: `{"t": 1.5}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.11

.07

.30

.51

softmax

weight

40%

RL step



0%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.08

.10

.32

.50

softmax

weight

32%

RL step

numerics alone 10%



0%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.12

.31

.04

.53

softmax

weight

0%

RL step



0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 1 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 8

Parameters: `{"t": 1.9}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.13

.31

.37

.19

softmax

weight

39%

RL step



0%

mean 40%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.13

.32

.35

.19

softmax

weight

31%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.31

.37

.12

.19

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 2 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 9

Parameters: `{"t": 2.2}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.08

.07

.27

.59

softmax

weight

38%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.10

.25

.12

.53

softmax

weight

33%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.08

.06

.27

.59

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 3 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 10

Parameters: `{"t": 2.6}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.07

.07

.33

.53

softmax

weight

40%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.12

.35

.15

.38

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.04

.08

.34

.54

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 4 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 11

Parameters: `{"t": 2.9}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.07

.07

.30

.57

softmax

weight

36%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.10

.23

.12

.55

softmax

weight

33%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.06

.30

.06

.58

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 5 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 12

Parameters: `{"t": 3.3}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.09

.09

.41

.41

softmax

weight

37%

RL step



0%

mean 38%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.10

.28

.15

.47

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.04

.07

.44

.45

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 6 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 13

Parameters: `{"t": 3.6}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.12

.38

.15

.35

softmax

weight

39%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.10

.29

.25

.35

softmax

weight

33%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.11

.13

.39

.37

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 7 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 14

Parameters: `{"t": 4}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.24

.42

.18

.17

softmax

weight

38%

RL step



0%

mean 38%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.34

.32

.17

.16

softmax

weight

31%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.27

.46

.07

.20

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 8 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 15

Parameters: `{"t": 4.3}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.06

.08

.70

.16

softmax

weight

40%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.06

.51

.11

.32

softmax

weight

31%

RL step

numerics alone 10%



0%

mean 32%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.08

.71

.05

.16

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 9 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 16

Parameters: `{"t": 4.7}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.05

.80

.05

.10

softmax

weight

38%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.07

.53

.11

.29

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.05

.04

.81

.10

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 10 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 17

Parameters: `{"t": 5.1}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.06

.05

.80

.09

softmax

weight

42%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.06

.57

.09

.27

softmax

weight

28%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.06

.80

.04

.09

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 11 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 18

Parameters: `{"t": 5.4}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.07

.82

.05

.06

softmax

weight

40%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.09

.57

.15

.20

softmax

weight

28%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.05

.84

.05

.06

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 12 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 19

Parameters: `{"t": 5.8}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.06

.81

.06

.06

softmax

weight

42%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.09

.64

.15

.12

softmax

weight

31%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.03

.06

.84

.06

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 13 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 20

Parameters: `{"t": 6.1}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.09

.09

.69

.13

softmax

weight

39%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.12

.39

.32

.17

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.09

.71

.13

.07

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 14 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 21

Parameters: `{"t": 6.5}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.06

.81

.07

.06

softmax

weight

38%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.09

.53

.22

.16

softmax

weight

26%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.05

.07

.82

.07

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 15 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 22

Parameters: `{"t": 7.2}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.09

.11

.66

.14

softmax

weight

40%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.13

.38

.32

.17

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.07

.10

.12

.71

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 17 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 23

Parameters: `{"t": 7.5}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.17

.14

.55

.14

softmax

weight

43%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.11

.35

.44

.10

softmax

weight

29%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.11

.15

.59

.15

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 18 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 24

Parameters: `{"t": 7.9}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.23

.47

.16

.14

softmax

weight

37%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.13

.51

.17

.19

softmax

weight

29%

RL step

numerics alone 10%



0%

mean 31%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.24

.50

.11

.14

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 19 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 25

Parameters: `{"t": 8.2}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.12

.23

.58

.07

softmax

weight

38%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.12

.41

.33

.14

softmax

weight

26%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.24

.06

.62

.08

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 20 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 26

Parameters: `{"t": 8.6}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.16

.24

.09

.51

softmax

weight

33%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.11

.44

.36

.10

softmax

weight

28%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.16

.24

.52

.07

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 21 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 27

Parameters: `{"t": 8.9}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.21

.36

.31

.11

softmax

weight

42%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.11

.33

.47

.10

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.22

.37

.09

.32

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 22 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 28

Parameters: `{"t": 9.3}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.56

.16

.16

.13

softmax

weight

40%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.15

.55

.15

.15

softmax

weight

28%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.09

.14

.60

.17

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 23 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 29

Parameters: `{"t": 9.6}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.13

.64

.08

.15

softmax

weight

37%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.08

.61

.24

.06

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.06

.07

.71

.17

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 24 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 30

Parameters: `{"t": 10}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.12

.10

.58

.20

softmax

weight

33%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.10

.09

.57

.23

softmax

weight

29%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.10

.60

.09

.21

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 25 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 31

Parameters: `{"t": 10.3}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.14

.50

.12

.25

softmax

weight

37%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.22

.08

.36

.35

softmax

weight

28%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.14

.08

.52

.26

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 26 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 32

Parameters: `{"t": 10.7}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.09

.36

.12

.44

softmax

weight

42%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.18

.34

.40

.08

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.09

.07

.38

.46

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 27 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 33

Parameters: `{"t": 11}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.06

.32

.14

.48

softmax

weight

41%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.12

.09

.31

.49

softmax

weight

30%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.06

.32

.14

.49

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 28 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

## Sample 34

Parameters: `{"t": 11.4}`

Router freezing or routing replay: which matches the rollout’s experts?

a token the trainer’s own routing mismatches:  
the trainer’s softmax(W·x)

experts the trainer runs
rollout engine’s top-4

routing mismatch: share of the 512 tokens whose experts differ from the rollout’s

Trainer’s own routing

the trainer’s own top-4 of softmax(W·x) (Kimi K2.5, Mellum 2: ratio correction or masking only)

.03

.18

.08

.71

softmax

weight

36%

RL step



0%

mean 39%

Frozen router

W frozen for RL, top-4 of softmax(W·x) while x still trains (Nemotron 3 Super and Ultra async RL recipes)

.18

.25

.46

.11

softmax

weight

31%

RL step

numerics alone 10%



0%

mean 30%

Routing replay

the rollout’s top-4 indices, weights from the trainer’s softmax(W·x) (DeepSeek-V3.2, MiMo-V2-Flash, Instella-MoE)

.03

.18

.08

.71

softmax

weight

0%

RL step



mean 0%

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.

RL step 29 of 30\. Each RL step, the rollout engine routes with weights from one update earlier, and the trainer’s router keeps learning unless it is frozen.

x is the router input and W the router matrix. Rollout numerics and one update are each set to the mismatch R3 and GSPO measured on Qwen3-30B-A3B, the update split equally between W and x (assumed). The sigmoid scores most listed models use pick the same top-k as this softmax before a balancing bias or a group limit (DeepSeek-V3.2 keeps 4 of 8 groups); the Nemotron recipes keep updating that bias.
