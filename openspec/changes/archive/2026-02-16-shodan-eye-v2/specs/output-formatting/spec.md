## ADDED Requirements

### Requirement: Human-Readable Console Formatting

`shodan_eye/formatter.py` transforms raw result dicts into display-ready strings.

#### Scenario: Location formatting

- **WHEN** a result has `location: {"city": "Amsterdam", "country_name": "Netherlands", "latitude": 52.37, "longitude": 4.89}`
- **THEN** the formatted location is `"Amsterdam, Netherlands"`
- **AND** if city is null, it falls back to `"Netherlands"`
- **AND** if both are null, it shows `"Unknown"`

#### Scenario: List field formatting

- **WHEN** a result has `domains: ["example.com", "test.com"]`
- **THEN** the formatted domains string is `"example.com, test.com"`
- **AND** empty lists display as `"None"`

#### Scenario: Consistent field naming

- **WHEN** results are formatted for any output target
- **THEN** the field name is `"Organization"` (American English, consistent everywhere)
- **AND** no field uses the British `"Organisation"` spelling

### Requirement: JSON Export

#### Scenario: JSON file output

- **WHEN** `export_json(results, filepath)` is called
- **THEN** it writes a JSON array of result dicts to the file
- **AND** each result includes all fields plus a `timestamp` and `query` metadata field
- **AND** the file is valid JSON parseable by any standard tool

#### Scenario: JSON-lines streaming

- **WHEN** `export_jsonl(result, file_handle)` is called with a single result
- **THEN** it writes one JSON object per line (JSON Lines format)
- **AND** this supports streaming writes during search iteration

### Requirement: TXT Export

#### Scenario: TXT file output with headers

- **WHEN** results are exported to TXT format
- **THEN** each search session starts with a header: separator line, query, timestamp, separator line
- **AND** each result is separated by a visual divider
- **AND** no ANSI color codes appear in the file

### Requirement: Color Constants

#### Scenario: ANSI colors defined as constants

- **WHEN** any module needs terminal coloring
- **THEN** it imports from `formatter.py`: `RED`, `BLUE`, `RESET`, `BOLD`
- **AND** no raw `\033[...m` escape codes appear anywhere else in the codebase
