#-------------------------------------------------------
# ©️ 2022 - Hannah Renners
# Released under the GNU GENERAL PUBLIC LICENSE Version 3
#-------------------------------------------------------

from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from colorama import Fore, Back, Style
import pwd
import os
import subprocess

#-------------------------------------------------------
# Setup & declaring variables
#-------------------------------------------------------

user = pwd.getpwuid(os.getuid())[0]

sudo = True
yay = True
packages_classes = ['']
packages_extra = ['']
packages_list = ['']
packages_all = ['']
packages_allAUR = ['']

raw_packages = {
    "non-aur": {
        "basic": ['man-db', 'neofetch', 'alacritty', 'git', 'fish', 'yakuake', 'libqalculate'],
        "image": ['krita', 'gimp', 'darktable', 'inkscape'],
        "3d": ['blender'],
        "code": ['code', 'python', 'rustup', 'cmake'],
        "office": ['xournalpp', 'libreoffice-fresh'],
        "utils": ['nextcloud-client', 'qalculate-gtk'],
        "video": ['kdenlive'],
        "gaming": ['']
    },
    "aur": {
        "basic": [''],
        "image": [''],
        "3d": [''],
        "code": [''],
        "office": ['notion-app-enhanced'],
        "utils": ['brave-bin'],
        "video": [''],
        "gaming": ['polymc-bin', 'steam', 'heroic-games-launcher-bin', 'mangohud']
    }
}

#-------------------------------------------------------
# Main logic
#-------------------------------------------------------

def __main__(packages_all, packages_allAUR):
    SudoQuestion()
    yay = YayQuestion()
    packages_classes = PackageClasses()
    packages_extra = ExtraPackages()
    packages_list = ListPackages()

    # Yay logic
    if yay == True:
        InstallYay()
    else:
        print(f"{user} chose not to install yay. Skipping yay instalation")

    # Package logic
    def PackageLogic():

        raw_nonAUR = raw_packages.get('non-aur')
        raw_AUR = raw_packages.get('aur')

        print(packages_classes.get(0))

        for x in packages_classes.get(0):
            packages_all = packages_all + raw_nonAUR.get(x)

        if yay == True:
            for x in packages_classes.get(0):
                packages_allAUR = packages_allAUR + raw_AUR.get(x)
    
    PackageLogic()
    PackageInstall(yay, packages_all, packages_allAUR)

    FishAliases()
    
    print(Fore.RED + "We're all done! I would suggest rebooting now! See you soon :>")

    exit()

#-------------------------------------------------------
# Copy stuff
#-------------------------------------------------------

#-------------------------------------------------------
# 
#-------------------------------------------------------
# print(Fore. + "" + Style.RESET_ALL)

#-------------------------------------------------------
# Initial User configuration
#-------------------------------------------------------

def SudoQuestion():

    #
    # Sudo?
    #

    print("\n\n\n\n\n")

    # Asking user if SUDO
    print(f"You're user {user}. The following installation requieres you to have SUDO priviliges!")
    q_sudoPriv = [{"type": "confirm", "message": "Do you have sudo priviliges?"}]
    sudoPriv = prompt(q_sudoPriv)

    # SUDO Question response
    if sudoPriv[0] == False:
        print(Fore.RED + "Please run this script with a USER that has SUDO priviliges!" + Style.RESET_ALL)
        exit()
    else:
        print(Fore.GREEN + "Great! Continuing with instalation." + Style.RESET_ALL)
        sudo = True

def YayQuestion():
    #
    # Yay?
    #

    print("\n\n\n\n\n")

    # Asking if yay should be installed
    print("To install packages from the AUR you can install yay to make it easier. \nIf you don't know how to install packages manually you should not install yay!\nIf you want to install AUR packagese via this program later you need to install yay.")
    q_installYay = [{"type": "confirm", "message": "Do you want to install Yay?", "name": "yay"}]
    p_installYay = prompt(q_installYay)
    installYay = p_installYay['yay']

    # Yay Question response
    if installYay == False:
        print(Fore.RED + "Not installing Yay!" + Style.RESET_ALL)
        return installYay
    else:
        print(Fore.GREEN + "Installing Yay Soon!" + Style.RESET_ALL)
        return installYay

