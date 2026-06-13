# Airbnb Cradle Mountain Scraper

A Playwright-based Python scraper that collects Airbnb listings near Cradle Mountain, Tasmania.

## Search Parameters
- **Location:** Cradle Mountain, Tasmania, Australia
- **Check-in:** July 20, 2026
- **Check-out:** July 22, 2026
- **Guests:** 1
- **Nights:** 2

## Setup

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Usage

```bash
python main.py
```

Results are saved to `results.json`.

## Files

| File | Purpose |
|------|---------|
| `config.py` | Search parameters, timeouts, feature keywords |
| `models.py` | Dataclass definitions for Listing and ScrapingResult |
| `scraper.py` | Core Playwright scraper with error handling |
| `main.py` | Entry point |
| `requirements.txt` | Python dependencies |
