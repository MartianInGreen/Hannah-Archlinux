from posixpath import split
from InquirerPy import prompt, inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from colorama import Fore, Back, Style

import subprocess

#---------------------------------------------------
# Main
#---------------------------------------------------

print(Fore.GREEN + "Small network configuration helper for Arch Linux & iwctl" + Style.RESET_ALL)

#
# List devices and ask user to select one
#

cmd_list = 'iwctl device list'

# run command
subprocess.run(cmd_list.split())

# Make menu to input device name
device_list = {
    "name": "device",
    "type": "input",  
    "message": "Enter the divice name:"
    }
device_list = prompt(device_list)

#
# List networks and ask user to select one
#

print(device_list.get('device'))

cmd_scan = 'iwctl station ' + device_list.get('device') + ' scan' 
subprocess.run(cmd_scan.split())
cmd_networks = 'iwctl station ' + device_list.get('device') + ' get-networks'
subprocess.run(cmd_networks.split())

network_list = {
    "name": "network",
    "type": "input",
    "message": "Enter the network name:"
    }
network_list = prompt(network_list)

#
# Connect to network
#

print(network_list.get('network'))

cmd_connect = 'iwctl station ' + device_list.get('device') + ' connect '

subprocess.run(cmd_connect.split() + [f"{network_list.get('network')}"])