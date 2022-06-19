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

sudo = True
yay = True
packages_classes = ['']
packages_extra = ['']
packages_list = ['']

def __main__():
    sudo_question()
    yay = yay_question()
    packages_classes = package_classes()
    packages_extra = extra_packages()
    packages_list = list_packages()

    if yay == True:
        #install_yay()
        print("install yay")
    else:
        print(f"{user} chose not to install yay. Skipping yay instalation")

    package_install()

    exit()

#-------------------------------------------------------
# Copy stuff
#-------------------------------------------------------

#-------------------------------------------------------
# 
#-------------------------------------------------------
# print(Fore. + "" + Style.RESET_ALL)

#-------------------------------------------------------
# Setup & declaring variables
#-------------------------------------------------------

user = pwd.getpwuid(os.getuid())[0]

#-------------------------------------------------------
# Initial User configuration
#-------------------------------------------------------

def sudo_question():

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

def yay_question():
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

def package_classes():
    
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

def extra_packages():
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
                Separator()
            ]
        }
    ]
    p_extraPackages = prompt(q_extraPackages)
    return q_extraPackages

def list_packages():
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

def install_yay():
    print("Installing yay now.")

    subprocess.run(["fish", "install-yay.fish"])

def package_install():
    print("Installing packages now!")

#-------------------------------------------------------
# Calling __main__
#-------------------------------------------------------

__main__()