# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Shodan Eye is a modular Python library for Shodan reconnaissance, designed to be orchestrated by Claude Code. The Python backend is non-interactive (no `input()`/`print()`) — it returns structured data that Claude Code presents to the user.

**Two repos:**
- **This repo** (`shodan-eye`) — Python library + OpenSpec artifacts
- **`shodan-cc`** — Claude Code deployment workspace with CLAUDE.md, settings, and skills

## Running

```bash
pip3 install -r requirements.txt   # sole dependency: shodan

# Library usage:
python3 -c "from shodan_eye import search, create_client, load_dorks"

# Legacy interactive mode (backward compatible):
python3 shodan-eye.py
```

## Package Structure

```
shodan_eye/
├── __init__.py      # Public API exports
├── api.py           # Client creation, key resolution (env var > file), account info
├── search.py        # search(), host_info(), search_stats()
├── formatter.py     # format_result(), export_json/txt/jsonl, color constants
├── dorks.py         # load_dorks(), list_categories(), search_dorks()
└── legacy.py        # Interactive wrapper preserving original UX
```

## API Key Handling

Resolution order (in `api.resolve_api_key()`):
1. `SHODAN_API_KEY` environment variable (preferred)
2. `./api.txt` file (if it exists and is non-empty)
3. Returns `None` — caller decides how to handle

The `api.txt` file is gitignored. Key validation uses `api.info()` (free endpoint) instead of a test search.

## Key Design Decisions

- **No interactive I/O in library**: All functions in `shodan_eye/` accept arguments and return dicts/lists. Only `legacy.py` uses `input()`/`print()`.
- **Progress via callbacks**: `search()` accepts `on_progress=callback(count, result)` — the caller decides how to display progress.
- **Formatted output by default**: `format_result()` converts raw Shodan banners to clean dicts (Location as "City, Country", lists as comma-joined strings).
- **Color constants**: `RED`, `BLUE`, `BOLD`, `RESET` defined in `formatter.py` — no raw escape codes elsewhere.

## Style Conventions

- f-strings for all string formatting
- `with` statements for all file I/O (except log file in legacy.py which uses try/finally)
- `getpass.getpass()` for hidden input (legacy mode only)
- Functions return data, don't print it (except legacy.py)

## Files

- `shodan-eye.py` — thin legacy entry point
- `shodan_eye/` — the library package (see structure above)
- `requirements.txt` — single dependency (`shodan`)
- `Shodan_Dorks_The_Internet_of_Sh*t.txt` — dorks database (parsed by `dorks.py`)
- `.gitignore` — excludes `api.txt`, `*.pyc`, `__pycache__/`
- `openspec/` — OpenSpec change artifacts (proposal, specs, design, tasks)
