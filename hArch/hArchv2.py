#-------------------------------------------------------
# ©️ 2022 - Hannah Renners
# Released under the GNU GENERAL PUBLIC LICENSE Version 3
# hArch v2.0
#-------------------------------------------------------

from time import sleep
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
    checkForSudo()
    main_menu = mainMenu()

    installYay()
    configs()

    if main_menu == "install_class":
        installClass()
        installExtra()
    elif main_menu == "install_name":
        installName()
    elif main_menu == "configs":
        configs()
    elif main_menu == "setup":
        setup()
    elif main_menu == "exit":
        goodbye()

#-------------------------------------------------------
# Secondary logic
#-------------------------------------------------------

def welcome():
    print(Fore.RED + "Welcome to hArch v2.0!")
    print(Fore.GREEN + "Starting execution of the Python program...")
    print(Fore.GREEN + "This program will help you set up your Arch installation." + Style.RESET_ALL)
    print(Fore.YELLOW + "This program is not affiliated with or endorsed by Arch Linux.")
    print(Fore.YELLOW + "Please review the source code before using this program!" + Style.RESET_ALL)
    print(Fore.RED + "This program is not guaranteed to work or be bug free! And is only meant to be used if you know how to do all of this mannually as well!" + Style.RESET_ALL)

def mainMenu():
    # make a main menu with InquirerPy
    main_menu = {
        "type": "list",
        "message": "What would you like to do?",
        "choices": [
            Choice("install_class", "Install packages by category/class"),
            Choice("install_name", "Install packages by name"),
            Choice("configs", "Configue programs & configs"),
            Choice("setup", "Create Folders & Setting up Git key & etc."),
            Choice("exit", "Exit")
        ]
    }
    out = prompt(main_menu)
    out = out[0]
    return out

def checkForSudo():
    # Check if the python script was run as sudo
    if os.geteuid() != 0:
        print(Fore.RED + "This program needs to be run as sudo. Exiting..." + Style.RESET_ALL)
        exit()
    else:
        print(Fore.GREEN + "This program was run as sudo. Continuing..." + Style.RESET_ALL)

def installYay():
    # Print a message that you should know how to manually install AUR packages before installing Yay
    print(Fore.RED + "You should know how to manually install AUR packages before installing Yay." + Style.RESET_ALL)
    print(Fore.RED + "If you don't know how to do that, please refer to the Arch wiki and only continue once you know how to do so!" + Style.RESET_ALL)
    print(Fore.RED + "Always make sure the AUR packages you are installing come from a trusted source or review them yourself before installing them!" + Style.RESET_ALL)
    print(Fore.RED + "Neither me nor the AUR team can be held responsible for any damage that may occur to your system!" + Style.RESET_ALL)

    # Sleep for 2 seconds
    sleep(2)

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
    cmd = 'fish install-yay.fish'
    subprocess.run(cmd.split())

def goodbye():
    print(Fore.GREEN + "All done now! I would recomend you to reboot now." + Style.RESET_ALL)
    print(Fore.GREEN + "Hope to see you after you next installation!" + Style.RESET_ALL)
    print(Fore.RED + "Goodbye!" + Style.RESET_ALL)

    # Make menu to ask if you want to reboot
    reboot_menu = {
        "type": "confirm",
        "message": "Do you want to reboot now?",
        "name": "reboot"
    }
    reboot_menu = prompt(reboot_menu)

    # If reboot is confirmed, reboot
    if reboot_menu.get("reboot"):
        cmd = 'reboot'
        subprocess.run(cmd.split())
    else:
        print(Fore.RED + "Exiting..." + Style.RESET_ALL)
        exit()

#-------------------------------------------------------
# Secondary logic - install by class
#-------------------------------------------------------

def installClass():
    print(Fore.RED + "Installing packages by class..." + Style.RESET_ALL)
    
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

def installExtra():
    extraPackages = [
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
            ]
        }
    ]
    extraPackages = prompt(extraPackages)
    
    # Install extra Packages with yay
    cmd = 'yay -S ' + ' '.join(extraPackages.get("extraPackages"))
    subprocess.run(cmd.split())

#-------------------------------------------------------
# Secondary logic - install by name
#-------------------------------------------------------

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

#-------------------------------------------------------
# Secondary logic - configs
#-------------------------------------------------------

