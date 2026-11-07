# active-vs-release

[Interactive original](../upstream/app/public/viz/index.html?c=active-vs-release) · [Poster](../upstream/app/public/viz/posters/active-vs-release.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/active-vs-release-CThK37Dd.js)

## Controls

```json
{
  "top": {
    "min": 5,
    "max": 29,
    "step": 1,
    "value": 20,
    "label": "top N by index"
  }
}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Dense or MoE: which do the strongest open-weights models use?

Intelligence Index (Artificial Analysis)MoEdense

10

20

30

Mar

May

Jul

Sep 2026

release date

top 20

18 MoE, 2 dense

#28 Mistral Small 4 (Reasoning), Mistral: 4.3, 119B total, 6.5B active, released 2026-03-16

#23 Nemotron 3.5 Lightning, NVIDIA: 5.5, 31.6B total, 3.6B active, released 2026-08-11

#22 Command A\+, Cohere: 6.2, 218B total, 25B active, released 2026-05-20

#20 Nemotron 3 Ultra 550B A55B (Reasoning), NVIDIA: 11.8, 550B total, 55B active, released 2026-06-04

#19 Inkling (Xhigh), Thinking Machines: 12.5, 975B total, 41B active, released 2026-07-15

#18 Inkling Small, Thinking Machines: 12.9, 266B total, 12B active, released 2026-07-30

#17 Nemotron 3.5 Super VL, NVIDIA: 13.6, 120B total, 12B active, released 2026-10-15

#16 Beam 1.0, Reflection: 17.7, 501B total, 23B active, released 2026-10-16

#15 K2 Horizon 375B A23B, Institute of Foundation Models: 17.8, 375B total, 23B active, released 2026-09-03

#14 MiniMax-M3, MiniMax: 18.9, 428B total, 23B active, released 2026-06-01

#11 DeepSeek V4 Pro 0813 (Max), DeepSeek: 23.1, 1600B total, 49B active, released 2026-08-13

#10 Muse Spark Open (Xhigh), Meta: 24.9, 816B total, 42B active, released 2026-10-15

#9 Mistral Large 4 (High), Mistral: 26.1, 1050B total, 52B active, released 2026-10-29

#8 MiMo-V2.6-Flash, Xiaomi: 26.7, 309B total, 15B active, released 2026-09-21

#7 GLM-5.3-Flash, Z AI: 27.8, 320B total, 18B active, released 2026-08-26

#6 Step 5 Preview, StepFun: 28.5, 600B total, 27B active, released 2026-09-18

#5 MiniMax-M3.1-Flash, MiniMax: 29.1, 428B total, 23B active, released 2026-10-19

#4 Ling 3.1 Flash 1019, InclusionAI: 29.6, 560B total, 25B active, released 2026-10-22

#3 MiMo-V2.6-Pro, Xiaomi: 29.9, 1020B total, 42B active, released 2026-09-21

#2 GLM-5.3 (Max), Z AI: 31.7, 753B total, 40B active, released 2026-08-18

#1 DeepSeek V4.1 Flash 1017 (Max), DeepSeek: 32.6, 552B total, 16B active, released 2026-10-17

#29 NVIDIA Nemotron 3 Nano 4B, NVIDIA: 1.8, 3.97B dense, released 2026-03-16

#27 Gemma 4 31B (Reasoning), Google: 4.4, 30.7B dense, released 2026-04-02

#26 Mistral Medium 3.5, Mistral: 4.6, 128B dense, released 2026-04-29

#25 Granite 4.2 3B, IBM: 4.7, 3B dense, released 2026-08-25

#24 Granite 4.2 8B, IBM: 5.1, 8B dense, released 2026-08-25

#21 Muse Glimmer (High), Meta: 6.3, 30B dense, released 2026-08-10

#13 Qwen3.8 27B (Xhigh), Alibaba: 20.1, 27B dense, released 2026-08-14

#12 Nanbeige4.3-33B, Nanbeige: 20.4, 33B dense, released 2026-10-25

DeepSeek V4.1 Flash 1017 (Max), #1

GLM-5.3 (Max), #2

MiMo-V2.6-Pro, #3

Ling 3.1 Flash 1019, #4

MiniMax-M3.1-Flash, #5

Step 5 Preview, #6

GLM-5.3-Flash, #7

MiMo-V2.6-Flash, #8

Mistral Large 4 (High), #9

Muse Spark Open (Xhigh), #10

DeepSeek V4 Pro 0813 (Max), #11

Nanbeige4.3-33B, #12

Qwen3.8 27B (Xhigh), #13

MiniMax-M3, #14

K2 Horizon 375B A23B, #15

Beam 1.0, #16

Nemotron 3.5 Super VL, #17

Inkling Small, #18

Inkling (Xhigh), #19

Nemotron 3 Ultra 550B A55B (Reasoning), #20

Muse Glimmer (High), #21

Command A\+, #22

Nemotron 3.5 Lightning, #23

Granite 4.2 8B, #24

Granite 4.2 3B, #25

Mistral Medium 3.5, #26

Gemma 4 31B (Reasoning), #27

Mistral Small 4 (Reasoning), #28

NVIDIA Nemotron 3 Nano 4B, #29

Each mark is one of the strongest open-weights models by the Artificial Analysis Intelligence Index, a composite of benchmark scores, placed at the date the model was released; marks below the top 20 line are faded. Almost every mark above the line is an MoE.

## Sample 2

Parameters: `{"t": 0, "top": 5}`

Dense or MoE: which do the strongest open-weights models use?

Intelligence Index (Artificial Analysis)MoEdense

10

20

30

Mar

May

Jul

Sep 2026

release date

top 5

5 MoE, 0 dense

#28 Mistral Small 4 (Reasoning), Mistral: 4.3, 119B total, 6.5B active, released 2026-03-16

#23 Nemotron 3.5 Lightning, NVIDIA: 5.5, 31.6B total, 3.6B active, released 2026-08-11

#22 Command A\+, Cohere: 6.2, 218B total, 25B active, released 2026-05-20

#20 Nemotron 3 Ultra 550B A55B (Reasoning), NVIDIA: 11.8, 550B total, 55B active, released 2026-06-04

#19 Inkling (Xhigh), Thinking Machines: 12.5, 975B total, 41B active, released 2026-07-15

#18 Inkling Small, Thinking Machines: 12.9, 266B total, 12B active, released 2026-07-30

#17 Nemotron 3.5 Super VL, NVIDIA: 13.6, 120B total, 12B active, released 2026-10-15

#16 Beam 1.0, Reflection: 17.7, 501B total, 23B active, released 2026-10-16

#15 K2 Horizon 375B A23B, Institute of Foundation Models: 17.8, 375B total, 23B active, released 2026-09-03

#14 MiniMax-M3, MiniMax: 18.9, 428B total, 23B active, released 2026-06-01

#11 DeepSeek V4 Pro 0813 (Max), DeepSeek: 23.1, 1600B total, 49B active, released 2026-08-13

#10 Muse Spark Open (Xhigh), Meta: 24.9, 816B total, 42B active, released 2026-10-15

#9 Mistral Large 4 (High), Mistral: 26.1, 1050B total, 52B active, released 2026-10-29

#8 MiMo-V2.6-Flash, Xiaomi: 26.7, 309B total, 15B active, released 2026-09-21

#7 GLM-5.3-Flash, Z AI: 27.8, 320B total, 18B active, released 2026-08-26

#6 Step 5 Preview, StepFun: 28.5, 600B total, 27B active, released 2026-09-18

#5 MiniMax-M3.1-Flash, MiniMax: 29.1, 428B total, 23B active, released 2026-10-19

#4 Ling 3.1 Flash 1019, InclusionAI: 29.6, 560B total, 25B active, released 2026-10-22

#3 MiMo-V2.6-Pro, Xiaomi: 29.9, 1020B total, 42B active, released 2026-09-21

#2 GLM-5.3 (Max), Z AI: 31.7, 753B total, 40B active, released 2026-08-18

#1 DeepSeek V4.1 Flash 1017 (Max), DeepSeek: 32.6, 552B total, 16B active, released 2026-10-17

#29 NVIDIA Nemotron 3 Nano 4B, NVIDIA: 1.8, 3.97B dense, released 2026-03-16

#27 Gemma 4 31B (Reasoning), Google: 4.4, 30.7B dense, released 2026-04-02

#26 Mistral Medium 3.5, Mistral: 4.6, 128B dense, released 2026-04-29

#25 Granite 4.2 3B, IBM: 4.7, 3B dense, released 2026-08-25

#24 Granite 4.2 8B, IBM: 5.1, 8B dense, released 2026-08-25

#21 Muse Glimmer (High), Meta: 6.3, 30B dense, released 2026-08-10

#13 Qwen3.8 27B (Xhigh), Alibaba: 20.1, 27B dense, released 2026-08-14

#12 Nanbeige4.3-33B, Nanbeige: 20.4, 33B dense, released 2026-10-25

DeepSeek V4.1 Flash 1017 (Max), #1

GLM-5.3 (Max), #2

MiMo-V2.6-Pro, #3

Ling 3.1 Flash 1019, #4

MiniMax-M3.1-Flash, #5

Step 5 Preview, #6

GLM-5.3-Flash, #7

MiMo-V2.6-Flash, #8

Mistral Large 4 (High), #9

Muse Spark Open (Xhigh), #10

DeepSeek V4 Pro 0813 (Max), #11

Nanbeige4.3-33B, #12

Qwen3.8 27B (Xhigh), #13

MiniMax-M3, #14

K2 Horizon 375B A23B, #15

Beam 1.0, #16

Nemotron 3.5 Super VL, #17

Inkling Small, #18

Inkling (Xhigh), #19

Nemotron 3 Ultra 550B A55B (Reasoning), #20

Muse Glimmer (High), #21

Command A\+, #22

Nemotron 3.5 Lightning, #23

Granite 4.2 8B, #24

Granite 4.2 3B, #25

Mistral Medium 3.5, #26

Gemma 4 31B (Reasoning), #27

Mistral Small 4 (Reasoning), #28

NVIDIA Nemotron 3 Nano 4B, #29

Each mark is one of the strongest open-weights models by the Artificial Analysis Intelligence Index, a composite of benchmark scores, placed at the date the model was released; marks below the top 5 line are faded. Almost every mark above the line is an MoE.

## Sample 3

Parameters: `{"t": 0, "top": 17}`

Dense or MoE: which do the strongest open-weights models use?

Intelligence Index (Artificial Analysis)MoEdense

10

20

30

Mar

May

Jul

Sep 2026

release date

top 17

15 MoE, 2 dense

#28 Mistral Small 4 (Reasoning), Mistral: 4.3, 119B total, 6.5B active, released 2026-03-16

#23 Nemotron 3.5 Lightning, NVIDIA: 5.5, 31.6B total, 3.6B active, released 2026-08-11

#22 Command A\+, Cohere: 6.2, 218B total, 25B active, released 2026-05-20

#20 Nemotron 3 Ultra 550B A55B (Reasoning), NVIDIA: 11.8, 550B total, 55B active, released 2026-06-04

#19 Inkling (Xhigh), Thinking Machines: 12.5, 975B total, 41B active, released 2026-07-15

#18 Inkling Small, Thinking Machines: 12.9, 266B total, 12B active, released 2026-07-30

#17 Nemotron 3.5 Super VL, NVIDIA: 13.6, 120B total, 12B active, released 2026-10-15

#16 Beam 1.0, Reflection: 17.7, 501B total, 23B active, released 2026-10-16

#15 K2 Horizon 375B A23B, Institute of Foundation Models: 17.8, 375B total, 23B active, released 2026-09-03

#14 MiniMax-M3, MiniMax: 18.9, 428B total, 23B active, released 2026-06-01

#11 DeepSeek V4 Pro 0813 (Max), DeepSeek: 23.1, 1600B total, 49B active, released 2026-08-13

#10 Muse Spark Open (Xhigh), Meta: 24.9, 816B total, 42B active, released 2026-10-15

#9 Mistral Large 4 (High), Mistral: 26.1, 1050B total, 52B active, released 2026-10-29

#8 MiMo-V2.6-Flash, Xiaomi: 26.7, 309B total, 15B active, released 2026-09-21

#7 GLM-5.3-Flash, Z AI: 27.8, 320B total, 18B active, released 2026-08-26

#6 Step 5 Preview, StepFun: 28.5, 600B total, 27B active, released 2026-09-18

#5 MiniMax-M3.1-Flash, MiniMax: 29.1, 428B total, 23B active, released 2026-10-19

#4 Ling 3.1 Flash 1019, InclusionAI: 29.6, 560B total, 25B active, released 2026-10-22

#3 MiMo-V2.6-Pro, Xiaomi: 29.9, 1020B total, 42B active, released 2026-09-21

#2 GLM-5.3 (Max), Z AI: 31.7, 753B total, 40B active, released 2026-08-18

#1 DeepSeek V4.1 Flash 1017 (Max), DeepSeek: 32.6, 552B total, 16B active, released 2026-10-17

#29 NVIDIA Nemotron 3 Nano 4B, NVIDIA: 1.8, 3.97B dense, released 2026-03-16

#27 Gemma 4 31B (Reasoning), Google: 4.4, 30.7B dense, released 2026-04-02

#26 Mistral Medium 3.5, Mistral: 4.6, 128B dense, released 2026-04-29

#25 Granite 4.2 3B, IBM: 4.7, 3B dense, released 2026-08-25

#24 Granite 4.2 8B, IBM: 5.1, 8B dense, released 2026-08-25

#21 Muse Glimmer (High), Meta: 6.3, 30B dense, released 2026-08-10

#13 Qwen3.8 27B (Xhigh), Alibaba: 20.1, 27B dense, released 2026-08-14

#12 Nanbeige4.3-33B, Nanbeige: 20.4, 33B dense, released 2026-10-25

DeepSeek V4.1 Flash 1017 (Max), #1

GLM-5.3 (Max), #2

MiMo-V2.6-Pro, #3

Ling 3.1 Flash 1019, #4

MiniMax-M3.1-Flash, #5

Step 5 Preview, #6

GLM-5.3-Flash, #7

MiMo-V2.6-Flash, #8

Mistral Large 4 (High), #9

Muse Spark Open (Xhigh), #10

DeepSeek V4 Pro 0813 (Max), #11

Nanbeige4.3-33B, #12

Qwen3.8 27B (Xhigh), #13

MiniMax-M3, #14

K2 Horizon 375B A23B, #15

Beam 1.0, #16

Nemotron 3.5 Super VL, #17

Inkling Small, #18

Inkling (Xhigh), #19

Nemotron 3 Ultra 550B A55B (Reasoning), #20

Muse Glimmer (High), #21

Command A\+, #22

Nemotron 3.5 Lightning, #23

Granite 4.2 8B, #24

Granite 4.2 3B, #25

Mistral Medium 3.5, #26

Gemma 4 31B (Reasoning), #27

Mistral Small 4 (Reasoning), #28

NVIDIA Nemotron 3 Nano 4B, #29

Each mark is one of the strongest open-weights models by the Artificial Analysis Intelligence Index, a composite of benchmark scores, placed at the date the model was released; marks below the top 17 line are faded. Almost every mark above the line is an MoE.

## Sample 4

Parameters: `{"t": 0, "top": 29}`

Dense or MoE: which do the strongest open-weights models use?

Intelligence Index (Artificial Analysis)MoEdense

10

20

30

Mar

May

Jul

Sep 2026

release date

top 29

21 MoE, 8 dense

#28 Mistral Small 4 (Reasoning), Mistral: 4.3, 119B total, 6.5B active, released 2026-03-16

#23 Nemotron 3.5 Lightning, NVIDIA: 5.5, 31.6B total, 3.6B active, released 2026-08-11

#22 Command A\+, Cohere: 6.2, 218B total, 25B active, released 2026-05-20

#20 Nemotron 3 Ultra 550B A55B (Reasoning), NVIDIA: 11.8, 550B total, 55B active, released 2026-06-04

#19 Inkling (Xhigh), Thinking Machines: 12.5, 975B total, 41B active, released 2026-07-15

#18 Inkling Small, Thinking Machines: 12.9, 266B total, 12B active, released 2026-07-30

#17 Nemotron 3.5 Super VL, NVIDIA: 13.6, 120B total, 12B active, released 2026-10-15

#16 Beam 1.0, Reflection: 17.7, 501B total, 23B active, released 2026-10-16

#15 K2 Horizon 375B A23B, Institute of Foundation Models: 17.8, 375B total, 23B active, released 2026-09-03

#14 MiniMax-M3, MiniMax: 18.9, 428B total, 23B active, released 2026-06-01

#11 DeepSeek V4 Pro 0813 (Max), DeepSeek: 23.1, 1600B total, 49B active, released 2026-08-13

#10 Muse Spark Open (Xhigh), Meta: 24.9, 816B total, 42B active, released 2026-10-15

#9 Mistral Large 4 (High), Mistral: 26.1, 1050B total, 52B active, released 2026-10-29

#8 MiMo-V2.6-Flash, Xiaomi: 26.7, 309B total, 15B active, released 2026-09-21

#7 GLM-5.3-Flash, Z AI: 27.8, 320B total, 18B active, released 2026-08-26

#6 Step 5 Preview, StepFun: 28.5, 600B total, 27B active, released 2026-09-18

#5 MiniMax-M3.1-Flash, MiniMax: 29.1, 428B total, 23B active, released 2026-10-19

#4 Ling 3.1 Flash 1019, InclusionAI: 29.6, 560B total, 25B active, released 2026-10-22

#3 MiMo-V2.6-Pro, Xiaomi: 29.9, 1020B total, 42B active, released 2026-09-21

#2 GLM-5.3 (Max), Z AI: 31.7, 753B total, 40B active, released 2026-08-18

#1 DeepSeek V4.1 Flash 1017 (Max), DeepSeek: 32.6, 552B total, 16B active, released 2026-10-17

#29 NVIDIA Nemotron 3 Nano 4B, NVIDIA: 1.8, 3.97B dense, released 2026-03-16

#27 Gemma 4 31B (Reasoning), Google: 4.4, 30.7B dense, released 2026-04-02

#26 Mistral Medium 3.5, Mistral: 4.6, 128B dense, released 2026-04-29

#25 Granite 4.2 3B, IBM: 4.7, 3B dense, released 2026-08-25

#24 Granite 4.2 8B, IBM: 5.1, 8B dense, released 2026-08-25

#21 Muse Glimmer (High), Meta: 6.3, 30B dense, released 2026-08-10

#13 Qwen3.8 27B (Xhigh), Alibaba: 20.1, 27B dense, released 2026-08-14

#12 Nanbeige4.3-33B, Nanbeige: 20.4, 33B dense, released 2026-10-25

DeepSeek V4.1 Flash 1017 (Max), #1

GLM-5.3 (Max), #2

MiMo-V2.6-Pro, #3

Ling 3.1 Flash 1019, #4

MiniMax-M3.1-Flash, #5

Step 5 Preview, #6

GLM-5.3-Flash, #7

MiMo-V2.6-Flash, #8

Mistral Large 4 (High), #9

Muse Spark Open (Xhigh), #10

DeepSeek V4 Pro 0813 (Max), #11

Nanbeige4.3-33B, #12

Qwen3.8 27B (Xhigh), #13

MiniMax-M3, #14

K2 Horizon 375B A23B, #15

Beam 1.0, #16

Nemotron 3.5 Super VL, #17

Inkling Small, #18

Inkling (Xhigh), #19

Nemotron 3 Ultra 550B A55B (Reasoning), #20

Muse Glimmer (High), #21

Command A\+, #22

Nemotron 3.5 Lightning, #23

Granite 4.2 8B, #24

Granite 4.2 3B, #25

Mistral Medium 3.5, #26

Gemma 4 31B (Reasoning), #27

Mistral Small 4 (Reasoning), #28

NVIDIA Nemotron 3 Nano 4B, #29

Each mark is one of the strongest open-weights models by the Artificial Analysis Intelligence Index, a composite of benchmark scores, placed at the date the model was released; marks below the top 29 line are faded. Almost every mark above the line is an MoE.
