#!/usr/bin/env/python3
# This Python file uses the following encoding:utf-8

# Author: Jolanda de Koff Bulls Eye
# GitHub: https://github.com/BullsEye0
# Website: https://hackingpassion.com
# linkedin: https://www.linkedin.com/in/jolandadekoff
# Facebook: facebook.com/jolandadekoff
# Facebook Page: https://www.facebook.com/ethical.hack.group
# Facebook Group: https://www.facebook.com/groups/hack.passion/
# YouTube: https://www.youtube.com/BullsEyeJolandadeKoff

# Shodan Eye v1.2.0 Created April - August 2019
# Shodan Eye v1.3.0 December 2019
# Copyright (c) 2019 - 2020 Jolanda de Koff.

# Your Shodan API Key can be found here: https://account.shodan.io

########################################################################

import os
import random
import shodan
import time
import sys

# Shodan Eye v1.3.0

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
                        ░                                  ░ ░  v1.3.0

\033[1;m
            \033[1;31mShodan Eye v1.3.0\033[0m

    ✓ The author will not be responsible for any damage caused or any laws broken by the end user, or misuse of information.
    ✓ Just remember, initiating or carrying out any breaches of privacy or data without written permission is illegal.

            Author:  Jolanda de Koff Bulls Eye (Audited by Jonathan A Kurtz)
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
             ▀                 █  █   ██                       v1.3.0

                              ▀
\033[1;m
        \033[1;31mShodan Eye v1.3.0\033[0m
     
     ✓ The author will not be responsible for any damage caused or any laws broken by the end user, or misuse of information.
     ✓ Just remember, initiating or carrying out any breaches of privacy or data without written permission is illegal.
 
             Author:  Jolanda de Koff Bulls Eye (Audited by Jonathan A Kurtz)
             Github:  https://github.com/BullsEye0
             Website: https://HackingPassion.com

        """)

choi = (banner1, banner2)
print (random.choice(choi))
time.sleep(0.5)

data = input("\n[+] \033[34mWould you like to save output to a file? \033[0m(Y/N) ").strip()
l0g = ("")


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(data)
    file.close()


if data.lower().startswith("y"):
    l0g = input("\n[~] \033[34mDesired file name: \033[0m ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] \033[34mSaving skipped\033[0m")
    print ("\n" + "  " + "»" * 78 + "\n")


def showdam():
    if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
        with open("api.txt", "r") as file:
            shodan_api_key = file.readline().rstrip("\n")
    else:
        file = open("api.txt", "w")
        os.system("stty -echo")
        shodan_api_key = input("[!] \033[34mPlease enter a valid Shodan API Key: \033[0m")
        os.system("stty echo")
        file.write(shodan_api_key)
        print ("\n[~] \033[34mFile written: ./api.txt \033[0m")
        file.close()

    api = shodan.Shodan(shodan_api_key)
    time.sleep(0.5)

    limit = 1000  # Just a number
    counter = 1

    try:
        print ("[~] \033[34mChecking Shodan.io API Key... \033[0m")
        api.search("b00m")
        print ("[✓] \033[34mAPI Key Authentication:\033[0m SUCCESS!")
        time.sleep(0.5)
        b00m = input("\n[+] \033[34mEnter your keyword(s):\033[0m ")
        counter += 1
        for banner in api.search_cursor(b00m):
            print ("[+] \033[1;31mIP: \033[1;m" + (banner["ip_str"]))
            print ("[+] \033[1;31mPort: \033[1;m" + str(banner["port"]))
            print ("[+] \033[1;31mOrganization: \033[1;m" + str(banner["org"]))
            print ("[+] \033[1;31mLocation: \033[1;m" + str(banner["location"]))
            print ("[+] \033[1;31mLayer: \033[1;m" + (banner["transport"]))
            print ("[+] \033[1;31mLayer: \033[1;m" + (banner["transport"]))
            print ("[+] \033[1;31mDomains: \033[1;m" + str(banner["domains"]))
            print ("[+] \033[1;31mHostnames: \033[1;m" + str(banner["hostnames"]))
            print ("[+] \033[1;31mThe banner information for the service: \033[1;m\n\n" + (banner["data"]))
            print ("\n[✓] Result: %s. Search query: %s" % (str(counter), str(b00m)))

            data = ("\nIP: " + banner["ip_str"]) + ("\nPort: " + str(banner["port"])) + ("\nOrganisation: " + str(banner["org"])) + ("\nLocation: " + str(banner["location"])) + ("\nLayer: " + banner["transport"]) + ("\nDomains: " + str(banner["domains"])) + ("\nHostnames: " + str(banner["hostnames"])) + ("\nData\n" + banner["data"])
            logger(data)
            print ("\n" + "  " + "»" * 78 + "\n")

            counter += 1
            if counter >= limit:
                exit()

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interrupt Detected: Exiting\033[0")
            time.sleep(0.1)
            sys.exit(1)

    except shodan.APIError as oeps:
            print ("[✘] \033[1;31mError: %s \033[0m" % (oeps))
            sha_api = input("[*] \033[34mWould you like to change the API Key? <Y/N>:\033[0m ").lower()
            if sha_api.lower().startswith("y"):
                file = open("api.txt", "w")
                os.system("stty -echo")
                shodan_api_key = input("[✓] \033[34mPlease enter valid Shodan.io API Key:\033[0m ")
                os.system("stty echo")
                file.write(shodan_api_key)
                print ("\n[~] \033[34mFile written: ./api.txt\033[0m")
                file.close()
                print ("[~] \033[34mRestarting, please wait...\033[0m \n")
                showdam()
            else:
                print ("")
                print ("[•] Exiting...")
                sys.exit()



# =====# Main #===== #
if __name__ == "__main__":
    showdam()

