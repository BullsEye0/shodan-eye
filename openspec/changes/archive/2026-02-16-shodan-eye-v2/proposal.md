## Why

Shodan Eye is a 220-line interactive script that does one search per run, wastes API credits on key validation, outputs raw Python dicts/lists, and ignores its bundled dorks file. Meanwhile, the official `shodan` Python library already provides a rich CLI (`search`, `host`, `stats`, `download`, `convert`, `alert`, `scan`, `stream`) — so rebuilding those features is wasted effort.

The real opportunity: **make Claude Code the user interface**. The Python backend becomes a non-interactive library of reconnaissance commands that Claude Code orchestrates via skills and slash commands. This gives us natural language queries, intelligent dork selection, formatted output, and iterative workflows — all without building a traditional CLI.

Two directories:
1. **Development** (`/home/fax/shodan-eye`) — the Python library + Claude Code skills source
2. **Deployment** (`/home/fax/shodan-eye-deploy`) — production Claude Code instance with local settings, CLAUDE.md, and skills configured to use the library

## What Changes

- **Modular Python library**: Break monolith into `shodan_eye/` package — `api.py` (wraps shodan with `api.info()`, structured output), `formatter.py` (human-readable + JSON), `dorks.py` (parses and categorizes the dorks file), `search.py` (core search with progress/limits)
- **No interactive prompts**: All functions accept arguments and return structured data (dicts/JSON). Claude Code handles the UX.
- **Dorks intelligence**: Parse `Shodan_Dorks_The_Internet_of_Sh*t.txt` into categorized, searchable entries. Claude Code can suggest relevant dorks based on user intent.
- **Formatted output**: Location as `City, Country`, Domains/Hostnames as comma-joined strings, consistent field naming, timestamps on exports
- **JSON + TXT export**: Structured JSON output by default, with TXT fallback
- **Claude Code skills**: Slash commands like `/shodan-search`, `/shodan-dorks`, `/shodan-host`, `/shodan-info` that wrap the library
- **Deployment setup**: Separate directory with CLAUDE.md teaching Claude how to use the Shodan Eye toolkit, plus local settings

## Capabilities

### New Capabilities
- `modular-library`: Non-interactive Python package replacing the monolith script
- `search-engine`: Core search with configurable limits, progress callbacks, `api.info()` validation, structured results
- `output-formatting`: Human-readable field formatting, JSON export, log timestamps/separators
- `dorks-intelligence`: Parsed/categorized dork database from the bundled text file
- `claude-code-integration`: Skills, CLAUDE.md, and deployment directory for Claude Code as the UI

### Modified Capabilities
<!-- No existing specs to modify -->

## Impact

- `shodan-eye.py` — kept as legacy entry point, imports from new package
- `shodan_eye/` — new package: `__init__.py`, `api.py`, `search.py`, `formatter.py`, `dorks.py`
- `skills/` — Claude Code skill definitions
- `requirements.txt` — sole dependency remains `shodan`
- `Shodan_Dorks_The_Internet_of_Sh*t.txt` — now parsed by `dorks.py`
- `/home/fax/shodan-eye-deploy/` — new deployment directory with `.claude/settings.json`, `CLAUDE.md`
