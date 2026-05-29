# Wiki Schema

## Domain
AI Supply Chain — the full value chain from upstream materials and equipment through compute, packaging, memory, networking, and infrastructure. Covers competitive dynamics, technology trends, market structure, and bottleneck analysis. Industry-focused, not portfolio-centric.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `hbm-memory.md`, `cowos-packaging.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- Wikilinks use simple filenames only — NO path prefixes (`[[hbm-memory]]`, NOT `[[concepts/hbm-memory]]`)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Source attribution:** Use `sources:` in YAML frontmatter only. **Do NOT use inline `^[raw/...]` provenance footnotes** — they expose raw directory paths and create visual noise for external browsing.
- **No portfolio references:** Do not include portfolio weights, allocation percentages, ticker-based tracking, "Portfolio Implications," or "Investment Verdict." Use "Key Players," "Market Dynamics," and "Industry Relevance" instead.
- Entity pages reference major industry players by name (e.g., TSMC, NVIDIA, ASML), not tickers.

### Required Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low        # how well-supported the claims are
contested: true                        # set when the page has unresolved contradictions
---
```

`confidence` and `contested` are optional but recommended for opinion-heavy or fast-moving topics.

### raw/ Frontmatter
Raw sources get frontmatter for re-ingest drift detection:
```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of the raw content below the closing --- >
---
```

## Tag Taxonomy
Every tag on a page must appear in this taxonomy. Add new tags here BEFORE using them.

### Layers (supply chain segments)
- materials, equipment, foundry, packaging, memory, compute, optical, pcb, ccl, components

### Technologies
- hbm, chiplet, cowos, cpo, silicon-carbide, advanced-node, co-packaged-optics

### Market Dynamics
- bottleneck, pricing-power, capex-cycle, localization, export-controls, supply-demand

### Meta
- comparison, overview, market-structure, competitive-analysis

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity (company, organization, key person). Include:
- Overview / what they do in the AI supply chain
- Key products, technologies, market position
- Relationships to other entities (`[[wikilinks]]`)
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge / market dynamics
- Key players and competitive landscape
- Open questions or debates
- Related concepts (`[[wikilinks]]`)

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Industry verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
