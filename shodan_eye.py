#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# Bulls Eye: https://github.com/BullsEye0

# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!

# Your Shodan API Key can be found here: https://account.shodan.io
# Have fun..!

# Created April 2019
# Copyright (c) 2019 Jolanda de Koff, Bulls Eye.


import random
import sys
import shodan
import time
# Thats all for now :)


banner1 = """

\033[1;31m

  ██████ ██░ ██ ▒█████ ▓█████▄ ▄▄▄      ███▄    █    ▓████▓██   ██▓█████
▒██    ▒▓██░ ██▒██▒  ██▒██▀ ██▒████▄    ██ ▀█   █    ▓█   ▀▒██  ██▓█   ▀
░ ▓██▄  ▒██▀▀██▒██░  ██░██   █▒██  ▀█▄ ▓██  ▀█ ██▒   ▒███   ▒██ ██▒███
  ▒   ██░▓█ ░██▒██   ██░▓█▄   ░██▄▄▄▄██▓██▒  ▐▌██▒   ▒▓█  ▄ ░ ▐██▓▒▓█  ▄
▒██████▒░▓█▒░██░ ████▓▒░▒████▓ ▓█   ▓██▒██░   ▓██░   ░▒████▒░ ██▒▓░▒████▒
▒ ▒▓▒ ▒ ░▒ ░░▒░░ ▒░▒░▒░ ▒▒▓  ▒ ▒▒   ▓▒█░ ▒░   ▒ ▒    ░░ ▒░ ░ ██▒▒▒░░ ▒░ ░
░ ░▒  ░ ░▒ ░▒░ ░ ░ ▒ ▒░ ░ ▒  ▒  ▒   ▒▒ ░ ░░   ░ ▒░    ░ ░  ▓██ ░▒░ ░ ░  ░
░  ░  ░  ░  ░░ ░ ░ ░ ▒  ░ ░  ░  ░   ▒     ░   ░ ░       ░  ▒ ▒ ░░    ░
      ░  ░  ░  ░   ░ ░    ░         ░  ░        ░       ░  ░ ░       ░  ░
                        ░                                  ░ ░

\033[1;m

Shodan Eye | Shall we play a game..?

By Jolanda de koff | facebook.com/jolandadekoff

I like to See Ya hacking... *

        """

banner2 = """

\033[1;31m


   ▄▄▄▄▄    ▄  █ ████▄ ██▄   ██      ▄       ▄███▄ ▀▄    ▄ ▄███▄
  █     ▀▄ █   █ █   █ █  █  █ █      █      █▀   ▀  █  █  █▀   ▀
▄  ▀▀▀▀▄   ██▀▀█ █   █ █   █ █▄▄█ ██   █     ██▄▄     ▀█   ██▄▄
 ▀▄▄▄▄▀    █   █ ▀████ █  █  █  █ █ █  █     █▄   ▄▀  █    █▄   ▄▀
              █        ███▀     █ █  █ █     ▀███▀  ▄▀     ▀███▀
             ▀                 █  █   ██

                              ▀
\033[1;m

Shodan Eye | Shall we play a game..?

By Jolanda de koff | facebook.com/jolandadekoff

I like to See Ya hacking... *

        """

stream = (banner1, banner2)

print random.choice(stream)
time.sleep(0.3)


# Your Shodan API Key can be found here: https://account.shodan.io
key = raw_input("\n[+] Enter your API key: ")
shodan_api_key = (key)
api = shodan.Shodan(shodan_api_key)
time.sleep(0.3)


b00m = raw_input("\n[+] Enter your keyword(s): ")
time.sleep(0.4)


def showdam():
    limit = 628  # Just a number
    counter = 0

    try:
        for banner in api.search_cursor(b00m):

            print"\033[1;31mIP: \033[1;m" + (banner["ip_str"])
            print"\033[1;31mOrganization: \033[1;m" + str(banner["org"])
            print"\033[1;31mLocation: \033[1;m" + str(banner["location"])
            print"\033[1;31mLayer: \033[1;m" + (banner["transport"])
            print"\033[1;31mDomains: \033[1;m" + str(banner["domains"])
            print"\033[1;31mHostnames: \033[1;m" + str(banner["hostnames"])
            print"\033[1;31mPort: \033[1;m" + str(banner["port"])
            print"\n"
            print"\033[1;31mThe banner information for the service: \033[1;m\n" + (banner["data"])
            time.sleep(0.2)
            print("*************************************\n")

            counter += 1
            if counter >= limit:
                break

    except KeyboardInterrupt:
            print "\n"
            print(" [-] User Interruption Detected.")
            time.sleep(0.5)
            sys.exit(1)


showdam()
