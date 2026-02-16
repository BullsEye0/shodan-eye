"""Core search functionality — search, host lookup, stats."""

from .formatter import format_result


def search(client, query, limit=100, on_progress=None):
    """Search Shodan and return formatted results.

    Args:
        client: shodan.Shodan instance
        query: Shodan search query string
        limit: Maximum results to return (default 100)
        on_progress: Optional callback(count, result) called per result

    Returns:
        List of formatted result dicts.
    """
    results = []
    for i, banner in enumerate(client.search_cursor(query)):
        if i >= limit:
            break
        result = format_result(banner)
        results.append(result)
        if on_progress:
            on_progress(i + 1, result)
    return results


def host_info(client, ip):
    """Look up a single host and return formatted info."""
    host = client.host(ip)
    from .formatter import format_location, format_list_field

    return {
        "ip": host.get("ip_str", ip),
        "org": host.get("org", "Unknown"),
        "os": host.get("os") or "Unknown",
        "location": format_location(host.get("location")),
        "ports": host.get("ports", []),
        "hostnames": format_list_field(host.get("hostnames")),
        "vulns": host.get("vulns", []),
        "data": [
            {
                "port": svc.get("port"),
                "transport": svc.get("transport", ""),
                "product": svc.get("product", ""),
                "banner": svc.get("data", "")[:500],
            }
            for svc in host.get("data", [])
        ],
    }


def search_stats(client, query, facets=None):
    """Get search statistics with faceted counts.

    Args:
        client: shodan.Shodan instance
        query: Shodan search query string
        facets: List of facet names (default: country, org, port)

    Returns:
        Dict with total count and facet breakdowns.
    """
    if facets is None:
        facets = ["country", "org", "port"]
    result = client.count(query, facets=facets)
    return {
        "total": result.get("total", 0),
        "facets": {
            name: [
                {"value": item["value"], "count": item["count"]}
                for item in result.get("facets", {}).get(name, [])
            ]
            for name in facets
        },
    }
