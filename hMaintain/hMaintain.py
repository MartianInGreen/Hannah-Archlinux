#-------------------------------------------------------
# ©️ 2022 - Hannah Renners
# Released under the GNU GENERAL PUBLIC LICENSE Version 3
#-------------------------------------------------------

from cProfile import run
from posixpath import split
import time
from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from colorama import Fore, Back, Style
import psutil
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
    updatePackages()
    updateAURPackages()
    uptimeCalc()

#-------------------------------------------------------
# Secondary logic
#-------------------------------------------------------

def welcome():
    print(Fore.RED)
    print("Welcome to hMaintain!")
    print("You are currently running as " + getUser())
    print("You are currently in " + getWorkingDir())
    print(Fore.GREEN)
    print("hMaintain - hMaintain.py")
    print("©️ 2022 - Hannah Renners")
    print("Released under the GNU GENERAL PUBLIC LICENSE Version 3")
    print(Fore.CYAN)
    print("This program is designed to help you maintain your system.")
    print(Fore.RED)
    print("You should run this program as root.")
    print("Please read the program code before using it!")
    print("You use the program at your own risk.")
    print(Style.RESET_ALL)

def updatePackages():
    print(Fore.RED)
    print("Updating packages...")
    print(Style.RESET_ALL)
    subprocess.call(["sudo", "pacman", "-Syu"])
    print(Fore.GREEN)
    print("Packages updated!")
    print(Style.RESET_ALL)

def updateAURPackages():
    print(Fore.RED)
    print("Updating AUR packages...")
    print(Style.RESET_ALL)
    subprocess.call(["sudo", "yay", "-Syu"])
    print(Fore.GREEN)
    print("AUR packages updated!")
    print(Style.RESET_ALL)

def uptimeCalc():
    uptime = getUptimeInSeconds()
    # Convert seconds to days
    uptime = uptime / 86400
    
    if uptime > 5:
        print(Fore.RED + Style.BRIGHT + "Your system has been up for " + str(uptime) + " days!\nYou should restart your System!" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Your system has been up for " + str(uptime) + " days!" + "\nYou should probably restart your system in " + str(5 - uptime) + " days!" + Style.RESET_ALL)

    # Sleep for 5 seconds
    time.sleep(5)

#-------------------------------------------------------
# Calling main logic
#-------------------------------------------------------

__main__()