## ADDED Requirements

### Requirement: Deployment Directory

A separate directory (`/home/fax/shodan-eye-deploy`) serves as the Claude Code workspace where users interact with Shodan Eye through natural language.

#### Scenario: Directory structure

- **WHEN** the deployment directory is set up
- **THEN** it contains: `CLAUDE.md` (tool documentation), `.claude/settings.local.json` (permissions config), and a symlink or path reference to the development library

#### Scenario: CLAUDE.md teaches tool usage

- **WHEN** Claude Code starts a session in the deployment directory
- **THEN** CLAUDE.md provides: available commands, example queries, API key setup instructions, dork categories overview, and output format options
- **AND** Claude can immediately use the tools without additional context

### Requirement: Skill Definitions

Claude Code skills wrap the Python library into natural slash commands.

#### Scenario: /shodan-search skill

- **WHEN** a user runs `/shodan-search` with a query
- **THEN** Claude calls `shodan_eye.search.search()` via Python and presents formatted results
- **AND** the user can specify limit, output format, and save location in natural language

#### Scenario: /shodan-dorks skill

- **WHEN** a user runs `/shodan-dorks`
- **THEN** Claude loads the dork database and presents categories
- **AND** the user can browse, search, or describe what they're looking for
- **AND** Claude suggests relevant dorks and can execute them directly

#### Scenario: /shodan-host skill

- **WHEN** a user runs `/shodan-host` with an IP address
- **THEN** Claude calls `shodan_eye.search.host_info()` and presents a formatted report

#### Scenario: /shodan-info skill

- **WHEN** a user runs `/shodan-info`
- **THEN** Claude calls `shodan_eye.api.get_account_info()` and displays plan type, remaining credits, and account status

### Requirement: Permission Configuration

#### Scenario: Local settings allow Python execution

- **WHEN** Claude Code operates in the deployment directory
- **THEN** `.claude/settings.local.json` pre-authorizes running `python3` commands against the shodan_eye library
- **AND** no additional user approval is needed for standard search/lookup operations

### Requirement: Development Directory CLAUDE.md

#### Scenario: Dev CLAUDE.md reflects new architecture

- **WHEN** a developer opens the development directory in Claude Code
- **THEN** CLAUDE.md documents the package structure, module responsibilities, how to run tests, and how skills are defined
