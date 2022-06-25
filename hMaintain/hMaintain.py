#-------------------------------------------------------
# ©️ 2022 - Hannah Renners
# Released under the GNU GENERAL PUBLIC LICENSE Version 3
#-------------------------------------------------------

from cProfile import run
from curses import window
from posixpath import split
import subprocess
import time
from tkinter import Tk
from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from colorama import Fore, Back, Style
import psutil
import pwd
import os

#-------------------------------------------------------
# Basic stuff
#-------------------------------------------------------

def getUser():
    return pwd.getpwuid(os.getuid())[0]

def getWorkingDir():
    return os.getcwd()

# Get the System Uptime and convert it to seconds
def getUptimeInSeconds():
    uptime = psutil.boot_time()
    uptime = time.time() - uptime
    return uptime

#-------------------------------------------------------
# Main logic
#-------------------------------------------------------

def __main__():
    welcome()
    basicChecks()
    
    while True:
        menu = mainMenu()
        if menu[0] == "packages":
            packageMenu()
        elif menu[0] == "system":
            systemMenu()
        elif menu[0] == "exit":
            exit()

#-------------------------------------------------------
# Secondary logic
#-------------------------------------------------------

def welcome():
    print(Fore.GREEN + "Welcome to hMaintain!")
    print(Fore.GREEN + "This is a tool to help you maintain your system.")
    print(Fore.GREEN + "It will help you install packages, update them, and remove them.")
    print(Fore.GREEN + "It will also help you manage your system.")
    print(Fore.RED)
    print("Use this tool at your own risk. Read the source code before using it.")
    print(Fore.YELLOW)
    print("-------------------------------------------------------")
    print("©️ 2022 - Hannah Renners")
    print("Released under the GNU GENERAL PUBLIC LICENSE Version 3")
    print("-------------------------------------------------------" + Fore.RESET)

def basicChecks():
    # Print system uptime in days
    uptime = getUptimeInSeconds()
    uptime = uptime / 60 / 60 / 24
    uptime = round(uptime)
    print(Fore.GREEN + "System Uptime: " + str(uptime) + " days")
    print(Fore.RESET)

    # Print the current user
    print(Fore.GREEN + "Current User: " + getUser() + "\n" + Fore.RESET)

    # Say user should restart system if uptime is more than 5 days and if less than 5 days say user should restart system in x hours to 5 days
    if uptime > 5:
        print(Fore.RED + "Your system has been up for " + str(uptime) + " days. It is recommended that you restart your system.")
        print(Fore.RESET)
    else:
        print(Fore.GREEN + "Your system has been up for " + str(uptime) + " days. It is recommended that you restart your system in " + str(5 - uptime) + " days.")
        print(Fore.RESET)

    # Print the current working directory
    print(Fore.GREEN + "Current Working Directory: " + getWorkingDir())
    print(Fore.RESET)

    # Check if Yay is installed and print if it is installed
    # If it is not installed print a message to install yay and exit program
    if checkForYay():
        print(Fore.GREEN + "Yay is installed. Continuing...")
        print(Fore.RESET)
    else:
        print(Fore.RED + "Yay is not installed. Please install yay to use this tool.")
        print(Fore.YELLOW + "Do you want to install yay?")
        if prompt({"type": "confirm", "name": "install_yay", "message": "Yes or No? You can not continue without."}).get("install_yay"):
            installYay()
        else:
            print(Fore.RED + "You need yay to continue. Exiting...")
            exit()

def checkForYay():
    # Check if yay is installed
    if os.path.isfile("/usr/bin/yay"):
        return True
    else:
        return False

def installYay():
    # run install-yay.fish script in subprocess with fish
    subprocess.run(["fish", "install-yay.fish"])

#-------------------------------------------------------
# Secondary logic - Main Menu
#-------------------------------------------------------

def mainMenu():
    # Make a menu with InquirerPy
    main_menu = {
        "type": "list",
        "message": "What would you like to do?",
        "choices": [
            Choice("packages", "Mange Packages"),
            Choice("system", "Manage System"),
            Choice("exit", "Exit")
        ]
    }
    menu = prompt(main_menu)
    return menu

#-------------------------------------------------------
# Secondary logic - Package Menu
#-------------------------------------------------------

