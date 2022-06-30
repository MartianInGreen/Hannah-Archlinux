from turtle import update
import requests, os, subprocess
from InquirerPy import prompt

def updateMirrors():

    url_all = 'https://archlinux.org/mirrorlist/?country=all&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_de = 'https://archlinux.org/mirrorlist/?country=DE&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_us = 'https://archlinux.org/mirrorlist/?country=US&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_uk = 'https://archlinux.org/mirrorlist/?country=GB&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_au = 'https://archlinux.org/mirrorlist/?country=AU&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_ca = 'https://archlinux.org/mirrorlist/?country=CA&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_nl = 'https://archlinux.org/mirrorlist/?country=NL&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_fr = 'https://archlinux.org/mirrorlist/?country=FR&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_is = 'https://archlinux.org/mirrorlist/?country=IS&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_nz = 'https://archlinux.org/mirrorlist/?country=NZ&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_no = 'https://archlinux.org/mirrorlist/?country=NO&protocol=http&protocol=https&ip_version=4&ip_version=6'
    url_in = 'https://archlinux.org/mirrorlist/?country=IN&protocol=http&protocol=https&ip_version=4&ip_version=6'

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
            "Netherlands",
            "France",
            "Iceland",
            "New Zealand",
            "Norway",
            "India"
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
    elif mirror_menu.get("mirror") == "France":
        r = requests.get(url_fr)
    elif mirror_menu.get("mirror") == "Iceland":
        r = requests.get(url_is)
    elif mirror_menu.get("mirror") == "New Zealand":
        r = requests.get(url_nz)
    elif mirror_menu.get("mirror") == "Norway":
        r = requests.get(url_no)
    elif mirror_menu.get("mirror") == "India":
        r = requests.get(url_in)


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

    # check if program was run as sudo
    if os.geteuid() != 0:
        # create temp python file
        tmp = open('/tmp/mirrorlist.py', 'w')
        cmd = 'sudo python /tmp/mirrorlist.py'

        tmp_cmd_1 = 'import os'
        tmp_cmd_2 = f"text = \'\\n\'.join({text_list})"
        tmp_cmd_3 = '# Updated by Hannah\'s Arch-Scripts :>\n' + text
        tmp_cmd_4 = 'file = open(\'/etc/pacman.d/mirrorlist\', \'w\')'
        tmp_cmd_5 = 'file.write(text)'
        tmp_cmd_6 = 'file.close()'

        # join all commands into one string
        tmp_cmd = tmp_cmd_1 + '\n' + tmp_cmd_2 + '\n' + tmp_cmd_3 + '\n' + tmp_cmd_4 + '\n' + tmp_cmd_5 + '\n' + tmp_cmd_6 + '\n'

        tmp.write(tmp_cmd)
        tmp.close()

        # run temp python file
        subprocess.run(cmd.split())

        # delete temp python file
        os.remove('/tmp/mirrorlist.py')
    else:
        file = open('/etc/pacman.d/mirrorlist', 'w')
        file.write(text)
        file.close()

    print("Mirrorlist updated!")

updateMirrors()