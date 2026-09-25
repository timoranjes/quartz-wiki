# AGENTS.md — projects/web/quartz-wiki/

## Scope
Quartz-based knowledge wiki deployed to GitHub Pages. Content is authored in
Obsidian vaults, deduplicated here, and published as a static site.

## Current State
- **Framework:** Quartz v5 (`@jackyzha0/quartz` 5.0.0)
- **Status:** Active — published site, built by GitHub Actions on push to `main`
- **Deploy URL:** https://timoranjes.github.io/quartz-wiki/
- **GitHub repo:** https://github.com/timoranjes/quartz-wiki
- **Visibility:** Public (required — GitHub Pages on this account)

> Cron-driven sync is **not** running on the VPS. The `Unified Wiki Sync`
> job (`*/15`) previously documented here is not registered in
> `~/.hermes/cron/jobs.json`, and the VPS has no iCloud vault paths. The
> staging crons below only write to `/home/orange/.hermes/wiki-jobs`.
> See "Sync" under Boundaries before assuming content lands automatically.

## Tech Stack
- **Build:** GitHub Actions → `npx quartz plugin install` + `npx quartz build` → `public/`
- **Plugins:** external plugins are pulled from `quartz.lock.json` at build time
- **Node:** >= 22 (engines field in `package.json`)

## Key Files
| File | Purpose |
|------|---------|
| `content/ai-intelligence/` | AI models, coding agents, agent frameworks + Classic Reference Set |
| `content/supply-chain/` | AI supply chain / semiconductor landscape |
| `content/index.md` | Wiki homepage |
| `quartz.config.yaml` | Quartz configuration |
| `quartz.lock.json` | Pinned external plugin commits |

## Content Layout Rules
- Only `content/**/*.md` is published. The site reads `content/` as its root.
- **Never commit** `.quartz/`, `content/*/state/`, `content/*/raw/`, or
  `content/*/wiki/` — these are build output and pipeline staging. They are
  gitignored; if a sync tool re-adds them, fix the tool, don't `git add -f`.
- Page slugs are path-derived. Two files with the same basename in different
  folders are fine; the same **full path** collides. Suffix retired-but-kept
  material with `-classic` rather than overwriting current pages.
- When renaming or moving a page, rewrite inbound `[[wikilinks]]` in the same
  change — Quartz does not redirect old slugs.

## Staging Crons (VPS, authoring side)
| Job ID | Name | Schedule |
|--------|------|----------|
| `8e838fb769b3` | AI Wiki — Process Sources (Stage 2) | 20 5 * * * |
| `f91fb94edce0` | AI Wiki — Source Watcher (Stage 1) | 50 4 * * * |
| `73b59d7c308e` | AI Wiki — YouTube Transcript Collector | 10 4 * * * |

These produce vault content. They do **not** push to this repo.

## Boundaries
✅ Allowed: Edit `content/`, rebuild locally, open PRs
❌ Never edit without approval: `.github/workflows/`, `package.json`, `quartz.config.yaml`
❌ Never commit: API keys, credentials, personal data, build artifacts, pipeline state

## Local Verification (run before opening a PR)
```bash
npm ci
npx quartz plugin install     # re-run after `rm -rf .quartz` if it reports failures
npx quartz build              # expect "Emitted N files" with no ERROR lines
```
If `quartz plugin install` reports mass failures, delete the cache and retry —
it leaves a detached dirty checkout otherwise:
```bash
rm -rf .quartz && npx quartz plugin install
```
