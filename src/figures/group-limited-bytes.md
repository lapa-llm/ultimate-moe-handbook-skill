# group-limited-bytes

[Interactive original](../upstream/app/public/viz/index.html?c=group-limited-bytes) · [Poster](../upstream/app/public/viz/posters/group-limited-bytes.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/group-limited-bytes-v9JuZXHP.js)

## Controls

```json
{
  "lognodes": {
    "min": 1,
    "max": 3,
    "step": 1,
    "value": 1,
    "label": "nodes = 2 to the power"
  }
}
```

Animation duration: 25 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

When does group-limited routing cut inter-node traffic?

this token's experts copy sent across nodescopy over NVLinkDeepEP relay GPUnode masked by the cap

this token’s copies, from GPU 1 of node 1 (dot); 4 experts per GPU

nodes holding its experts

hidden-state bytes sent across nodes per token

alltoall, no cap

one copy per selected expert; top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

20 KiB

16.0 KiB

alltoall, group-limited

keep the best 1 of 2 nodes by the sum of their top-8 scores, then top-8 inside them (DeepSeek-V3 keeps 4 of 8 nodes)

node 1

sum 6.99

node 2

sum 7.29

this token 1 of 2

mean 1.0

32 KiB

16.0 KiB

DeepEP, no cap

one copy per remote destination node, relayed over NVLink inside it (normal kernels); top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

4 KiB

4.0 KiB

DeepEP, group-limited

the same node cap on the same token

node 1

node 2

this token 1 of 2

mean 1.0

4 KiB

2.0 KiB

0

16

32 KiB, all 8 copies

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

EP16 over 2 nodes. With the cap, DeepEP sends as many copies of this token across nodes, alltoall more.

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

## Sample 2

Parameters: `{"t": 12.5}`

When does group-limited routing cut inter-node traffic?

this token's experts copy sent across nodescopy over NVLinkDeepEP relay GPUnode masked by the cap

this token’s copies, from GPU 1 of node 1 (dot); 4 experts per GPU

nodes holding its experts

hidden-state bytes sent across nodes per token

alltoall, no cap

one copy per selected expert; top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

20 KiB

16.0 KiB

alltoall, group-limited

keep the best 1 of 2 nodes by the sum of their top-8 scores, then top-8 inside them (DeepSeek-V3 keeps 4 of 8 nodes)

node 1

sum 6.39

node 2

sum 7.01

this token 1 of 2

mean 1.0

32 KiB

16.0 KiB

DeepEP, no cap

one copy per remote destination node, relayed over NVLink inside it (normal kernels); top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

4 KiB

4.0 KiB

DeepEP, group-limited

the same node cap on the same token

node 1

node 2

this token 1 of 2

mean 1.0

4 KiB

2.0 KiB

0

16

32 KiB, all 8 copies

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

EP16 over 2 nodes. With the cap, DeepEP sends as many copies of this token across nodes, alltoall more.

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

## Sample 3

Parameters: `{"lognodes": 2, "t": 0}`

When does group-limited routing cut inter-node traffic?

this token's experts copy sent across nodescopy over NVLinkDeepEP relay GPUnode masked by the cap

this token’s copies, from GPU 1 of node 1 (dot); 2 experts per GPU

nodes holding its experts

hidden-state bytes sent across nodes per token

alltoall, no cap

one copy per selected expert; top-8 of all 64

node 1

node 2

node 3

node 4

this token 2 of 4

mean 3.7

20 KiB

24.0 KiB

alltoall, group-limited

keep the best 2 of 4 nodes by the sum of their top-4 scores, then top-8 inside them (DeepSeek-V3 keeps 4 of 8 nodes)

node 1

sum 3.67

node 2

sum 3.21

node 3

sum 3.21

node 4

sum 3.84

this token 2 of 4

mean 2.0

20 KiB

24.0 KiB

DeepEP, no cap

one copy per remote destination node, relayed over NVLink inside it (normal kernels); top-8 of all 64

node 1

node 2

node 3

node 4

this token 2 of 4

mean 3.7

4 KiB

11.0 KiB

DeepEP, group-limited

the same node cap on the same token

node 1

node 2

node 3

node 4

this token 2 of 4

mean 2.0

4 KiB

6.0 KiB

0

16

32 KiB, all 8 copies

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

EP32 over 4 nodes. The cap leaves this token’s cross-node copies unchanged.

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

## Sample 4

Parameters: `{"lognodes": 3, "t": 0}`

When does group-limited routing cut inter-node traffic?

this token's experts copy sent across nodescopy over NVLinkDeepEP relay GPUnode masked by the cap

this token’s copies, from GPU 1 of node 1 (dot); one expert per GPU

nodes holding its experts

hidden-state bytes sent across nodes per token

alltoall, no cap

one copy per selected expert; top-8 of all 64

node 1

node 2

node 3

node 4

node 5

node 6

node 7

node 8

this token 3 of 8

mean 5.4

32 KiB

28.0 KiB

alltoall, group-limited

keep the best 4 of 8 nodes by the sum of their top-2 scores, then top-8 inside them (DeepSeek-V3 keeps 4 of 8 nodes)

node 1

sum 1.71

node 2

sum 1.91

node 3

sum 1.59

node 4

sum 1.57

node 5

sum 1.27

node 6

sum 1.68

node 7

sum 1.91

node 8

sum 1.94

this token 3 of 8

mean 4.0

32 KiB

28.0 KiB

DeepEP, no cap

one copy per remote destination node, relayed over NVLink inside it (normal kernels); top-8 of all 64

node 1

