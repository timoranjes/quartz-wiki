---
title: Amazon Nova Act
researched: 2026-06-05
sources:
  - https://nova.amazon.com/act
  - https://labs.amazon.science/blog/nova-act
  - https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-nova-act-extension-build-test-ai-agents-ide/
---

# Amazon Nova Act

## Company Facts
- Provider: Amazon (AWS / Amazon AGI Labs)
- Announced: March 31, 2025 (research preview)
- AWS Service: September 2025
- SDK: `pip install nova-act`
- GitHub: github.com/aws/nova-act

## Model Lineup
| Model | ID | Context | Pricing | Type |
|-------|-----|---------|---------|------|
| **Nova Act** | `nova-act` | N/A | AWS usage-based | Web action agent |

## Capabilities
- Reasoning: yes (contextual instructions)
- Vision: yes (browser screen understanding)
- Audio: no
- Tool Use: yes (Playwright browser automation)
- Agentic: yes (autonomous multi-step web workflows)
- Coding: yes (interleaved Python code execution)

## Key Facts
- First model focused on reliable, low-level web browser actions — not just natural language responses
- Over 90% accuracy on tricky UI elements (date pickers, dropdowns, popups) in internal benchmarks
- Hybrid execution: Playwright browser manipulation + API calls + interleaved Python
- Used in Alexa+ for autonomous web navigation when APIs unavailable
- IDE extensions available for VS Code and Kiro
- No-code Playground at nova.amazon.com/act — no API key required for prototyping
- Customer cases: Hertz (weeks → hours for QA), 1Password, Sola (hundreds of thousands of executions/month)
- Trained via reinforcement learning on diverse real-world web environments, not just supervised fine-tuning

## Sources
- https://nova.amazon.com/act
- https://labs.amazon.science/blog/nova-act
- https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-nova-act-extension-build-test-ai-agents-ide/
