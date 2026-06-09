# CHANGELOG.md — Quartz Wiki

All notable changes to this project.

## [1.0.0] - 2026-06-07

### Added
- Initial Quartz wiki deployment to GitHub Pages
- AI Agents vault sync (`wiki-ai-agents` → `content/ai-agents/`)
- Supply Chain vault sync (`wiki-ai-supply-chain` → `content/supply-chain/`)
- LLM Providers vault sync (`wiki-llm-providers` → `content/llm-providers/`)
- GitHub Actions workflow for auto-build on push to `main`

### Changed
- 2026-06-09: Consolidated vault paths — merged `ai-agents` + `llm-providers` into `wiki-ai-intelligence` → `content/ai-intelligence/`
- 2026-06-09: Relocated repo from `~/quartz-wiki` → `~/projects/web/quartz-wiki`
- 2026-06-09: Restored broken `sync-unified-wiki.sh` cron job (was failing due to missing local directory)

### Fixed
- Broken cron job `5b2f441352eb` (Unified Wiki Sync) — local directory deleted, repo re-cloned
- Updated script to reference correct merged vault path (`wiki-ai-intelligence`)