node 2

node 3

node 4

node 5

node 6

node 7

node 8

this token 3 of 8

mean 5.4

12 KiB

19.0 KiB

DeepEP, group-limited

the same node cap on the same token

node 1

node 2

node 3

node 4

node 5

node 6

node 7

node 8

this token 3 of 8

mean 4.0

12 KiB

13.9 KiB

0

16

32 KiB, all 8 copies

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

EP64 over 8 nodes. The cap leaves this token’s cross-node copies unchanged.

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

## Sample 5

Parameters: `{"t": 5.1}`

When does group-limited routing cut inter-node traffic?

this token's experts copy sent across nodescopy over NVLinkDeepEP relay GPUnode masked by the cap

this token’s copies, from GPU 1 of node 1 (dot); 4 experts per GPU

nodes holding its experts

hidden-state bytes sent across nodes per token

alltoall, no cap

one copy per selected expert; top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

12 KiB

16.0 KiB

alltoall, group-limited

keep the best 1 of 2 nodes by the sum of their top-8 scores, then top-8 inside them (DeepSeek-V3 keeps 4 of 8 nodes)

node 1

sum 7.26

node 2

sum 7.19

this token 1 of 2

mean 1.0

0 KiB

16.0 KiB

DeepEP, no cap

one copy per remote destination node, relayed over NVLink inside it (normal kernels); top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

4 KiB

4.0 KiB

DeepEP, group-limited

the same node cap on the same token

node 1

node 2

this token 1 of 2

mean 1.0

0 KiB

2.0 KiB

0

16

32 KiB, all 8 copies

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

EP16 over 2 nodes. With the cap, DeepEP sends fewer copies of this token across nodes, alltoall fewer.

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

## Sample 6

Parameters: `{"t": 7.6}`

When does group-limited routing cut inter-node traffic?

this token's experts copy sent across nodescopy over NVLinkDeepEP relay GPUnode masked by the cap

this token’s copies, from GPU 1 of node 1 (dot); 4 experts per GPU

nodes holding its experts

hidden-state bytes sent across nodes per token

alltoall, no cap

one copy per selected expert; top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

20 KiB

16.0 KiB

alltoall, group-limited

keep the best 1 of 2 nodes by the sum of their top-8 scores, then top-8 inside them (DeepSeek-V3 keeps 4 of 8 nodes)

node 1

sum 6.80

node 2

sum 6.98

this token 1 of 2

mean 1.0

32 KiB

16.0 KiB

DeepEP, no cap

one copy per remote destination node, relayed over NVLink inside it (normal kernels); top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

4 KiB

4.0 KiB

DeepEP, group-limited

the same node cap on the same token

node 1

node 2

this token 1 of 2

mean 1.0

4 KiB

2.0 KiB

0

16

32 KiB, all 8 copies

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

EP16 over 2 nodes. With the cap, DeepEP sends as many copies of this token across nodes, alltoall more.

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

## Sample 7

Parameters: `{"t": 15.1}`

When does group-limited routing cut inter-node traffic?

this token's experts copy sent across nodescopy over NVLinkDeepEP relay GPUnode masked by the cap

this token’s copies, from GPU 1 of node 1 (dot); 4 experts per GPU

nodes holding its experts

hidden-state bytes sent across nodes per token

alltoall, no cap

one copy per selected expert; top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

8 KiB

16.0 KiB

alltoall, group-limited

keep the best 1 of 2 nodes by the sum of their top-8 scores, then top-8 inside them (DeepSeek-V3 keeps 4 of 8 nodes)

node 1

sum 7.41

node 2

sum 6.53

this token 1 of 2

mean 1.0

0 KiB

16.0 KiB

DeepEP, no cap

one copy per remote destination node, relayed over NVLink inside it (normal kernels); top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

4 KiB

4.0 KiB

DeepEP, group-limited

the same node cap on the same token

node 1

node 2

this token 1 of 2

mean 1.0

0 KiB

2.0 KiB

0

16

32 KiB, all 8 copies

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

EP16 over 2 nodes. With the cap, DeepEP sends fewer copies of this token across nodes, alltoall fewer.

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

## Sample 8

Parameters: `{"t": 22.5}`

When does group-limited routing cut inter-node traffic?

this token's experts copy sent across nodescopy over NVLinkDeepEP relay GPUnode masked by the cap

this token’s copies, from GPU 1 of node 1 (dot); 4 experts per GPU

nodes holding its experts

hidden-state bytes sent across nodes per token

alltoall, no cap

one copy per selected expert; top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

16 KiB

16.0 KiB

alltoall, group-limited

keep the best 1 of 2 nodes by the sum of their top-8 scores, then top-8 inside them (DeepSeek-V3 keeps 4 of 8 nodes)

node 1

sum 6.43

node 2

sum 6.87

this token 1 of 2

mean 1.0

32 KiB

16.0 KiB

DeepEP, no cap

one copy per remote destination node, relayed over NVLink inside it (normal kernels); top-8 of all 64

node 1

node 2

this token 2 of 2

mean 2.0

4 KiB

4.0 KiB

DeepEP, group-limited

the same node cap on the same token

node 1

node 2

this token 1 of 2

mean 1.0

4 KiB

2.0 KiB

0

16

32 KiB, all 8 copies

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.

EP16 over 2 nodes. With the cap, DeepEP sends as many copies of this token across nodes, alltoall more.

DeepEP sends one copy per destination node, the alltoall dispatcher one per selected expert. Scores here are random and ignore which node the token sits on; each mean averages 4,000 such tokens, each placed on every node in turn.
