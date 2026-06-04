---
title: NVIDIA (NIM Models)
researched: 2026-06-05
sources:
  - https://developer.nvidia.com/nim
  - https://developer.nvidia.com/ai-models
  - https://www.nvidia.com/en-us/ai/
  - https://greennode.ai/blog/greennode-nim-overview
---
# NVIDIA (NIM Models)

## Company Facts
- **Founded**: 1993
- **HQ**: Santa Clara, California
- **CEO**: Jensen Huang
- **Core Business**: GPU hardware, AI infrastructure, inference microservices (NIM)

## Model Lineup
NVIDIA's NIM (NVIDIA Inference Microservices) is not a model family but an inference platform that hosts models from multiple providers:

| Model | Developer | NVIDIA Optimization |
|-------|-----------|---------------------|
| DeepSeek R1/V3.2 | DeepSeek | 15x speedup on GB200 over H200; FP4 quantized |
| gpt-oss 20B/120B | OpenAI | 10x inference speedup on Blackwell; 1.5M TPS on GB200 NVL72 |
| Kimi K2 | Moonshot AI | 10x speedup on GB200 NVL72; NVFP4 quantized; 140+ TPS on B200 |
| Llama 4 | Meta | 3x throughput boost with speculative decoding; FP8 quantized |
| Nemotron (Nano/Super/Ultra) | NVIDIA | FP4 on B200 → 6x throughput vs. FP8 on H100 |
| Qwen3 | Alibaba | 50x better agentic AI perf on Blackwell Ultra |
| Gemma 3n | Google DeepMind | Runs on Jetson, RTX, data center |
| Phi-4 | Microsoft | Jetson/RTX optimized |

### NVIDIA's Own Models: Nemotron
- **Nemotron Nano**: Edge-optimized agentic model
- **Nemotron Super**: Mid-size reasoning model
- **Nemotron Ultra**: Datacenter-scale reasoning and agentic AI

## Capabilities
- **Inference Optimization**: TensorRT-LLM, vLLM, SGLang pre-integrated
- **Quantization**: TensorRT Model Optimizer supports FP4, INT4, NVFP4
- **Deployment**: Self-hosted containers, Kubernetes (Helm charts), cloud endpoints
- **API Compatibility**: OpenAI-compatible API endpoints via NIM
- **Edge Deployment**: Jetson AI Lab, Ollama, llama.cpp, ChatRTX
- **AI Blueprints**: Pre-built RAG, agentic workflows via NVIDIA Launchables
- **AgentIQ Toolkit**: Developer toolkit for building AI agent workflows

## Key Facts
1. NVIDIA NIM provides GPU-accelerated, self-hostable microservices for deploying pretrained and customized AI models across RTX workstations, on-prem data centers, and cloud environments.
2. NVIDIA's AI Models catalog supports 10x+ performance gains on Blackwell (GB200 NVL72) vs. Hopper (H200) for MoE models.
3. NVIDIA Nemotron is NVIDIA's own model family optimized for agentic AI, with FP4 quantization delivering 6x throughput improvement over FP8 on H100.
4. NIM supports thousands of community fine-tuned models and custom fine-tunes with OpenAI-compatible API endpoints.
5. NVIDIA AI Enterprise provides production-grade support for self-hosted NIM deployments.

## Sources
