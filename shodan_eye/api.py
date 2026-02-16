"""Shodan API client wrapper — key resolution, client creation, account info."""

import os
import shodan


def resolve_api_key(filepath="api.txt"):
    """Resolve API key: env var > file > None."""
    key = os.environ.get("SHODAN_API_KEY")
    if key:
        return key

    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, "r") as f:
            return f.readline().rstrip("\n")

    return None


def save_api_key(key, filepath="api.txt"):
    """Write API key to file."""
    with open(filepath, "w") as f:
        f.write(key)


def create_client(api_key):
    """Create and return a shodan.Shodan client instance."""
    return shodan.Shodan(api_key)


def get_account_info(client):
    """Validate key and return account info using the free api.info() endpoint.

    Returns dict with plan, query_credits, scan_credits, etc.
    Raises shodan.APIError if key is invalid.
    """
    info = client.info()
    return {
        "plan": info.get("plan", "unknown"),
        "query_credits": info.get("query_credits", 0),
        "scan_credits": info.get("scan_credits", 0),
        "telnet": info.get("telnet", False),
        "https": info.get("https", False),
        "unlocked": info.get("unlocked", False),
        "unlocked_left": info.get("unlocked_left", 0),
    }
