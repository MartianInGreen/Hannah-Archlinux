#-------------------------------------------------------
# ©️ 2022 - Hannah Renners
# Released under the GNU GENERAL PUBLIC LICENSE Version 3
# hSys - v0.0.1
#-------------------------------------------------------

#-------------------------------------------------------
# Boot Logic
#-------------------------------------------------------

def boot():
    print("\n\n\n\n")
    print( "-----------------------------------------------------------------------------------------------" )
    print( "MartianInGreen's Linux Scripts" )
    print( "Copyright (C) 2022 by Hannah Renners" )
    print( "Licenced under the ---> GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 <---" )
    print( "For more info read the LICENSE file" ) 
    print( "You run this program at your own risk!" )
    print( "-----------------------------------------------------------------------------------------------" )
    print("\n\n\n\n")

    time.sleep(5)

    # check if git is installed
    if not os.path.exists("/usr/bin/git"):
        # install git
        print(Fore.RED + "Git not installed! Installing git...")
        cmd = 'sudo pacman -S git'
        subprocess.run(cmd.split())

    # check if pip is installed with pacman
    if not os.path.exists("/usr/bin/pip"):
        # install pip
        print(Fore.RED + "Pip not installed! Installing pip...")
        cmd = 'sudo pacman -S python-pip'
        subprocess.run(cmd.split())
    
    # automatically install inquirer if not installed
    cmd = 'pip install InquirerPy'
    subprocess.run(cmd.split())

boot()

#-------------------------------------------------------
# Imports
#-------------------------------------------------------

from colorama import Fore, Back, Style

from InquirerPy import prompt, inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

import sys, os, subprocess, time, pwd, psutil

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
# Main Logic
#-------------------------------------------------------

def __main__():
    welcome()
    basicChecks()

    # Check if the python script was run as sudo
    checkForSudo()
    checkForYay()

    while True:
        mainMenu = mainMenu()

        if mainMenu.choice == "Setup":
            setupMenu = setupMenu()

            # implement all the choices
            if setupMenu.choice == "all":
                installClass()
                installExtra()
                installName()
                fishAlias()
                pacmanConfig()
                setupGit()
                createFolders()
            elif setupMenu.choice == "install_class":
                installClass()
            elif setupMenu.choice == "install_extra":
                installExtra()
            elif setupMenu.choice == "install_name":
                installName()
            elif setupMenu.choice == "setup_fish":
                fishAlias()
            elif setupMenu.choice == "setup_pacman":
                pacmanConfig()
            elif setupMenu.choice == "setup_git":
                setupGit()
            elif setupMenu.choice == "setup_foders":
                createFolders()
            elif setupMenu.choice == "Exit":
                pass

        elif mainMenu.choice == "Manage":
            manageMenu = manageMenu()

            # implement all the choices
            if manageMenu.choice == "install_class":
                installClass()
            elif manageMenu.choice == "install_extra":
                installExtra()
            elif manageMenu.choice == "install_name":
                installName()
            elif manageMenu.choice == "update":
                updateYayPackages()
            elif manageMenu.choice == "upgrade":
                upgrade()
            elif manageMenu.choice == "remove":
                removePackages()
            elif manageMenu.choice == "search":
                managePackages()
            elif manageMenu.choice == "redo_setup_git":
                setupGit()
            elif manageMenu.choice == "Exit":
                pass

        elif mainMenu.choice == "Exit":
            goodbye()
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)

#-------------------------------------------------------
# Secondary Logic
#-------------------------------------------------------

def welcome():
    print(Fore.RED + "Welcome to hSys!")
    print(Fore.GREEN + "hSys is a TUI tool to help you setup and manage your Arch installation.")
    print(Fore.YELLOW + "This program is not affiliated with or endorsed by Arch Linux.")
    print(Fore.YELLOW + "Please review the source code before using this program!" + Style.RESET_ALL)
    print(Fore.RED + "This program is not guaranteed to work or be bug free! And is only meant to be used if you know how to do all of this mannually as well!" + Style.RESET_ALL)

def mainMenu():
    # Make main menu with inquirer
    mainMenu = {
        "type": "select",
        "message": "What would you like to do?",
        "name": "main",
        "choices": [
            Separator("Main Menu"),
            Choice("Setup", "Setup your system"),
            Choice("Manage", "Manage your system"),
            Choice("Exit", "Exit hSys"),
            Separator("Main Menu"),
        ]
    }
    mainMenu = prompt(mainMenu)

    return mainMenu

def setupMenu():
    # Make setup menu with inquirer
    setupMenu = {
        "type": "select",
        "message": "What would you like to do?",
        "name": "setup",
        "choices": [
            Separator("Setup Menu"),
            Choice("install_class", "Install packages by package class"),
            Choice("install_extra", "Install extra packages"),
            Choice("install_name", "Install packages by name"),
            Choice("setup_fish", "Setup fish aliases"),
            Choice("setup_pacman", "Setup pacman"),
            Choice("setup_git", "Setup git with ssh & gpg keys"),
            Choice("setup_foders", "Setup folders in /home/<user>"),
            Choice("All", "Run the setup for all of the above"),
            Choice("Exit", "Exit to main menu"),
            Separator("Setup Menu"),
        ]
    }
    setupMenu = prompt(setupMenu)

    return setupMenu

