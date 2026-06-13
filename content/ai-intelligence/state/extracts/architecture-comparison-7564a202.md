title: Architecture Comparison
tags: architecture, model-design
# Architecture Comparison

## Model Architecture Types

### Dense Models
- Single FFN activated for every token
- **Providers**: OpenAI GPT-5.5, Anthropic Claude Opus 4.6, Google Gemini 3.5 Pro
- **Advantage**: Simpler, more predictable behavior; easier to quantize
- **Disadvantage**: All parameters cost compute; harder to scale beyond ~100B

### MoE Models
- Sparse FFN routing; only subset of experts activated per token
- **Providers**: DeepSeek V4 (1.6T/49B active), Meta Llama 4 (400B/17B active), Mistral Large 3 (675B/41B active), Moonshot Kimi K2 (1T/32B active)
- **Advantage**: Massive parameter count at manageable inference cost
- **Disadvantage**: Training complexity; VRAM must hold all parameters

## Attention Mechanisms

| Provider | Model | Attention Type | Key Innovation |
|----------|-------|---------------|----------------|
| DeepSeek | V4 | CSA+HCA hybrid | 4×/128× KV compression |
| Meta | Llama 4 | iRoPE | Interleaved RoPE/NoPE layers |
| Mistral | Large 3 | MLA | Multi-Head Latent Attention |
| Alibaba | Qwen3.7 | RoPE + ALiBi | Hybrid positional encoding |
| Google | Gemini 3.5 | RoPE extensions | 10M+ context support |
| NVIDIA | Nematron-5 | Flash Attention 4 | Block-sparse on Blackwell |
| OpenAI | GPT-5.5 | Proprietary | Optimized for reasoning |
| Anthropic | Claude Opus 4.6 | Proprietary | Constitution-aligned attention |
| Moonshot | Kimi K2 | MLA variant | Optimized for Chinese text |
| xAI | Grok 4.3 | RoPE | Standard with large context |

## Training Optimizers

| Provider | Optimizer | Notes |
|----------|-----------|-------|
| DeepSeek | Muon | Switched from AdamW for MoE stability |
| Meta | AdamW | Standard with Llama-specific LR schedules |
| OpenAI | Proprietary | Likely Muon/AdamW hybrid |
| Anthropic | AdamW | Constitutional AI adds complexity |
| Mistral | AdamW | Standard for open-weight |
| Google | Proprietary | RLAIF at scale requires custom optimizer |
| Moonshot | Muon | At MoE scale for Kimi K2 |
| NVIDIA | AdamW + custom | TensorRT-LLM optimized |

## Parameter Scaling

| Provider | Largest Model | Total Params | Active Params | Ratio |
|----------|--------------|-------------|--------------|-------|
| DeepSeek | V4 Pro | 1.6T | 49B | 3.1% active |
| Meta | Llama 4 Maverick | ~400B | 17B | 4.3% active |
| Mistral | Large 3 | 675B | 41B | 6.1% active |
| Moonshot | Kimi K2 | 1T | 32B | 3.2% active |
| Zhipu AI | GLM-5 | 744B | — | MoE |
| Alibaba | Qwen3.7 Max | ~1T | — | Sparse MoE |
| OpenAI | GPT-5.5 | Estimated ~2T | — | Dense (estimated) |
| Anthropic | Claude Opus 4.6 | Estimated ~1.5T | — | Dense (estimated) |

## Key Architectural Trends (2026)

1. **MoE dominance**: Most frontier models now use MoE; only OpenAI and Anthropic remain dense at the top
2. **KV compression**: DeepSeek CSA+HCA leads efficiency; others adopt similar approaches
3. **Muon optimizer**: Replacing AdamW for MoE training stability
4. **FP4 QAT**: Training with quantization awareness becoming standard
5. **Codistillation**: Meta's approach of training with teacher signal during pre-training

## Related

- [[moE-architecture]] — Detailed MoE routing and expert selection
- [[kv-cache-optimization]] — Architecture affects KV cache behavior
- [[quantization]] — QAT integrated into architecture design