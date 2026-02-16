"""Legacy interactive wrapper — preserves original UX using the new library."""

import getpass
import random
import re
import sys

from .api import resolve_api_key, create_client, get_account_info, save_api_key
from .search import search
from .formatter import (
    RED, BLUE, RESET, result_to_console, export_json, export_txt, format_result,
)
from .dorks import load_dorks

banner1 = ("""

\033[1;31m

  ██████ ██░ ██ ▒█████ ▓█████▄ ▄▄▄      ███▄    █    ▓████▓██   ██▓█████
▒██    ▒▓██░ ██▒██▒  ██▒██▀ ██▒████▄    ██ ▀█   █    ▓█   ▀▒██  ██▓█   ▀
░ ▓██▄  ▒██▀▀██▒██░  ██░██   █▒██  ▀█▄ ▓██  ▀█ ██▒   ▒███   ▒██ ██▒███
  ▒   ██░▓█ ░██▒██   ██░▓█▄  █░██▄▄▄▄██▓██▒  ▐▌██▒   ▒▓█  ▄ ░ ▐██▓▒▓█  ▄
▒██████▒░▓█▒░██░ ████▓▒░▒████▓ ▓█   ▓██▒██░   ▓██░   ░▒████▒░ ██▒▓░▒████▒
▒ ▒▓▒ ▒ ░▒ ░░▒░░ ▒░▒░▒░ ▒▒▓  ▒ ▒▒   ▓▒█░ ▒░   ▒ ▒    ░░ ▒░ ░ ██▒▒▒░░ ▒░ ░
░ ░▒  ░ ░▒ ░▒░ ░ ░ ▒ ▒░ ░ ▒  ▒  ▒   ▒▒ ░ ░░   ░ ▒░    ░ ░  ▓██ ░▒░ ░ ░  ░
░  ░  ░  ░  ░░ ░ ░ ░ ▒  ░ ░  ░  ░   ▒     ░   ░ ░       ░  ▒ ▒ ░░    ░
      ░  ░  ░  ░   ░ ░    ░         ░  ░        ░       ░  ░ ░       ░  ░
                        ░                                  ░ ░  v2.0.0

\033[1;m
            \033[1;31mShodan Eye v2.0.0\033[0m

    Author:  Jolanda de Koff Bulls Eye
    Github:  https://github.com/BullsEye0
    Website: https://HackingPassion.com
        """)

banner2 = ("""

\033[1;31m


   ▄▄▄▄▄    ▄  █ ████▄ ██▄   ██      ▄       ▄███▄ ▀▄    ▄ ▄███▄
  █     ▀▄ █   █ █   █ █  █  █ █      █      █▀   ▀  █  █  █▀   ▀
▄  ▀▀▀▀▄   ██▀▀█ █   █ █   █ █▄▄█ ██   █     ██▄▄     ▀█   ██▄▄
 ▀▄▄▄▄▀    █   █ ▀████ █  █  █  █ █ █  █     █▄   ▄▀  █    █▄   ▄▀
              █        ███▀     █ █  █ █     ▀███▀  ▄▀     ▀███▀
             ▀                 █  █   ██                       v2.0.0

                              ▀
\033[1;m
        \033[1;31mShodan Eye v2.0.0\033[0m

    Author:  Jolanda de Koff Bulls Eye
    Github:  https://github.com/BullsEye0
    Website: https://HackingPassion.com
        """)

BANNERS = (banner1, banner2)


def _progress(count, result):
    print(f"\r{BLUE}[~] Fetched {count} results...{RESET}", end="", flush=True)


def run():
    """Legacy interactive entry point."""
    print(random.choice(BANNERS))

    # Save preferences
    save_choice = input(f"\n[+] {BLUE}Save output to file? {RESET}(Y/N) ").strip()
    save_enabled = save_choice.lower().startswith("y")
    log_filename = ""
    output_format = "txt"

    if save_enabled:
        log_filename = input(f"\n[~] {BLUE}Filename (no extension): {RESET}").strip()
        if not re.match(r'^[a-zA-Z0-9_\-]+$', log_filename):
            print(f"[!] {RED}Invalid filename. Use only letters, numbers, underscores, hyphens.{RESET}")
            sys.exit(1)
        fmt = input(f"[~] {BLUE}Format (txt/json): {RESET}").strip().lower()
        if fmt in ("json", "j"):
            output_format = "json"
        print("\n" + "  " + "\u00bb" * 78 + "\n")
    else:
        print(f"[!] {BLUE}Saving is skipped{RESET}")
        print("\n" + "  " + "\u00bb" * 78 + "\n")

    # API key + auth loop
    while True:
        api_key = resolve_api_key()
        if not api_key:
            api_key = getpass.getpass(f"[!] {BLUE}Enter your Shodan API Key: {RESET}")
            save_api_key(api_key)

        client = create_client(api_key)

        try:
            print(f"[~] {BLUE}Checking API Key...{RESET}")
            info = get_account_info(client)
            print(f"[✓] {BLUE}API Key valid!{RESET} Plan: {info['plan']} | "
                  f"Query credits: {info['query_credits']} | "
                  f"Scan credits: {info['scan_credits']}")

            # Search loop
            while True:
                query = input(f"\n[+] {BLUE}Enter search query:{RESET} ").strip()
                if not query:
                    continue

                limit_str = input(f"[~] {BLUE}Max results (default 100):{RESET} ").strip()
                limit = int(limit_str) if limit_str.isdigit() else 100

                print()
                results = search(client, query, limit=limit, on_progress=_progress)
                print(f"\r{BLUE}[✓] Fetched {len(results)} results.{RESET}          ")

                # Display results
                for i, result in enumerate(results, 1):
                    print(result_to_console(result))
                    print(f"\n[✓] Result: {i}. Search query: {query}")
                    print("\n" + "  " + "\u00bb" * 78 + "\n")

                # Save
                if save_enabled and results:
                    if output_format == "json":
                        path = f"{log_filename}.json"
                        export_json(results, path, query=query)
                    else:
                        path = f"{log_filename}.txt"
                        export_txt(results, path, query=query)
                    print(f"[~] {BLUE}Results saved to {path}{RESET}")

                # Continue?
                again = input(f"\n[+] {BLUE}Search again? {RESET}(Y/N) ").strip()
                if not again.lower().startswith("y"):
                    break

            break

        except KeyboardInterrupt:
            print(f"\n\n{RED}[!] User Interruption Detected{RESET}")
            sys.exit(1)

        except Exception as api_error:
            print(f"[✘] {RED}Error: {api_error}{RESET}")
            change = input(f"[*] {BLUE}Change API Key? (Y/N):{RESET} ").strip()
            if change.lower().startswith("y"):
                api_key = getpass.getpass(f"[✓] {BLUE}Enter new API Key:{RESET} ")
                save_api_key(api_key)
                continue
            else:
                sys.exit()

    print(f"\n\n\tShodan Eye {RED}See Ya! {RESET}\n")
