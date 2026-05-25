#!/usr/bin/env/python3
# This Python file uses the following encoding:utf-8

# ===== #
#   
# ▀█████████▄     ▄████████         Websites: HackingPassion.com | Bullseye0.com
#   ███    ███   ███    ███         Author: Jolanda de Koff | Bulls Eye
#   ███    ███   ███    █▀          GitHub: https://github.com/BullsEye0
#  ▄███▄▄▄██▀   ▄███▄▄▄             linkedin: https://www.linkedin.com/in/jolandadekoff
# ▀▀███▀▀▀██▄  ▀▀███▀▀▀             Facebook Group: https://www.facebook.com/groups/hack.passion/
#   ███    ██▄   ███    █▄          Facebook: https://www.facebook.com/profile.php?id=100069546190609
#   ███    ███   ███    ███         Twitter: https://twitter.com/bulls__eye
# ▄█████████▀    ██████████         LBRY: https://lbry.tv/$/invite/@hackingpassion:9
#                                   
#          Bulls Eye..!
# ===== #

# Shodan Eye v1.2.0 Created April - August 2019
# Shodan Eye v1.3.0 December 2019
# Copyright (c) 2019 - 2026 Jolanda de Koff.

# Your Shodan API Key can be found here: https://account.shodan.io

########################################################################

# A notice to all nerds and n00bs...
# If you copy the developer's work, it will not make you a hacker..!
# Respect all developers, we're doing this because it's fun...

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

    ✓ The author is not responsible for any damage, misuse of the information.
    ✓ Shodan Eye shall only be used to expand knowledge and not for
      causing malicious or damaging attacks.
    ✓ Just remember, Performing any hacks without written permission is illegal ..!

            Author:  Jolanda de Koff Bulls Eye
            Github:  https://github.com/BullsEye0
            Website: https://HackingPassion.com

            \033[1;31mHi there, Shall we play a game..?\033[0m 😃
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

    ✓ The author is not responsible for any damage, misuse of the information.
    ✓ Shodan Eye shall only be used to expand knowledge and not for
      causing malicious or damaging attacks.
    ✓ Just remember, Performing any hacks without written permission is illegal ..!

            Author:  Jolanda de Koff Bulls Eye
            Github:  https://github.com/BullsEye0
            Website: https://HackingPassion.com

            \033[1;31mHi there, Shall we play a game..?\033[0m 😃
        """)

choi = (banner1, banner2)
print (random.choice(choi))
time.sleep(0.5)

data = input("\n[+] \033[34mDo you like to save the output in a file? \033[0m(Y/N) ").strip()
l0g = ("")


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(data)
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("\n[~] \033[34mGive the file a name: \033[0m ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] \033[34mSaving is skipped\033[0m")
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
    time.sleep(0.4)

    limit = 888  # Just a number
    counter = 1

    try:
        print ("[~] \033[34mChecking Shodan.io API Key... \033[0m")
        api.search("b00m")
        print ("[✓] \033[34mAPI Key Authentication:\033[0m SUCCESS..!")
        time.sleep(0.5)
        b00m = input("\n[+] \033[34mEnter your keyword(s):\033[0m ")
        counter = counter + 1
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
            time.sleep(0.1)
            print ("\n" + "  " + "»" * 78 + "\n")

            counter += 1
            if counter >= limit:
                exit()

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    except shodan.APIError as oeps:
            print ("[✘] \033[1;31mError: %s \033[0m" % (oeps))
            sha_api = input("[*] \033[34mWould you like to change the API Key? <Y/N>:\033[0m ").lower()
            if sha_api.startswith("y" or "Y"):
                file = open("api.txt", "w")
                os.system("stty -echo")
                shodan_api_key = input("[✓] \033[34mPlease enter valid Shodan.io API Key:\033[0m ")
                os.system("stty echo")
                file.write(shodan_api_key)
                print ("\n[~] \033[34mFile written: ./api.txt\033[0m")
                file.close()
                print ("[~] \033[34mRestarting the Platform, Please wait...\033[0m \n")
                time.sleep(1)
                showdam()
            else:
                print ("")
                print ("[•] Exiting Platform... \033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
                sys.exit()

    print ("\n\n\tShodan Eye \033[1;91mI like to See Ya, Hacking \033[0m😃\n\n")


# =====# Main #===== #
if __name__ == "__main__":
    showdam()

