from turtle import update
import requests, os
from InquirerPy import prompt

def updateMirrors():
    # check if run as sudo
    if os.geteuid() != 0:
        print("This program was not run as sudo - please run as sudo. Closing...")
        exit()

    file = open('/etc/pacman.d/mirrorlist', 'w')

    url_all = 'https://archlinux.org/mirrorlist/?country=all&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_de = 'https://archlinux.org/mirrorlist/?country=DE&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_us = 'https://archlinux.org/mirrorlist/?country=US&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_uk = 'https://archlinux.org/mirrorlist/?country=UK&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_au = 'https://archlinux.org/mirrorlist/?country=AU&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_ca = 'https://archlinux.org/mirrorlist/?country=CA&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_nl = 'https://archlinux.org/mirrorlist/?country=NL&protocol=http&protocol=https&ip_version=4&ip_version=6'

    # make menu for mirror selection
    mirror_menu = {
        "type": "list",
        "message": "Select a mirror",
        "name": "mirror",
        "choices": [
            "All",
            "Germany",
            "United States",
            "United Kingdom",
            "Australia",
            "Canada",
            "Netherlands"
        ]
    }
    mirror_menu = prompt(mirror_menu)

    # for each choise get the mirror list
    if mirror_menu.get("mirror") == "All":
        r = requests.get(url_all)
    elif mirror_menu.get("mirror") == "Germany":
        r = requests.get(url_de)
    elif mirror_menu.get("mirror") == "United States":
        r = requests.get(url_us)
    elif mirror_menu.get("mirror") == "United Kingdom":
        r = requests.get(url_uk)
    elif mirror_menu.get("mirror") == "Australia":
        r = requests.get(url_au)
    elif mirror_menu.get("mirror") == "Canada":
        r = requests.get(url_ca)
    elif mirror_menu.get("mirror") == "Netherlands":
        r = requests.get(url_nl)

    text = r.text

    # put text into list by line
    text_list = text.split('\n')

    # replace all '#Server' with 'Server'
    for i in range(len(text_list)):
        text_list[i] = text_list[i].replace('#Server', 'Server')

    # combine list into string
    text = '\n'.join(text_list)

    # add line to beginning of text
    text = '# Updated by Hannah\'s Arch-Scripts :>\n' + text

    file.write(text)

    print("Mirrorlist updated!")

updateMirrors()