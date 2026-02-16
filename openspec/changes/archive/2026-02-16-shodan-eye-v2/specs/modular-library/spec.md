## ADDED Requirements

### Requirement: Package Structure

The application must be organized as a Python package `shodan_eye/` with focused modules instead of a single monolithic script. Each module has a single responsibility. No module contains interactive prompts (`input()`, `getpass`). All functions accept arguments and return structured data.

#### Scenario: Package layout

- **WHEN** a developer inspects the `shodan_eye/` directory
- **THEN** they find these modules: `__init__.py`, `api.py`, `search.py`, `formatter.py`, `dorks.py`
- **AND** each module can be imported independently without side effects

#### Scenario: No interactive I/O in library

- **WHEN** any function in `shodan_eye/` is called
- **THEN** it never calls `input()`, `getpass.getpass()`, or `print()` to stdout
- **AND** it returns data as Python dicts, lists, or strings that the caller decides how to present

#### Scenario: Legacy entry point preserved

- **WHEN** a user runs `python3 shodan-eye.py`
- **THEN** it imports from `shodan_eye/` and provides backward-compatible interactive behavior
- **AND** existing users are not broken by the restructure

### Requirement: API Module

`shodan_eye/api.py` wraps the `shodan` library with opinionated defaults and structured returns.

#### Scenario: API client initialization

- **WHEN** `create_client(api_key)` is called with a valid key
- **THEN** it returns a `shodan.Shodan` instance
- **AND** validates the key using `api.info()` (free endpoint, no credit cost)

#### Scenario: API key resolution

- **WHEN** `resolve_api_key()` is called with no arguments
- **THEN** it checks `SHODAN_API_KEY` env var first, then `./api.txt` file
- **AND** returns the key string or `None` if neither source has one

#### Scenario: Account info

- **WHEN** `get_account_info(client)` is called
- **THEN** it returns a dict with `plan`, `query_credits`, `scan_credits`, `telnet`, `https`, `unlocked`, `unlocked_left`
