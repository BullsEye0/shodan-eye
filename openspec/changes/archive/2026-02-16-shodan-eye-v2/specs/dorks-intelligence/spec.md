## ADDED Requirements

### Requirement: Dorks Parser

`shodan_eye/dorks.py` parses `Shodan_Dorks_The_Internet_of_Sh*t.txt` into structured, searchable entries.

#### Scenario: Parse dorks file

- **WHEN** `load_dorks(filepath)` is called with the bundled dorks file
- **THEN** it returns a list of dork entries, each with `category`, `description`, and `query` fields
- **AND** categories are derived from the `→` arrow headers in the file (e.g., `"Chromecasts / Smart TVs"`)
- **AND** the description is any non-query text between the header and the query line

#### Scenario: File not found

- **WHEN** `load_dorks(filepath)` is called with a non-existent path
- **THEN** it returns an empty list (not an exception)

### Requirement: Category Listing

#### Scenario: List all categories

- **WHEN** `list_categories(dorks)` is called
- **THEN** it returns a sorted list of unique category names
- **AND** each category includes a count of dorks it contains

### Requirement: Dork Search

#### Scenario: Search by keyword

- **WHEN** `search_dorks(dorks, keyword="camera")` is called
- **THEN** it returns all dorks where the keyword appears in category, description, or query (case-insensitive)

#### Scenario: Filter by category

- **WHEN** `get_dorks_by_category(dorks, category="Remote Desktop")` is called
- **THEN** it returns only dorks in that category

### Requirement: Dork Suggestion

#### Scenario: Suggest dorks from natural language

- **WHEN** Claude Code asks for dorks related to a user's intent (e.g., "find exposed webcams")
- **THEN** the `search_dorks()` function provides relevant matches that Claude can present and refine
- **AND** the query field from each match can be passed directly to `search()`