#-------------------------------------------------------
# Package configuration
#-------------------------------------------------------

def PackageClasses():
    
    #
    # Package classes
    #
   
    print("\n\n\n\n\n")

    q_packageClasses = [
        {
            "type": "list",
            "message": "Please select all package classes you want to install. Navigate with <Up> <Down> and (de-)select with <Space>. Confirm with <Enter>.",
            "choices": [
                Choice("basic", name="Basic: Essential utility's and library's", enabled=True),
                Choice("image", name="Image: Image editing, manipulation, and drawing tools", enabled=True),
                Choice("3d", name="3D: 3D rendering and creation", enabled=True),
                Choice("video", name="Video creation & playback software", enabled=True),
                Choice("code", name="Code: Coding tools and toolchains", enabled=True),
                Choice("office", name="Office: Office and Notetaking", enabled=True),
                Choice("utils", name="Util: Various utility software", enabled=True),
                Choice("gaming", name="Gaming: Launchers & gaming utility's", enabled=True)
            ],
            "multiselect": True,
            "transformer": lambda result: f"\nInstalling the following package classes:"
        }
    ]
    q_packageClasses   = prompt(q_packageClasses)
    for i in q_packageClasses :
        print(Fore.LIGHTBLUE_EX + f"{q_packageClasses [i]}" + Style.RESET_ALL)
    return q_packageClasses

def ExtraPackages():
    #
    # Extra packages
    #

    q_extraPackages = [
        {
            "type": "list",
            "message": "Please select all extra packages you want to install. Navigate with <Up> <Down> and (de-)select with <Space>. Confirm with <Enter>.",
            "multiselect": True,
            "choices": [
                Choice("spotify", enabled=True),
                Separator(),
                Choice("Firefox", enabled=False),
                Choice("chromium-bin", enabled=False),
                Separator(),
                Choice("vlc", enabled=False)
            ]
        }
    ]
    p_extraPackages = prompt(q_extraPackages)
    return q_extraPackages

def ListPackages():
    q_listPackages =[
        {
            "type": "input",
            "message": "If you want to install any additional packages you can list them below (non AUR and AUR if you have selected yay). Seperate them by space."
        }
    ]
    return prompt(q_listPackages)


#-------------------------------------------------------
# Package instalation
#-------------------------------------------------------

def InstallYay(installAUR, pack_nonAUR, pack_AUR):
    print("Installing yay now.")

    subprocess.run(["fish", "install-yay.fish"])

def PackageInstall():
    print("Installing packages now!\nBeginning with non AUR packages.")
    
    string_pack_nonAUR = ""
    strin_pack_AUR = ""

    # Seperating packages into strings
    for x in pack_nonAUR:
        string_pack_nonAUR = string_pack_nonAUR + x + " " 
    if installAUR == True:
        for x in pack_AUR:
            string_pack_AUR = string_pack_AUR + x  + " " 

    cmd = 'sudo pacman -Syu ' + string_pack_nonAUR 
    subprocess.run(cmd.split())

    if installAUR == True:
        cmd = 'yay -S ' + string_pack_AUR
        subprocess.run(cmd.split())

#-------------------------------------------------------
# Config modification
#-------------------------------------------------------

#-------------------------------------------------------
# Fish aliases
#-------------------------------------------------------

def FishAliases():
    cmd = 'fish -c \'alias -s nf="cd && fish"\''
    subprocess.run(cmd.split())

    cmd = 'fish -c \'alias -s please="sudo"\''
    subprocess.run(cmd.split())

    cmd = 'fish -c \'alias -s q="qalc"\''
    subprocess.run(cmd.split())

    cmd = 'fish -c \'alias -s wa="brave --homepage https://www.wolframalpha.com/"\''
    subprocess.run(cmd.split())

    cmd = 'fish -c \'alias -s pm="sudo pacman -Syu"\''
    subprocess.run(cmd.split())

    cmd = 'fish -c \'alias -s start_qemu="sudo systemctl start libvirtd.service"\''
    subprocess.run(cmd.split())

#-------------------------------------------------------
# Calling __main__
#-------------------------------------------------------

__main__(packages_all, packages_allAUR)