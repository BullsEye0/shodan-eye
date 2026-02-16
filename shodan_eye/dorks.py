"""Dorks intelligence — parse, categorize, and search the bundled dorks file."""

import os
import re


def load_dorks(filepath=None):
    """Parse the Shodan dorks file into structured entries.

    Each entry has: category, description, query.
    Returns empty list if file not found.
    """
    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), "..",
                                "Shodan_Dorks_The_Internet_of_Sh*t.txt")
        filepath = os.path.normpath(filepath)

    if not os.path.exists(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    dorks = []

    # Parse curated dorks (category -> format, lines with arrow)
    curated_pattern = re.compile(
        r'^(.+?)\s*\u2192\s*$\n(.*?)(?=\n\n|\Z)',
        re.MULTILINE | re.DOTALL
    )
    for match in curated_pattern.finditer(content):
        category = match.group(1).strip()
        body = match.group(2).strip()
        lines = [line.strip() for line in body.split('\n') if line.strip()]
        if not lines:
            continue
        query = lines[-1]
        description = " ".join(lines[:-1]) if len(lines) > 1 else ""
        dorks.append({
            "category": category,
            "description": description,
            "query": query,
        })

    # Parse numbered dorks (N. `query`: description)
    numbered_pattern = re.compile(
        r'^\d+\.\s+`([^`]+)`:\s+(.+)$',
        re.MULTILINE
    )
    for match in numbered_pattern.finditer(content):
        query = match.group(1).strip()
        description = match.group(2).strip()
        category = _categorize_numbered_dork(query, description)
        dorks.append({
            "category": category,
            "description": description,
            "query": query,
        })

    return dorks


def _categorize_numbered_dork(query, description):
    """Derive a category for numbered dorks based on keywords."""
    text = f"{query} {description}".lower()
    categories = {
        "Databases": ["mongodb", "redis", "mysql", "postgresql", "elasticsearch",
                       "couchdb", "cassandra", "mariadb", "neo4j", "oracle",
                       "sql server", "ms sql", "influxdb", "cockroachdb", "db2",
                       "hbase", "riak", "solr", "firebird", "teradata", "sybase",
                       "vertica", "greenplum", "voltdb", "cratedb", "filemaker",
                       "druid"],
        "Remote Access": ["rdp", "vnc", "ssh", "telnet", "teamviewer", "anydesk",
                          "logmein", "splashtop", "nomachine", "connectwise",
                          "gotomypc", "parallels", "guacamole", "radmin", "sftp"],
        "Web Servers": ["apache", "nginx", "tomcat", "http proxy"],
        "IoT / Industrial": ["scada", "modbus", "industrial control", "mqtt",
                             "coap", "smart home", "smart tv"],
        "Network Services": ["dns", "dhcp", "ntp", "ldap", "snmp", "nfs",
                             "netbios", "smb", "socks proxy", "squid proxy",
                             "radius", "vpn", "openvpn", "ftp"],
        "Email": ["smtp", "imap", "pop3", "exchange", "zimbra"],
        "CI/CD & DevOps": ["jenkins", "gitlab", "docker", "kubernetes", "ansible",
                           "puppet", "saltstack", "travis", "circleci"],
        "Monitoring": ["grafana", "zabbix", "nagios", "cacti", "icinga", "graylog",
                       "kibana", "zenoss", "spiceworks"],
        "CMS & E-Commerce": ["wordpress", "joomla", "drupal", "magento",
                             "prestashop", "shopify", "woocommerce", "bigcommerce",
                             "wix", "weebly", "mediawiki"],
        "Hosting Panels": ["cpanel", "plesk", "webmin", "directadmin"],
        "Cameras & Streaming": ["webcam", "ip camera", "rtsp", "webrtc",
                                "surveillance"],
        "Messaging": ["rabbitmq", "kafka", "activemq", "xmpp", "sip",
                      "teamspeak"],
        "Crypto": ["ethereum", "bitcoin"],
        "Storage": ["nas", "emc storage", "netapp", "hadoop", "rsync"],
        "Virtualization": ["vmware", "citrix", "plex"],
        "Security": ["fortinet", "checkpoint", "paloalto", "cyberark", "firewall"],
        "Enterprise": ["sap", "jira", "confluence", "nextcloud", "owncloud"],
    }
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                return cat
    return "Other"


def list_categories(dorks):
    """Return sorted list of unique categories with counts."""
    counts = {}
    for d in dorks:
        cat = d["category"]
        counts[cat] = counts.get(cat, 0) + 1
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))


def search_dorks(dorks, keyword):
    """Search dorks by keyword (case-insensitive) across all fields."""
    keyword = keyword.lower()
    return [
        d for d in dorks
        if keyword in d["category"].lower()
        or keyword in d["description"].lower()
        or keyword in d["query"].lower()
    ]


def get_dorks_by_category(dorks, category):
    """Filter dorks by exact category name."""
    return [d for d in dorks if d["category"] == category]
