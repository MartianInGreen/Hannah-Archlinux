from turtle import update
import requests, os

def updateMirrors():
    # check if run as sudo
    if os.geteuid() != 0:
        print("This program was not run as sudo - please run as sudo. Closing...")
        exit()

    file = open('/etc/pacman.d/mirrorlist', 'w')

    url = 'https://archlinux.org/mirrorlist/?country=DE&protocol=http&protocol=https&ip_version=4&ip_version=6'

    r = requests.get(url)

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