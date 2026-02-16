"""Shodan Eye — modular Python library for Shodan reconnaissance."""

from .api import resolve_api_key, create_client, get_account_info, save_api_key
from .search import search, host_info, search_stats
from .formatter import format_result, export_json, export_jsonl, export_txt
from .dorks import load_dorks, search_dorks, list_categories, get_dorks_by_category

__all__ = [
    "resolve_api_key", "create_client", "get_account_info", "save_api_key",
    "search", "host_info", "search_stats",
    "format_result", "export_json", "export_jsonl", "export_txt",
    "load_dorks", "search_dorks", "list_categories", "get_dorks_by_category",
]
