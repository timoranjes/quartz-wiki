# AGENTS.md — projects/web/quartz-wiki/

## Scope
Quartz-based knowledge wiki deployed to GitHub Pages. Syncs content from Obsidian vaults.

## Current State
- **Version:** v1.0.0 ⭐
- **Status:** Active — cron sync every 15 min
- **Last sync:** 2026-06-09 08:34 HKT (25 files changed)
- **Deploy URL:** https://timoranjes.github.io/quartz-wiki/
- **GitHub repo:** https://github.com/timoranjes/quartz-wiki

## Tech Stack
- **Framework:** Quartz v4 (@jackyzha0/quartz)
- **Build:** GitHub Actions → `npx quartz build` → `public/`
- **Sync:** `~/.hermes/scripts/sync-unified-wiki.sh` (rsync + git)

## Key Files
| File | Purpose |
|------|---------|
| `content/ai-intelligence/` | AI Agents + LLM Providers vault (merged) |
| `content/supply-chain/` | AI Supply Chain vault |
| `content/index.md` | Wiki homepage |
| `quartz.config.yaml` | Quartz configuration |
| `~/.hermes/scripts/sync-unified-wiki.sh` | Sync script |

## Cron Jobs
| Job ID | Name | Schedule |
|--------|------|----------|
| `05689676e5b9` | Unified Wiki Sync | */15 min |
| `8e838fb769b3` | AI Wiki — Process Sources (Stage 2) | 07:15 daily |
| `f91fb94edce0` | AI Wiki — Source Watcher (Stage 1) | 06:45 daily |

## Source Vaults
| Vault | Local Path |
|-------|------------|
| AI Intelligence | `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki-ai-intelligence` |
| Supply Chain | `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki-ai-supply-chain` |

## Boundaries
✅ Allowed: Sync vault content, update wiki pages, rebuild Quartz
❌ Never edit: `.github/workflows/`, `package.json`, `quartz.config.yaml` without approval
❌ Never commit: API keys, credentials, personal data
