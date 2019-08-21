#!/usr/bin/env/python
# This Python file uses the following encoding:utf-8

# Author: Jolanda de Koff
# Bulls Eye: https://github.com/BullsEye0
# linkedin: https://www.linkedin.com/in/jolandadekoff
# Facebook: facebook.com/jolandadekoff
# Facebook Group: https://www.facebook.com/groups/ethicalhacking.hacker
# Facebook Page: https://www.facebook.com/ethical.hack.group

# Created April - August 2019 | Copyright (c)2019 Jolanda de Koff.
# Your Shodan API Key can be found here: https://account.shodan.io

# A notice to all nerds and n00bs...
# If you will copy developers work it will not make you a hacker..!
# Resepect all developers, we doing this because it's fun... :)

#######################################################################

import os
import random
import shodan
import time

import sys
reload(sys)
sys.setdefaultencoding("utf8")
# Shodan Eye v1.2.0

banner1 = """

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
                        ░                                  ░ ░  v1.2.0

\033[1;m
            \033[1;31mShodan Eye v1.2.0\033[0m

    The author is not responsible for any damage, misuse of the information..!
    This tool shall only be used to expand knowledge and not for
    causing malicious or damaging attacks.
    Performing any hacks without written permission is illegal.

            Author: Jolanda de Koff
            Bulls Eye | https://github.com/BullsEye0

            \033[1;31mHi there, Shall we play a game..?\033[0m 😃
        """

banner2 = """

\033[1;31m


   ▄▄▄▄▄    ▄  █ ████▄ ██▄   ██      ▄       ▄███▄ ▀▄    ▄ ▄███▄
  █     ▀▄ █   █ █   █ █  █  █ █      █      █▀   ▀  █  █  █▀   ▀
▄  ▀▀▀▀▄   ██▀▀█ █   █ █   █ █▄▄█ ██   █     ██▄▄     ▀█   ██▄▄
 ▀▄▄▄▄▀    █   █ ▀████ █  █  █  █ █ █  █     █▄   ▄▀  █    █▄   ▄▀
              █        ███▀     █ █  █ █     ▀███▀  ▄▀     ▀███▀
             ▀                 █  █   ██                       v1.2.0

                              ▀
\033[1;m
        \033[1;31mShodan Eye v1.2.0\033[0m

    The author is not responsible for any damage, misuse of the information..!
    This tool shall only be used to expand knowledge and not for
    causing malicious or damaging attacks.
    Performing any hacks without written permission is illegal.

        Author: Jolanda de Koff
        Bulls Eye | https://github.com/BullsEye0

        \033[1;31mHi there, Shall we play a game..?\033[0m 😃
        """

choi = (banner1, banner2)

print random.choice(choi)
time.sleep(0.5)


def showdam():
    if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
        with open("api.txt", "r") as file:
            shodan_api_key = file.readline().rstrip("\n")
    else:
        file = open("api.txt", "w")
        shodan_api_key = raw_input("[!] Please enter a valid Shodan API Key: ")
        file.write(shodan_api_key)
        print "[~] File written: ./api.txt"
        file.close()

    api = shodan.Shodan(shodan_api_key)
    time.sleep(0.4)

    limit = 999  # Just a number
    counter = 1

    try:
        print "[~] Checking Shodan.io API Key..."
        api.search("b00m")
        print "[✓] API Key Authentication: SUCCESS..!"
        time.sleep(0.5)
        b00m = raw_input("\n[+] Enter your keyword(s): ")
        counter = counter + 1
        for banner in api.search_cursor(b00m):
            print "[+] \033[1;31mIP: \033[1;m" + (banner["ip_str"])
            print "[+] \033[1;31mPort: \033[1;m" + str(banner["port"])
            print "[+] \033[1;31mOrganization: \033[1;m" + str(banner["org"])
            print "[+] \033[1;31mLocation: \033[1;m" + str(banner["location"])
            print "[+] \033[1;31mLayer: \033[1;m" + (banner["transport"])
            print "[+] \033[1;31mDomains: \033[1;m" + str(banner["domains"])
            print "[+] \033[1;31mHostnames: \033[1;m" + str(banner["hostnames"])
            print "[+] \033[1;31mThe banner information for the service: \033[1;m\n\n" + (banner["data"])
            print "\n[✓] Result: %s. Search query: %s" % (str(counter), str(b00m))
            time.sleep(0.1)
            print "+" * 60 + "\n"

            counter += 1
            if counter >= limit:
                exit()

    except KeyboardInterrupt:
            print "\n"
            print "\033[1;91m[!] User Interruption Detected..!\033[0"
            time.sleep(0.5)
            print "\n\n\t\033[1;91m[!] I like to See Ya, Hacking\033[0m\n\n"
            time.sleep(0.5)
            sys.exit(1)

    except shodan.APIError as oeps:
            print "[✘] Error: %s" % (oeps)
            sha_api = raw_input("[*] Would you like to change the API Key? <Y/n>: ").lower()
            if sha_api.startswith("y" or "Y"):
                file = open("api.txt", "w")
                shodan_api_key = raw_input("[✓] Please enter valid Shodan.io API Key: ")
                file.write(shodan_api_key)
                print "[~] File written: ./api.txt"
                file.close()
                print "[~] Restarting the Platform, Please wait... \n"
                time.sleep(1)
                showdam()
            else:
                print ""
                print "[•] Exiting Platform... \033[1;91m[!] I like to See Ya, Hacking\033[0m\n\n"
                sys.exit()

    print "\n\n\tShodan Eye \033[1;91mI like to See Ya, Hacking \033[0m\n\n"


# =====# Main #===== #
if __name__ == "__main__":
    showdam()

