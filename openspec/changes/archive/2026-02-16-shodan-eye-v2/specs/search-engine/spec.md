## ADDED Requirements

### Requirement: Core Search

`shodan_eye/search.py` provides the primary search functionality with configurable limits and structured results.

#### Scenario: Basic search

- **WHEN** `search(client, query, limit=100)` is called
- **THEN** it uses `client.search_cursor(query)` to iterate results
- **AND** stops after `limit` results are collected
- **AND** returns a list of formatted result dicts

#### Scenario: Configurable result limit

- **WHEN** `search()` is called with `limit=50`
- **THEN** it returns at most 50 results
- **AND** the default limit is 100 (not the old arbitrary 888)

#### Scenario: Progress callback

- **WHEN** `search()` is called with `on_progress=callback_fn`
- **THEN** it calls `callback_fn(current_count, result)` after each result is fetched
- **AND** the caller can use this to display progress, write to files, or stream results

#### Scenario: Result structure

- **WHEN** a single result is returned from `search()`
- **THEN** it is a dict with keys: `ip`, `port`, `org`, `location`, `transport`, `domains`, `hostnames`, `data`, `timestamp`
- **AND** `location` is a formatted string like `"Amsterdam, Netherlands"` (not a raw dict)
- **AND** `domains` and `hostnames` are comma-joined strings (not Python lists)
- **AND** `timestamp` is ISO 8601 format

### Requirement: Host Lookup

#### Scenario: Single host details

- **WHEN** `host_info(client, ip)` is called
- **THEN** it returns a dict with IP, open ports, vulns, hostnames, location, org, OS, and banner data
- **AND** wraps `client.host(ip)` with formatted output

### Requirement: Search Statistics

#### Scenario: Faceted stats

- **WHEN** `search_stats(client, query, facets=["country", "org", "port"])` is called
- **THEN** it returns a dict mapping each facet to its top values and counts
- **AND** uses `client.count(query, facets=facets)` under the hood
