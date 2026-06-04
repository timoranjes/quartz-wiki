#!/usr/bin/env python3
"""Batch inject entity header badges into all entity pages."""
import re
import os
from pathlib import Path

BASE = Path(os.path.expanduser("~/quartz-wiki/content/ai-intelligence"))

# --- Entity metadata map ---
ENTITIES = {
    # LLM Providers
    "entities/llm-providers/openai.md": {"region": "us", "pricing": "enterprise", "open_weight": "no", "entity_type": "LLM Provider", "headquarters": "San Francisco, US", "valuation": "$500B+", "models": "GPT-5.5, GPT-oss, Sora 2"},
    "entities/llm-providers/anthropic.md": {"region": "us", "pricing": "premium", "open_weight": "no", "entity_type": "LLM Provider", "headquarters": "San Francisco, US", "valuation": "$96.5B+", "models": "Claude Opus 4.8, Sonnet 4.6, Haiku 4.5"},
    "entities/llm-providers/alibaba-qwen.md": {"region": "cn", "pricing": "competitive", "open_weight": "yes", "entity_type": "LLM Provider", "headquarters": "Hangzhou, CN", "valuation": "Alibaba Group", "models": "Qwen 3.7 Max/Plus, Omni, Wan 2.7"},
    "entities/llm-providers/google-gemini.md": {"region": "us", "pricing": "competitive", "open_weight": "partial", "entity_type": "LLM Provider", "headquarters": "Mountain View, US", "valuation": "Alphabet", "models": "Gemini 2.5 Pro/Flash, Veo, Imagen"},
    "entities/llm-providers/meta-llama.md": {"region": "us", "pricing": "free", "open_weight": "yes", "entity_type": "LLM Provider", "headquarters": "Menlo Park, US", "valuation": "Meta Platforms", "models": "Llama 4 Scout/Maverick, Code Llama"},
    "entities/llm-providers/deepseek.md": {"region": "cn", "pricing": "low-cost", "open_weight": "yes", "entity_type": "LLM Provider", "headquarters": "Beijing, CN", "valuation": "DeepSeek AI", "models": "DeepSeek-V4 Pro, R1, V3"},
    "entities/llm-providers/mistral.md": {"region": "eu", "pricing": "competitive", "open_weight": "yes", "entity_type": "LLM Provider", "headquarters": "Paris, FR", "valuation": "€6B", "models": "Mistral Large, Mixtral, Codestral"},
    "entities/llm-providers/xai-grok.md": {"region": "us", "pricing": "competitive", "open_weight": "partial", "entity_type": "LLM Provider", "headquarters": "San Francisco, US", "valuation": "$80B", "models": "Grok 4, Grok Code Fast 1"},
    "entities/llm-providers/zhipu-ai.md": {"region": "cn", "pricing": "low-cost", "open_weight": "yes", "entity_type": "LLM Provider", "headquarters": "Beijing, CN", "valuation": "GLM / Zhipu AI", "models": "GLM-5.1, GLM-4, CogView"},
    "entities/llm-providers/stepfun.md": {"region": "cn", "pricing": "low-cost", "open_weight": "partial", "entity_type": "LLM Provider", "headquarters": "Beijing, CN", "valuation": "StepFun AI", "models": "Step 3, Step 2"},
    "entities/llm-providers/cohere.md": {"region": "us", "pricing": "enterprise", "open_weight": "partial", "entity_type": "LLM Provider", "headquarters": "Toronto, CA", "valuation": "$5.8B", "models": "Command A, Rerank, Embed"},
    "entities/llm-providers/stability-ai.md": {"region": "eu", "pricing": "competitive", "open_weight": "yes", "entity_type": "LLM Provider", "headquarters": "London, UK", "valuation": "Stability AI", "models": "Stable Diffusion 3.5, Stable LM"},
    "entities/llm-providers/together-ai.md": {"region": "us", "pricing": "low-cost", "open_weight": "yes", "entity_type": "Cloud Platform", "headquarters": "San Francisco, US", "valuation": "Together AI", "models": "Hosts 200+ open-source models"},
    "entities/llm-providers/minimax.md": {"region": "cn", "pricing": "low-cost", "open_weight": "no", "entity_type": "LLM Provider", "headquarters": "Shanghai, CN", "valuation": "MiniMax AI", "models": "MiniMax M2.7, Speech-02"},
    "entities/llm-providers/moonshot-ai.md": {"region": "cn", "pricing": "low-cost", "open_weight": "no", "entity_type": "LLM Provider", "headquarters": "Beijing, CN", "valuation": "Moonshot AI", "models": "Kimi K2.6, Kimi Dev"},
    "entities/llm-providers/nvidia.md": {"region": "us", "pricing": "enterprise", "open_weight": "partial", "entity_type": "Infrastructure", "headquarters": "Santa Clara, US", "valuation": "NVIDIA Corp", "models": "Nemotron, Llama Nemotron"},
    "entities/llm-providers/microsoft-phi.md": {"region": "us", "pricing": "competitive", "open_weight": "partial", "entity_type": "LLM Provider", "headquarters": "Redmond, US", "valuation": "Microsoft", "models": "Phi-4, Phi-4 Mini, Phi-3"},
    "entities/llm-providers/perplexity.md": {"region": "us", "pricing": "competitive", "open_weight": "no", "entity_type": "Search Engine", "headquarters": "San Francisco, US", "valuation": "$14B", "models": "Sonar Pro, Sonar Reasoning"},

    # Coding Agents
    "entities/coding-agents/cursor.md": {"region": "us", "pricing": "competitive", "open_weight": "no", "entity_type": "Coding Agent (IDE)", "headquarters": "San Francisco, US", "valuation": "Anysphere", "models": "Claude Sonnet 4.6, GPT-5.5, Composer 2.5"},
    "entities/coding-agents/claude-code.md": {"region": "us", "pricing": "competitive", "open_weight": "no", "entity_type": "Coding Agent (CLI)", "headquarters": "San Francisco, US", "valuation": "Anthropic", "models": "Claude Sonnet 4.6, Opus 4.8"},
    "entities/coding-agents/github-copilot.md": {"region": "us", "pricing": "competitive", "open_weight": "no", "entity_type": "Coding Agent (IDE)", "headquarters": "San Francisco, US", "valuation": "Microsoft", "models": "GPT-4o, Claude, Gemini"},
    "entities/coding-agents/opencode.md": {"region": "global", "pricing": "free", "open_weight": "yes", "entity_type": "Coding Agent (CLI)", "headquarters": "Open Source", "valuation": "—", "models": "Any via LiteLLM"},
    "entities/coding-agents/aider.md": {"region": "global", "pricing": "free", "open_weight": "yes", "entity_type": "Coding Agent (CLI)", "headquarters": "Open Source", "valuation": "—", "models": "Any OpenAI-compatible API"},
    "entities/coding-agents/openai-codex.md": {"region": "us", "pricing": "competitive", "open_weight": "no", "entity_type": "Coding Agent (CLI)", "headquarters": "San Francisco, US", "valuation": "OpenAI", "models": "GPT-5.3 Codex, o3"},
    "entities/coding-agents/devin-desktop.md": {"region": "us", "pricing": "premium", "open_weight": "no", "entity_type": "Coding Agent (Desktop)", "headquarters": "San Francisco, US", "valuation": "Cognition AI", "models": "Cognition proprietary + Claude"},
    "entities/coding-agents/gemini-cli.md": {"region": "us", "pricing": "free", "open_weight": "no", "entity_type": "Coding Agent (CLI)", "headquarters": "Mountain View, US", "valuation": "Google/Alphabet", "models": "Gemini 2.5 Pro"},
    "entities/coding-agents/grok-build.md": {"region": "us", "pricing": "competitive", "open_weight": "partial", "entity_type": "Coding Agent (CLI)", "headquarters": "San Francisco, US", "valuation": "xAI", "models": "Grok Code Fast 1"},
    "entities/coding-agents/amazon-nova-act.md": {"region": "us", "pricing": "competitive", "open_weight": "no", "entity_type": "Coding Agent (Cloud)", "headquarters": "Seattle, US", "valuation": "Amazon/AWS", "models": "Amazon Nova"},

    # Agent Frameworks
    "entities/agent-frameworks/langchain.md": {"region": "us", "pricing": "free", "open_weight": "yes", "entity_type": "Agent Framework", "headquarters": "Open Source", "valuation": "—", "models": "Any LLM"},
    "entities/agent-frameworks/crewai.md": {"region": "us", "pricing": "free", "open_weight": "yes", "entity_type": "Agent Framework", "headquarters": "Open Source", "valuation": "—", "models": "Any LLM"},
    "entities/agent-frameworks/autogen.md": {"region": "us", "pricing": "free", "open_weight": "yes", "entity_type": "Agent Framework", "headquarters": "Open Source (Microsoft)", "valuation": "—", "models": "Any LLM"},
    "entities/agent-frameworks/llamaindex.md": {"region": "us", "pricing": "free", "open_weight": "yes", "entity_type": "Agent Framework", "headquarters": "Open Source", "valuation": "—", "models": "Any LLM"},
    "entities/agent-frameworks/openai-agents-sdk.md": {"region": "us", "pricing": "free", "open_weight": "no", "entity_type": "Agent Framework", "headquarters": "San Francisco, US", "valuation": "OpenAI", "models": "OpenAI models only"},
    "entities/agent-frameworks/semantic-kernel.md": {"region": "us", "pricing": "free", "open_weight": "yes", "entity_type": "Agent Framework", "headquarters": "Redmond, US", "valuation": "Microsoft", "models": "Any LLM"},
    "entities/agent-frameworks/smolagents.md": {"region": "eu", "pricing": "free", "open_weight": "yes", "entity_type": "Agent Framework", "headquarters": "Open Source (Hugging Face)", "valuation": "—", "models": "Any LLM"},

    # AI Finance
    "entities/ai-finance/ai-alpha-generation.md": {"region": "global", "pricing": "enterprise", "open_weight": "partial", "entity_type": "AI Finance Concept", "headquarters": "—", "valuation": "—", "models": "Multiple LLMs"},
    "entities/ai-finance/bloomberg-gpt.md": {"region": "us", "pricing": "enterprise", "open_weight": "no", "entity_type": "AI Finance Product", "headquarters": "New York, US", "valuation": "Bloomberg LP", "models": "BloombergGPT 50B"},
    "entities/ai-finance/sentiment-analysis-finance.md": {"region": "global", "pricing": "enterprise", "open_weight": "partial", "entity_type": "AI Finance Concept", "headquarters": "—", "valuation": "—", "models": "FinBERT, LLMs"},
    "entities/ai-finance/financial-reasoning-benchmarks.md": {"region": "global", "pricing": "free", "open_weight": "yes", "entity_type": "Benchmark", "headquarters": "—", "valuation": "—", "models": "Multiple"},

    # Open Source Ecosystem
    "entities/open-source-ecosystem/hugging-face.md": {"region": "us", "pricing": "free", "open_weight": "yes", "entity_type": "Platform", "headquarters": "New York, US", "valuation": "$4.5B", "models": "500K+ models"},
    "entities/open-source-ecosystem/ollama.md": {"region": "global", "pricing": "free", "open_weight": "yes", "entity_type": "Tool", "headquarters": "Open Source", "valuation": "—", "models": "Any GGUF model"},
    "entities/open-source-ecosystem/model-commoditization.md": {"region": "global", "pricing": "free", "open_weight": "yes", "entity_type": "Concept", "headquarters": "—", "valuation": "—", "models": "—"},
}

