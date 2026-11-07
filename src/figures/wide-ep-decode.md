# wide-ep-decode

[Interactive original](../upstream/app/public/viz/index.html?c=wide-ep-decode) · [Poster](../upstream/app/public/viz/posters/wide-ep-decode.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/wide-ep-decode-B6RiZm4Q.js)

## Controls

```json
{
  "req": {
    "min": 8,
    "max": 256,
    "step": 8,
    "value": 64,
    "label": "requests per GPU"
  }
}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

What does wider expert parallelism buy in decode?

DeepSeek-V4.1-Flash, 384 routed experts, context 131,072 tokens, redrawn from DeepSeek’s DeepInfer benchmark

tokens per second per GPU

dots labelled by requests per GPU

0

10,000

20,000

0

100

200

300

tokens per second per user

EP64 \+25%

8

16

32

64

128

256

EP64, 7 routed experts per GPU

8

16

32

64

128

256

EP8, 52 routed experts per GPU

Each dot is one decode benchmark read off DeepSeek’s published chart, whose token rates are measured decode steps per second times the tokens a step yields at an assumed draft-token acceptance, a factor that leaves the ratio between the runs unchanged. Going from EP8 to EP64 cuts the experts each GPU holds, and at the same requests per GPU EP64 decodes faster per GPU and per user, more so at fewer requests.

## Sample 2

Parameters: `{"req": 8, "t": 0}`

What does wider expert parallelism buy in decode?

DeepSeek-V4.1-Flash, 384 routed experts, context 131,072 tokens, redrawn from DeepSeek’s DeepInfer benchmark

tokens per second per GPU

dots labelled by requests per GPU

0

10,000

20,000

0

100

200

300

tokens per second per user

EP64 \+36%

8

16

32

64

128

256

EP64, 7 routed experts per GPU

8

16

32

64

128

256

EP8, 52 routed experts per GPU

Each dot is one decode benchmark read off DeepSeek’s published chart, whose token rates are measured decode steps per second times the tokens a step yields at an assumed draft-token acceptance, a factor that leaves the ratio between the runs unchanged. Going from EP8 to EP64 cuts the experts each GPU holds, and at the same requests per GPU EP64 decodes faster per GPU and per user, more so at fewer requests.

## Sample 3

Parameters: `{"req": 132, "t": 0}`

What does wider expert parallelism buy in decode?

DeepSeek-V4.1-Flash, 384 routed experts, context 131,072 tokens, redrawn from DeepSeek’s DeepInfer benchmark

tokens per second per GPU

dots labelled by requests per GPU

0

10,000

20,000

0

100

200

300

tokens per second per user

EP64 \+19%

8

16

32

64

128

256

EP64, 7 routed experts per GPU

8

16

32

64

128

256

EP8, 52 routed experts per GPU

Each dot is one decode benchmark read off DeepSeek’s published chart, whose token rates are measured decode steps per second times the tokens a step yields at an assumed draft-token acceptance, a factor that leaves the ratio between the runs unchanged. Going from EP8 to EP64 cuts the experts each GPU holds, and at the same requests per GPU EP64 decodes faster per GPU and per user, more so at fewer requests.

## Sample 4

Parameters: `{"req": 256, "t": 0}`

What does wider expert parallelism buy in decode?

DeepSeek-V4.1-Flash, 384 routed experts, context 131,072 tokens, redrawn from DeepSeek’s DeepInfer benchmark

tokens per second per GPU

dots labelled by requests per GPU

0

10,000

20,000

0

100

200

300

tokens per second per user

EP64 \+6%

8

16

32

64

128

256

EP64, 7 routed experts per GPU

8

16

32

64

128

256

EP8, 52 routed experts per GPU

Each dot is one decode benchmark read off DeepSeek’s published chart, whose token rates are measured decode steps per second times the tokens a step yields at an assumed draft-token acceptance, a factor that leaves the ratio between the runs unchanged. Going from EP8 to EP64 cuts the experts each GPU holds, and at the same requests per GPU EP64 decodes faster per GPU and per user, more so at fewer requests.