def packageMenu():
    # Make menu with InquirerPy
    package_menu = {
        "type": "list", "name": "package_menu", "message": "What would you like to do?", "choices": ['Install Custom', 'Install Class', 'Update', 'Remove', 'Manage', 'Back']
    }
    package_menu = prompt(package_menu)

    # If the user selects Install, run the install function
    if package_menu.get("package_menu") == "Install Custom":
        installCustomYayPackage()
    elif package_menu.get("package_menu") == "Install Class":
        installClassYayPackage()
    elif package_menu.get("package_menu") == "Update":
        updateYayPackages()
    elif package_menu.get("package_menu") == "Remove":
        removePackages()
    elif package_menu.get("package_menu") == "Manage":
        managePackages()

def installCustomYayPackage():
    # Make menu with InquirerPy where you can type in the package name
    package_list = {
        "type": "input",
        "name": "package_list",
        "message": "Type the name of the package you want to install."
    }
    package = prompt(package_list)

    # Install a package with yay
    cmd = 'yay -S ' + package.get("package_list")
    subprocess.run(cmd.split())

def installClassYayPackage():
    package_classes = [
        {
            "type": "list",
            "message": "Please select all package classes you want to install. Navigate with <Up> <Down> and (de-)select with <Space>. Confirm with <Enter>.",
            "choices": [
                Choice("basic", name="Basic: Essential utility's and library's", enabled=False),
                Choice("image", name="Image: Image editing, manipulation, and drawing tools", enabled=False),
                Choice("3d", name="3D: 3D rendering and creation", enabled=False),
                Choice("video", name="Video creation & playback software", enabled=False),
                Choice("code", name="Code: Coding tools and toolchains", enabled=False),
                Choice("office", name="Office: Office and Notetaking", enabled=False),
                Choice("utils", name="Util: Various utility software", enabled=False),
                Choice("gaming", name="Gaming: Launchers & gaming utility's", enabled=False)
            ],
            "multiselect": True,
            "transformer": lambda result: f"\nInstalling the following package classes:"
        }
    ]
    package_classes = prompt(package_classes)
    package_classes = package_classes.get("package_classes")

    # Same packe list as in hArch
    package_list = {
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
            "code": ['ptpython'],
            "office": ['notion-app-enhanced'],
            "utils": ['brave-bin'],
            "video": [''],
            "gaming": ['polymc-bin', 'steam', 'heroic-games-launcher-bin', 'mangohud']
        }
        }

    # Combine the package lists
    package_list = {**package_list["non-aur"], **package_list["aur"]}

    # Loop through the package classes and install the packages
    for package_class in package_classes:
        for package in package_list[package_class]:
            cmd = 'yay -S ' + package
            subprocess.run(cmd.split())

def updateYayPackages():
    # Update all packages with yay
    cmd = 'yay -Syu'
    subprocess.run(cmd.split())

def removePackages():
    # Make menu with InquirerPy where you can type in the package name
    package_list = {
        "type": "input",
        "name": "package_list",
        "message": "Type the name of the package you want to remove."
    }
    package = prompt(package_list)

    # Remove a package with yay
    cmd = 'yay -R ' + package.get("package_list")
    subprocess.run(cmd.split())

def managePackages():

     # Run command "pacman -Q" and get output
    cmd = 'pacman -Q'
    output = subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')

    # split the packages into a list
    all_packages = output.split("\n")

    # print the number of installed packages
    print(Fore.GREEN)
    print("\nThere are " + str(len(all_packages)) + " packages installed.")
    print(Style.RESET_ALL)

    # Make menu with InquirerPy where you can type in the package name
    package_list = {
        "type": "input",
        "name": "package_list",
        "message": "Type a name to get output of all package names that contain the name and are installed."
    }
    package = prompt(package_list)

    # run the loop to find the packages that match the name
    for x in all_packages:
        if package.get("package_list") in x:
            print(Style.NORMAL + Fore.YELLOW + "->" + Fore.CYAN + Style.DIM + x + Style.RESET_ALL)

#-------------------------------------------------------
# Secondary logic - System Menu
#-------------------------------------------------------

def systemMenu():
    # Make menu with InquirerPy
    system_menu = {
        "type": "list", "name": "system_menu", "message": "What would you like to do?", "choices": ['Restart', 'Shutdown', 'Back']
    }
    system_menu = prompt(system_menu)

    # If the user selects Restart, run the restart function
    if system_menu.get("system_menu") == "Restart":
        # restart system with subprocess
        subprocess.call(["systemctl", "reboot"])
    # If the user selects Shutdown, run the shutdown function
    elif system_menu.get("system_menu") == "Shutdown":
        # shutdown system with subprocess
        subprocess.call(["systemctl", "shutdown"])

#-------------------------------------------------------
# Calling main logic
#-------------------------------------------------------

__main__()