def manageMenu():
    # Make manage menu with inquirer
    manageMenu = {
        "type": "select",
        "message": "What would you like to do?",
        "name": "manage",
        "choices": [
            Separator("Manage Menu"),
            Choice("install_class", "Install packages by package class"),
            Choice("install_extra", "Install extra packages"),
            Choice("install_name", "Install packages by name"),
            Choice("update", "Update your system"),
            Choice("upgrade", "Update your Arch-Linux mirrors system"),
            Choice("remove", "Remove packages"),
            Choice("search", "Search for installed packages"),
            Choice("redo_setup_git", "Redo git setup"),
            Choice("Exit", "Exit to main menu"),
            Separator("Manage Menu"),
        ]
    }
    manageMenu = prompt(manageMenu)

    return manageMenu

def checkForSudo():
    # Check if the python script was run as sudo
    if os.geteuid() != 0:
        print(Fore.RED + "This program needs to be run as sudo. Exiting..." + Style.RESET_ALL)
        exit()
    else:
        print(Fore.GREEN + "This program was run as sudo. Continuing..." + Style.RESET_ALL)

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

def checkForYay():
    # Check if yay is installed
    try:
        subprocess.check_output(["yay", "-h"])
    except:
        print(Fore.RED + "yay is not installed. Please install yay before using this program." + Style.RESET_ALL)
        installYay()

def goodbye():
    print(Fore.RED + "All done now!" + Style.RESET_ALL)
    print(Fore.RED + "If you have changed a lot of things I would recommend you reboot your system!" + Style.RESET_ALL)

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
        print(Fore.RED + "Exiting... GOOD BYE!" + Style.RESET_ALL)
        exit()

#-------------------------------------------------------
# Install Logic
#-------------------------------------------------------

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
    cmd = 'fish install-yay.fish'
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
# Configuration Logic
#-------------------------------------------------------

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

def createFolders():
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

def setupGit():
    print(Fore.RED + "Setting up Git..." + Style.RESET_ALL)
    
    def sshKey():
        # Make menu to ask if ssh key should be created
        create_ssh_key = {
            "type": "confirm",
            "name": "create_ssh_key",
            "message": "Do you want to create an ssh key?",
        }
        create_ssh_key = prompt(create_ssh_key)
        create_ssh_key = create_ssh_key.get("create_ssh_key")

        if create_ssh_key:
            # Create an ssh key
            cmd = 'ssh-keygen -t rsa -b 4096'
            subprocess.run(cmd.split())

        # Get the ssh key
        cmd = 'cat ~/.ssh/id_rsa.pub'
        ssh_key = subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')

        # Write ssh_key to a file in the home directory with the name 'ssh_key.txt'
        ssh_key_file = open('ssh_key.txt', 'w')
        ssh_key_file.write(ssh_key)
        ssh_key_file.close()
    sshKey()

    def gpgKey():
        # Make menu to ask if gpg key should be created
        create_gpg_key = {
            "type": "confirm",
            "name": "create_gpg_key",
            "message": "Do you want to create a gpg key?",
        }
        create_gpg_key = prompt(create_gpg_key)
        create_gpg_key = create_gpg_key.get("create_gpg_key")

        if create_gpg_key:
            # Create a gpg key
            cmd = 'gpg --default-new-key-algo rsa4096 --gen-key'
            subprocess.run(cmd.split())

        # Get the gpg key
        cmd = 'cat ~/.gnupg/pubring.gpg'
        gpg_key = subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')

        # get the public key from the gpg key
        gpg_key = gpg_key.split('\n')
        gpg_key = gpg_key[1]

        # Write gpg_key to a file in the home directory with the name 'gpg_key.txt'
        gpg_key_file = open('gpg_key.txt', 'w')
        gpg_key_file.write(gpg_key)
        gpg_key_file.close()
    gpgKey()

    def gitConfig():
        # Make a menu to ask if git config should be configured
        configure_git_config = {
            "type": "confirm",
            "name": "configure_git_config",
            "message": "Do you want to configure git config?",
        }
        configure_git_config = prompt(configure_git_config)
        configure_git_config = configure_git_config.get("configure_git_config")

        if configure_git_config:
            # Get the gpg key
            cmd = 'cat ~/.gnupg/pubring.gpg'
            gpg_key = subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')

            # Add gpg_key to the git config file
            cmd = 'git config --global user.signingkey ' + gpg_key
            subprocess.run(cmd.split())

            # Set gpgsign to true in the git config file
            cmd = 'git config --global commit.gpgsign true'
            subprocess.run(cmd.split())
    gitConfig()

    print(Fore.YELLOW + "Please remember to mannually add the keys to your GitHub/GitLab account!" + Style.RESET_ALL)
    print(Fore.GREEN + "Git setup complete!" + Style.RESET_ALL)

#-------------------------------------------------------
# Management logic
#-------------------------------------------------------

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

def upgrade():
    pass

#-------------------------------------------------------
# Execute Main
#-------------------------------------------------------

__main__()