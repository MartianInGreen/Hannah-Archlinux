import os, subprocess

def setup():
    # check if git is installed
    if not os.path.exists("/usr/bin/git"):
        # install git
        print("Git not installed! Installing git...")
        cmd = 'sudo pacman -S git'
        subprocess.run(cmd.split())

    # check if pip is installed with pacman
    if not os.path.exists("/usr/bin/pip"):
        # install pip
        print("Pip not installed! Installing pip...")
        cmd = 'sudo pacman -S python-pip'
        subprocess.run(cmd.split())

    # install inquirerPy with pip
    cmd = 'sudo pip install inquirerPy'
    subprocess.run(cmd.split())
    
    # install colorama with pip
    cmd = 'sudo pip install colorama'
    subprocess.run(cmd.split())

    # install psutil with pip
    cmd = 'sudo pip install psutil'
    subprocess.run(cmd.split())

    print("Setup complete!")

setup()