from InquirerPy import prompt, inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from colorama import Fore, Back, Style

import psutil

import os, pwd, time, subprocess

#---------------------------------------------------
# Main
#---------------------------------------------------

def main():
    checkForSudo()
    checkForYay()
    installClass()
    installExtra()
    installName()
    print(Fore.GREEN + "All packages installed!" + Style.RESET_ALL)
    exit()

#---------------------------------------------------
# Checks
#---------------------------------------------------

def checkForSudo():
    # Check if the python script was run as sudo
    if os.geteuid() != 0:
        print(Fore.GREEN + "This program was not run as sudo - as it should. Continuing..." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Please do NOT run this program as sudo! This program will not work if you do!" + Style.RESET_ALL)
        exit()

def checkForYay():
    # Check if yay is installed
    try:
        subprocess.check_output(["yay", "-h"])
    except:
        print(Fore.RED + "yay is not installed. Please install yay before using this program." + Style.RESET_ALL)
        installYay()

def getUser():
    return pwd.getpwuid(os.getuid())[0]

def getWorkingDir():
    return os.getcwd()

#---------------------------------------------------
# Installers
#---------------------------------------------------

def installYay():
    # Print a message that you should know how to manually install AUR packages before installing Yay
    print(Fore.RED + "You should know how to manually install AUR packages before installing Yay." + Style.RESET_ALL)
    print(Fore.RED + "If you don't know how to do that, please refer to the Arch wiki and only continue once you know how to do so!" + Style.RESET_ALL)
    print(Fore.RED + "Always make sure the AUR packages you are installing come from a trusted source or review them yourself before installing them!" + Style.RESET_ALL)
    print(Fore.RED + "Neither me nor the AUR team can be held responsible for any damage that may occur to your system!" + Style.RESET_ALL)

    # Sleep for 2 seconds
    time.sleep(2)

    # Make a menu to confirm yay
    yay_menu = {
        "type": "confirm",
        "message": "Do you want to install yay? You need yay to continue! (yay is a package manager for the AUR)",
        "name": "yay"
    }
    yay_menu = prompt(yay_menu)
    
    # If yay is confirmed, install yay
    if not yay_menu.get("yay"):
        print(Fore.RED + "You did not confirm yay. Exiting..." + Style.RESET_ALL)
        exit()

    print(Fore.RED + "Installing yay..." + Style.RESET_ALL)

    cmd_1 = 'set init_dir ' + getWorkingDir()
    cmd_2 = 'cd /opt'
    cmd_3 = 'sudo git clone https://aur.archlinux.org/yay-git.git'
    cmd_4 = 'sudo chown -R $USER:$USER ./yay-git'
    cmd_5 = 'cd yay-git'
    cmd_6 = 'makepkg -si'
    
    cmd = cmd_1 + ' && ' + cmd_2 + ' && ' + cmd_3 + ' && ' + cmd_4 + ' && ' + cmd_5 + ' && ' + cmd_6

    print(Fore.RED + "The yay Git repo will be cloned and then installed. This may take a while..." + Style.RESET_ALL)

    time.sleep(2)

    # Run the commands
    subprocess.run(cmd.split())

def installName():
    print(Fore.RED + "Installing packages by name..." + Style.RESET_ALL)

    # Make menu with InquirerPy where you can type in the package name
    package_list = {
        "type": "input",
        "name": "package_list",
        "message": "Type the name of the packages you want to install. Seperate them by a space. Confirm with <Enter>.",
    }
    package = prompt(package_list)

    # Install a package with yay
    cmd = 'yay -S ' + package.get("package_list")
    subprocess.run(cmd.split())

def installClass():
    print(Fore.RED + "Installing packages by class..." + Style.RESET_ALL)
    
    package_classes = [
        {
            "type": "list",
            "message": "Please select all package classes you want to install. Navigate with <Up> <Down> and (de-)select with <Space>. Confirm with <Enter>.",
            "name": "package_classes",
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

    # print the package classes
    print(Fore.RED + "Installing the following package classes: " + Fore.GREEN + str(package_classes) + Style.RESET_ALL)

    # Same packe list as in hMaintain.py
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
            "code": [''],
            "office": ['notion-app-enhanced'],
            "utils": ['brave-bin'],
            "video": [''],
            "gaming": ['polymc-bin', 'steam', 'heroic-games-launcher-bin', 'mangohud']
        }
        }

    # combine the packages in package_list non-aur and aur for each sub category
    package_list_combined = {}
    for category in package_list["non-aur"]:
        package_list_combined[category] = package_list["non-aur"][category] + package_list["aur"][category]
    
    # Install the packages
    for category in package_list_combined:
        if category in package_classes:
            for package in package_list_combined[category]:
                cmd = 'yay -S ' + package
                subprocess.run(cmd.split())


def installExtra():
    extraPackages = [
        {
            "type": "list",
            "message": "Please select all extra packages you want to install. Navigate with <Up> <Down> and (de-)select with <Space>. Confirm with <Enter>.",
            "name": "extra_packages",
            "multiselect": True,
            "choices": [
                Choice("spotify", enabled=False),
                Choice("whatsapp-nativefier", enabled=False),
                Separator(),
                Choice("Firefox", enabled=False),
                Choice("chromium-bin", enabled=False),
                Separator(),
                Choice("vlc", enabled=False),
                Separator(),
                Choice("visual-studio-code-bin", enabled=False),
                Choice("neovim", enabled=False),
                Choice("emacs", enabled=False),
                Choice("sublime-text-bin", enabled=False),
                Choice("atom", enabled=False),
                Separator(),
                Choice("python-pip", enabled=False),
                Choice("python-virtualenv", enabled=False),
                Choice("python-tk", enabled=False),
                Separator(),
                Choice("zhs", enabled=False),
                Choice("ptpython", enabled=False),
            ]
        }
    ]
    extraPackages = prompt(extraPackages)
    
    # Install extra Packages with yay
    cmd = 'yay -S ' + ' '.join(extraPackages.get("extraPackages"))
    subprocess.run(cmd.split())

main()