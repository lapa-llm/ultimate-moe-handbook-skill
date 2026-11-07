# router-authority

[Interactive original](../upstream/app/public/viz/index.html?c=router-authority) · [Poster](../upstream/app/public/viz/posters/router-authority.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/router-authority-DOou3o9r.js)

## Controls

```json
{
  "seed": {
    "min": 1,
    "max": 20,
    "step": 1,
    "value": 2,
    "label": "seed",
    "hidden": true
  }
}
```

Animation duration: 13 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.26

.26

.24

.26

.27

.21

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.41

.24

.37

.14

.21

.13

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

pad the

pad pad the

pad pad pad the

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The first “the”: its token id alone fixes the hash layer’s six experts; the learned router reads its context too.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 2

Parameters: `{"t": 6.5}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.26

.21

.24

.26

.23

.31

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.24

.27

.18

.30

.35

.17

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

mat and

the mat and

on the mat and

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The learned router scores this word in its context; the hash layer looks its experts up by token id.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 3

Parameters: `{"seed": 1, "t": 0}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.26

.24

.22

.23

.29

.26

score s

weight w

each “the”

overlap 0.71

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.15

.34

.23

.28

.37

.13

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

pad the

pad pad the

pad pad pad the

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The first “the”: its token id alone fixes the hash layer’s six experts; the learned router reads its context too.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 4

Parameters: `{"seed": 10.5, "t": 0}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.27

.22

.24

.26

.24

.28

score s

weight w

each “the”

overlap 0.54

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.32

.26

.17

.36

.14

.26

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

pad the

pad pad the

pad pad pad the

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The first “the”: its token id alone fixes the hash layer’s six experts; the learned router reads its context too.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 5

Parameters: `{"seed": 20, "t": 0}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.28

.29

.18

.18

.30

.27

score s

weight w

each “the”

overlap 0.64

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.18

.12

.26

.09

.45

.40

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

pad the

pad pad the

pad pad pad the

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The first “the”: its token id alone fixes the hash layer’s six experts; the learned router reads its context too.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 6

Parameters: `{"t": 1.1}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.26

.25

.27

.22

.28

.23

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.20

.21

.31

.34

.27

.17

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

the cat

pad the cat

pad pad the cat

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The learned router scores this word in its context; the hash layer looks its experts up by token id.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 7

Parameters: `{"t": 4}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.25

.23

.20

.26

.33

.24

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.38

.26

.42

.17

.15

.11

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

on the

sat on the

cat sat on the

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

Another “the”: the hash layer gives it the same experts, the learned router chooses by context, and Engram looks up its own n-grams.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 8

Parameters: `{"t": 5.1}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.22

.31

.24

.28

.20

.26

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.35

.22

.16

.32

.15

.29

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

the mat

on the mat

sat on the mat

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The learned router scores this word in its context; the hash layer looks its experts up by token id.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 9

Parameters: `{"t": 7.1}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.30

.20

.24

.24

.27

.24

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.43

.35

.35

.17

.11

.09

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

and the

mat and the

the mat and the

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

Another “the”: the hash layer gives it the same experts, the learned router chooses by context, and Engram looks up its own n-grams.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 10

Parameters: `{"t": 8.1}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.27

.29

.20

.31

.19

.25

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.18

.29

.28

.24

.26

.26

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

the dog

and the dog

mat and the dog

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The learned router scores this word in its context; the hash layer looks its experts up by token id.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 11

Parameters: `{"t": 11.1}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.25

.25

.23

.32

.22

.23

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.43

.28

.40

.15

.14

.11

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

to the

ran to the

dog ran to the

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

Another “the”: the hash layer gives it the same experts, the learned router chooses by context, and Engram looks up its own n-grams.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

## Sample 12

Parameters: `{"t": 12.1}`

Learned or hash routing: what selects each token’s experts?

the cat sat on the mat and the dog ran to the door

used by the bold tokenused by another “the”

Learned router
experts \= top-6 of s \+ b, w \= 1.5 · s / Σtop-6 s (DeepSeek-V4-Flash layers 3 to 42\)

.26

.30

.21

.21

.23

.28

score s

weight w

each “the”

overlap 0.69

chance 0.24

Hash layer
experts \= tid2eid\[token id\], w \= 1.5 · s / Σexperts s (DeepSeek-V4-Flash layers 0 to 2\)

.25

.23

.19

.40

.21

.23

score s

weight w

each “the”

overlap 1

Engram
rows \= table\[hash(last 2 to 4 canonical token ids)\] (DeepSeek-V4.1-Flash layers 1 and 14\)

project, gate

attention

MoE, learned router

the door

to the door

ran to the door

residual

table rows

each “the”

overlap 0

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.

The last word: the hash layer gave all four “the”s the same six experts, which neither context nor a bias can move; Engram, which V4.1-Flash keeps, picks no experts.

16 of V4-Flash’s 256 experts, with one router matrix for both routing rows. 1.5 is V4-Flash’s routed scaling factor, b the balancing bias (0 here), and overlap the mean Jaccard similarity of the four “the”s’ sets.