def configs():
    print(Fore.RED + "Configuring programs & configs..." + Style.RESET_ALL)

    # Make fish alias's
    def fishAlias():
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

        cmd = 'fish -c \'alias -s p="clear && ptpython"\''
        subprocess.run(cmd.split())
    fishAlias()

    def pacmanConfig():
        # Get the pacman config file and write it to variable
        pacman_config = open('pacman.conf', 'w')
        pacman_config_read = pacman_config.read
        
        # Seperate to config file by line
        pacman_config_read = pacman_config_read.split('\n')

        # Add 'color' to the end of the config file in a new line
        pacman_config_read.append('Color')

        # Ask with menu how many parallel downloads you want
        parallel_downloads = {
            "type": "input",
            "name": "parallel_downloads",
            "message": "How many parallel downloads do you want? (1-10...)"
        }
        parallel_downloads = prompt(parallel_downloads)
        parallel_downloads = parallel_downloads.get("parallel_downloads")

        # Search for 'parallelDownloads' 
        for line in pacman_config_read:
            if 'parallelDownloads' in line:
                # Replace the line with the new one
                pacman_config_read[pacman_config_read.index(line)] = 'parallelDownloads = ' + parallel_downloads
        
        # Make list to string
        pacman_config_read = '\n'.join(pacman_config_read)

        # Make string to utf-8
        pacman_config_read = pacman_config_read.encode('utf-8')

        # Write the new config file overwriting the old one
        pacman_config.write(pacman_config_read)
        pacman_config.close()
    pacmanConfig()

#-------------------------------------------------------
# Secondary logic - setup
#-------------------------------------------------------

def setup():
    # Make menu to ask if directories should be created
    create_directories = {
        "type": "confirm",
        "name": "create_directories",
        "message": "Do you want to create directories?",
    }
    create_directories = prompt(create_directories)
    create_directories = create_directories.get("create_directories")

    if create_directories:
        # Create a new directory called 'Dev' in the home directory
        cmd = 'mkdir ~/Dev'
        subprocess.run(cmd.split())

        # Create a new directory called 'Working' in the home directory
        cmd = 'mkdir ~/Working'
        subprocess.run(cmd.split())

        # Create a new directory called 'Tools' in the home directory
        cmd = 'mkdir ~/Tools'
        subprocess.run(cmd.split())

        # Create a new directory called 'Creative' in the home directory
        cmd = 'mkdir ~/Creative'
        subprocess.run(cmd.split())
    
    # Make menu to ask if git should be configured
    configure_git = {
        "type": "confirm",
        "name": "configure_git",
        "message": "Do you want to configure git?",
    }
    configure_git = prompt(configure_git)
    configure_git = configure_git.get("configure_git")

    if configure_git:
        setupGit()
    else:
        print(Fore.RED + "Skipping git configuration..." + Style.RESET_ALL)

def setupGit():
    print(Fore.RED + "Setting up Git..." + Style.RESET_ALL)
    
    # Make menu to ask if ssh key should be created
    ssh_key = {
        "type": "confirm",
        "name": "ssh_key",
        "message": "Do you want to create a new SSH key?"
    }
    ssh_key = prompt(ssh_key)
    ssh_key = ssh_key.get("ssh_key")

    # Create a new SSH key if the user wants to
    if ssh_key:
        cmd = 'ssh-keygen -t rsa -b 4096'
        subprocess.run(cmd.split())
    
    # Get the PGP public key from the SSH key
    cmd = 'cat ~/.ssh/id_rsa.pub'
    public_key = subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')

    # Make menu to ask if the public key should be added to the Github account
    add_public_key = {
        "type": "confirm",
        "name": "add_public_key",
        "message": "Do you want to add the public key to your Github account?"
    }
    add_public_key = prompt(add_public_key)
    add_public_key = add_public_key.get("add_public_key")

    # Write the public key to the file 'ssh_key' in the home directory
    if add_public_key:
        cmd = 'echo ' + public_key + ' >> ~/.ssh/ssh_key'
        subprocess.run(cmd.split())
    
    # Make menu to ask if GPG key should be created
    gpg_key = {
        "type": "confirm",
        "name": "gpg_key",
        "message": "Do you want to create a new GPG key?"
    }
    gpg_key = prompt(gpg_key)
    gpg_key = gpg_key.get("gpg_key")

    # Create a new GPG key if the user wants to
    if gpg_key:
        cmd = 'gpg --default-new-key-algo rsa4096 --gen-key'
        subprocess.run(cmd.split())
    
    # Get the GPG public key from the GPG key
    cmd = 'cat ~/.gnupg/pubring.gpg | grep "^pub" | cut -d " " -f 2'
    public_key = subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')

    # Write the public key to the file 'gpg_key' in the home directory
    cmd = 'echo ' + public_key + ' >> ~/.ssh/gpg_key'
    subprocess.run(cmd.split())

    # Add gpg_key to the git config file
    cmd = 'git config --global user.signingkey ' + public_key
    subprocess.run(cmd.split())

    # Set gpgsign to true in the git config file
    cmd = 'git config --global commit.gpgsign true'
    subprocess.run(cmd.split())

#-------------------------------------------------------
# exectue Main logic
#-------------------------------------------------------

__main__()