# Region icon map
REGION_ICONS = {
    "us": "🇺🇸",
    "cn": "🇨🇳",
    "eu": "🇪🇺",
    "global": "🌐",
}

def make_entity_header(data):
    """Generate the entity header HTML block."""
    region_icon = REGION_ICONS.get(data["region"], "🏢")
    pricing_class = data["pricing"]
    ow_class = "yes" if data["open_weight"] == "yes" else ("partial" if data["open_weight"] == "partial" else "no")
    ow_label = "Open" if data["open_weight"] == "yes" else ("Partial" if data["open_weight"] == "partial" else "Closed")
    pricing_label = data["pricing"].capitalize()

    return f"""<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge {data["region"]}">{region_icon} {data["region"].upper()}</span>
    <span class="pricing-badge {pricing_class}">{pricing_label}</span>
    <span class="open-weight-{ow_class}">● {ow_label} weights</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>{data["entity_type"]}{"" if not data.get("headquarters") or data["headquarters"] == "—" else f'<span class="entity-meta-key">HQ</span>{data["headquarters"]}'}{"" if not data.get("valuation") or data["valuation"] == "—" else f'<span class="entity-meta-key">Valuation</span>{data["valuation"]}'}{"" if not data.get("models") or data["models"] == "—" else f'<span class="entity-meta-key">Key Models</span>{data["models"]}'}
  </div>
</div>
"""

def process_file(rel_path):
    full = BASE / rel_path
    if not full.exists():
        return f"SKIP: {rel_path} not found"

    content = full.read_text()
    data = ENTITIES.get(rel_path)
    if not data:
        return f"SKIP: {rel_path} not in metadata map"

    # Check if entity header already exists
    if 'class="entity-header"' in content:
        return f"SKIP: {rel_path} already has entity header"

    # Find the first `# Title` line and inject before it
    pattern = re.compile(r'^(# .+)$', re.MULTILINE)
    match = pattern.search(content)
    if not match:
        return f"SKIP: {rel_path} no H1 found"

    header_html = make_entity_header(data)
    new_content = content[:match.start()] + header_html + content[match.start():]
    full.write_text(new_content)
    return f"OK: {rel_path}"

# Run
results = []
for path in sorted(ENTITIES.keys()):
    results.append(process_file(path))

for r in results:
    print(r)

total = len(results)
ok = sum(1 for r in results if r.startswith("OK"))
skip = sum(1 for r in results if r.startswith("SKIP"))
print(f"\nTotal: {total} | Updated: {ok} | Skipped: {skip}")
