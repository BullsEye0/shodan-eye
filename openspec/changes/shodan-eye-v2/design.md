## Context

Shodan Eye is a 220-line single-file interactive Python script. The official `shodan` library already provides a full CLI with `search`, `host`, `stats`, `download`, `convert`, `alert`, `scan`, `stream` — so we don't reimplement those. Instead, we restructure Shodan Eye as a non-interactive Python library that Claude Code orchestrates via skills.

Two repos:
- **`shodan-eye`** (dev) — Python library + skills source
- **`shodan-cc`** (deploy) — Claude Code workspace with CLAUDE.md + settings

## Goals / Non-Goals

**Goals:**
- Break monolith into importable, testable modules
- All functions return structured data (dicts/JSON), no `input()`/`print()`
- Claude Code becomes the sole UI layer
- Leverage `shodan` library methods directly (don't wrap what already works)
- Parse bundled dorks file into searchable database

**Non-Goals:**
- Building a standalone CLI (the official `shodan` CLI already exists)
- Adding dependencies beyond `shodan` (stdlib only)
- Real-time streaming (Shodan firehose is a different product)
- Web UI or API server
- Replacing the official `shodan` CLI

## Decisions

### Decision 1: Package structure — flat modules in `shodan_eye/`

```
shodan_eye/
├── __init__.py      # Package exports
├── api.py           # Client creation, key resolution, account info
├── search.py        # search(), host_info(), search_stats()
├── formatter.py     # format_result(), export_json(), export_txt(), color constants
└── dorks.py         # load_dorks(), list_categories(), search_dorks()
```

**Rationale:** Flat is better than nested for a small library. Five modules with clear boundaries. No sub-packages needed.

### Decision 2: `api.info()` replaces `api.search("b00m")` for validation

The current code wastes API query credits to validate the key. `api.info()` is free, returns account details, and serves double duty: validates the key AND shows remaining credits.

### Decision 3: Progress via callbacks, not print statements

```python
def search(client, query, limit=100, on_progress=None):
    for i, banner in enumerate(client.search_cursor(query)):
        result = format_result(banner)
        if on_progress:
            on_progress(i + 1, result)
        ...
```

Claude Code can pass its own callback to display progress however it wants. The library stays silent.

### Decision 4: Dorks parsed as structured data

The dorks file uses a pattern: `Category →` header, optional description lines, then query line. We parse this into:

```python
{"category": "Chromecasts / Smart TVs", "description": "...", "query": "\"Chromecast:\" port:8008"}
```

Claude Code can then search/filter/suggest dorks using natural language.

### Decision 5: Skills live in dev repo, deployed via symlink/copy

Skills are defined in `shodan-eye/skills/` as markdown files following Claude Code's skill format. The deployment repo references or copies them. This keeps skills version-controlled alongside the library they call.

### Decision 6: Legacy `shodan-eye.py` becomes a thin wrapper

```python
#!/usr/bin/env python3
from shodan_eye.legacy import run
if __name__ == "__main__":
    run()
```

The `legacy.py` module recreates the original interactive behavior using the new library functions. Existing users aren't broken.

### Decision 7: Deploy CLAUDE.md is the product interface

The deployment CLAUDE.md teaches Claude:
- What tools are available and how to call them
- Where the Python library lives
- How to format and present results
- How to use dorks for reconnaissance workflows
- API key setup instructions for the user

This is the "product documentation" — it defines the user experience.
