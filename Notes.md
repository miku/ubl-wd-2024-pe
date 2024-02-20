# Notes

GPT4 has about 51x the size (1.76T parameters) of a (quantized) model
(llama-34B) that can run on a contemporary consumer GPU (20GB VRAM).

```
llava:34b-v1.6-q4_K_S                   787b2213f0db    20 GB   18 hours ago
```

Companies (most likely) uses
[H100](https://resources.nvidia.com/en-us-dgx-systems/ai-enterprise-dgx) HW w/
640GB total VRAM (10.2kW max).
