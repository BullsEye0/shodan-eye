## 1. Package scaffolding

- [x] 1.1 Create `shodan_eye/` directory with `__init__.py`
- [x] 1.2 Create empty module files: `api.py`, `search.py`, `formatter.py`, `dorks.py`
- [x] 1.3 Set up venv with `shodan` dependency for development
- [x] 1.4 Replace `shodan-eye.py` with thin legacy wrapper

## 2. API module (`shodan_eye/api.py`)

- [x] 2.1 Implement `resolve_api_key()` — env var > file > None
- [x] 2.2 Implement `create_client(api_key)` — returns `shodan.Shodan` instance
- [x] 2.3 Implement `get_account_info(client)` — wraps `api.info()`, returns structured dict
- [x] 2.4 Implement `save_api_key(key, filepath="api.txt")` — writes key to file

## 3. Formatter module (`shodan_eye/formatter.py`)

- [x] 3.1 Define color constants: `RED`, `BLUE`, `BOLD`, `RESET`
- [x] 3.2 Implement `format_location(loc_dict)` — returns `"City, Country"` string
- [x] 3.3 Implement `format_list_field(items)` — returns comma-joined string or `"None"`
- [x] 3.4 Implement `format_result(banner)` — returns structured dict with all fields formatted
- [x] 3.5 Implement `export_json(results, filepath)` — write JSON array to file
- [x] 3.6 Implement `export_jsonl(result, file_handle)` — write single JSON line
- [x] 3.7 Implement `export_txt(results, filepath, query, timestamp)` — write TXT with headers/separators
- [x] 3.8 Implement `result_to_console(result)` — returns ANSI-colored string for terminal display

## 4. Search module (`shodan_eye/search.py`)

- [x] 4.1 Implement `search(client, query, limit=100, on_progress=None)` — core search with cursor iteration
- [x] 4.2 Implement `host_info(client, ip)` — wraps `client.host()`, returns formatted dict
- [x] 4.3 Implement `search_stats(client, query, facets)` — wraps `client.count()`, returns facet summary

## 5. Dorks module (`shodan_eye/dorks.py`)

- [x] 5.1 Implement `load_dorks(filepath)` — parse the dorks text file into structured list
- [x] 5.2 Implement `list_categories(dorks)` — return sorted unique categories with counts
- [x] 5.3 Implement `search_dorks(dorks, keyword)` — case-insensitive search across all fields
- [x] 5.4 Implement `get_dorks_by_category(dorks, category)` — filter by category name

## 6. Legacy wrapper

- [x] 6.1 Create `shodan_eye/legacy.py` — re-creates interactive behavior using new library
- [x] 6.2 Update `shodan-eye.py` to import and call `legacy.run()`

## 7. Package exports (`shodan_eye/__init__.py`)

- [x] 7.1 Export public API: `search`, `host_info`, `search_stats`, `create_client`, `resolve_api_key`, `get_account_info`, `load_dorks`, `search_dorks`, `format_result`, `export_json`

## 8. Claude Code deployment (`shodan-cc`)

- [x] 8.1 Write deployment `CLAUDE.md` — tool docs, examples, dork categories, API key setup
- [x] 8.2 Write `.claude/settings.local.json` — pre-authorize Python execution
- [x] 8.3 Create skill files: `shodan-search.md`, `shodan-dorks.md`, `shodan-host.md`, `shodan-info.md`
- [x] 8.4 Create `.gitignore` for deploy repo (api.txt, *.pyc, __pycache__)
- [x] 8.5 Initial commit and push to `brainbloodbarrier/shodan-cc`

## 9. Development CLAUDE.md update

- [x] 9.1 Rewrite dev `CLAUDE.md` to document new package structure, module responsibilities, how to add skills

## 10. Verify

- [x] 10.1 Run `python3 -c "from shodan_eye import search, create_client, load_dorks"` — imports work
- [x] 10.2 Run `python3 shodan-eye.py` — legacy wrapper still works
- [x] 10.3 Verify dorks parser loads all entries from the bundled file
- [x] 10.4 Verify JSON export produces valid JSON
