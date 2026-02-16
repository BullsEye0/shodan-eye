"""Output formatting — color constants, field formatting, JSON/TXT export."""

import json
from datetime import datetime, timezone

# ANSI color constants
RED = "\033[1;31m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"


def format_location(loc):
    """Format location dict as 'City, Country'. Falls back gracefully."""
    if not loc or not isinstance(loc, dict):
        return "Unknown"
    city = loc.get("city")
    country = loc.get("country_name")
    if city and country:
        return f"{city}, {country}"
    return country or city or "Unknown"


def format_list_field(items):
    """Format a list field as comma-joined string. Empty/None becomes 'None'."""
    if not items:
        return "None"
    if isinstance(items, list):
        return ", ".join(str(i) for i in items) if items else "None"
    return str(items)


def format_result(banner):
    """Transform a raw Shodan banner into a structured result dict."""
    return {
        "ip": banner.get("ip_str", ""),
        "port": banner.get("port", 0),
        "org": banner.get("org", "Unknown"),
        "location": format_location(banner.get("location")),
        "transport": banner.get("transport", ""),
        "domains": format_list_field(banner.get("domains")),
        "hostnames": format_list_field(banner.get("hostnames")),
        "data": banner.get("data", ""),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def result_to_console(result):
    """Return ANSI-colored string for terminal display."""
    lines = [
        f"[+] {RED}IP: {RESET}{result['ip']}",
        f"[+] {RED}Port: {RESET}{result['port']}",
        f"[+] {RED}Organization: {RESET}{result['org']}",
        f"[+] {RED}Location: {RESET}{result['location']}",
        f"[+] {RED}Layer: {RESET}{result['transport']}",
        f"[+] {RED}Domains: {RESET}{result['domains']}",
        f"[+] {RED}Hostnames: {RESET}{result['hostnames']}",
        f"[+] {RED}Banner: {RESET}\n{result['data']}",
    ]
    return "\n".join(lines)


def result_to_txt(result):
    """Return plain text string for file export (no ANSI codes)."""
    return (
        f"IP: {result['ip']}\n"
        f"Port: {result['port']}\n"
        f"Organization: {result['org']}\n"
        f"Location: {result['location']}\n"
        f"Layer: {result['transport']}\n"
        f"Domains: {result['domains']}\n"
        f"Hostnames: {result['hostnames']}\n"
        f"Data:\n{result['data']}"
    )


def export_json(results, filepath, query=None):
    """Write results as a JSON array to file."""
    output = {
        "query": query,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total": len(results),
        "results": results,
    }
    with open(filepath, "w") as f:
        json.dump(output, f, indent=2, default=str)


def export_jsonl(result, file_handle):
    """Write a single result as a JSON line to an open file handle."""
    file_handle.write(json.dumps(result, default=str) + "\n")


def export_txt(results, filepath, query=None):
    """Write results to TXT file with headers and separators."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(filepath, "a") as f:
        f.write(f"\n{'=' * 78}\n")
        f.write(f"Search: {query or 'N/A'}\n")
        f.write(f"Time: {ts}\n")
        f.write(f"Results: {len(results)}\n")
        f.write(f"{'=' * 78}\n\n")
        for i, result in enumerate(results, 1):
            formatted = format_result(result) if "ip_str" in result else result
            f.write(f"--- Result #{i} ---\n")
            f.write(result_to_txt(formatted))
            f.write(f"\n{'─' * 78}\n\n")
