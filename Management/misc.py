from InquirerPy import prompt, inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from colorama import Fore, Back, Style

import psutil

import os, pwd, time, subprocess

def main():

    # ask if fish aliases should be added
    fish_alias = {
        "type": "confirm",
        "message": "Would you like to add fish aliases?",
        "name": "fish_alias",
        "default": True,
    }
    fish_alias = prompt(fish_alias)

    # ask if pacman should be setup
    pacman = {
        "type": "confirm",
        "message": "Would you like to setup pacman?",
        "name": "pacman",
        "default": True,
    }
    pacman = prompt(pacman)

    # ask if git should be setup
    git = {
        "type": "confirm",
        "message": "Would you like to setup git? (Probalby not working)",
        "name": "git",
        "default": True,
    }
    git = prompt(git)

    # ask if folders should be setup
    folders = {
        "type": "confirm",
        "message": "Would you like to setup folders?",
        "name": "folders",
        "default": True,
    }
    folders = prompt(folders)

    # for each option, run the function
    if fish_alias.get("fish_alias"):
        print(Fore.GREEN + "Adding fish aliases..." + Style.RESET_ALL)
        fishAlias()
    if pacman.get("pacman"):
        print(Fore.GREEN + "Setting up pacman..." + Style.RESET_ALL)
        pacmanConfig()
    if git.get("git"):
        print(Fore.GREEN + "Setting up git..." + Style.RESET_ALL)
        setupGit()
    if folders.get("folders"):
        print(Fore.GREEN + "Setting up folders..." + Style.RESET_ALL)
        createFolders()


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

    cmd = 'mkdir ~/School'
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

main()