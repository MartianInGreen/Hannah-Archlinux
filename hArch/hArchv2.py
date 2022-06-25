#-------------------------------------------------------
# ©️ 2022 - Hannah Renners
# Released under the GNU GENERAL PUBLIC LICENSE Version 3
# hARch v2.0
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
# Basic stuff
#-------------------------------------------------------

def getUser():
    return pwd.getpwuid(os.getuid())[0]

def getWorkingDir():
    return os.getcwd()

#-------------------------------------------------------
# Main logic
#-------------------------------------------------------

def __main__():
    welcome()
    main_menu = mainMenu()

    if main_menu == "install_class":
        installClass()
    elif main_menu == "install_name":
        installName()
    elif main_menu == "configs":
        configs()
    elif main_menu == "exit":
        exit()

#-------------------------------------------------------
# Secondary logic
#-------------------------------------------------------

def welcome():
    print(Fore.RED + "Welcome to hArch v2.0!")
    print(Fore.GREEN + "Starting execution of the Python program...")
    print(Fore.GREEN + "This program will help you set up your Arch installation." + Style.RESET_ALL)

def mainMenu():
    # make a main menu with InquirerPy
    main_menu = {
        "type": "list",
        "message": "What would you like to do?",
        "choices": [
            Choice("install_class", "Install packages by category/class"),
            Choice("install_name", "Install packages by name"),
            Choice("configs", "Configue programs & configs"),
            Choice("exit", "Exit")
        ]
    }
    out = prompt(main_menu)
    out = out[0]
    return out

#-------------------------------------------------------
# Secondary logic - install by class
#-------------------------------------------------------

#-------------------------------------------------------
# Secondary logic - install by name
#-------------------------------------------------------

#-------------------------------------------------------
# Secondary logic - configs
#-------------------------------------------------------

#-------------------------------------------------------
# exectue Main logic
#-------------------------------------------------------

__main__()