These are my personal setup & management & help scripts and programs for Arch Linux (https://archlinux.org/)

# Management scripts

## Clone && basic
- Run the 'Archinstall' command to install Arch
- Select your Language, Mirror region, Keyboard layout
- Create at least one user that has Sudo priviliges
- Select Bootloader
- Partition drive
- Select "Desktop" from the Profile section
- Select DE & Audio pipline & Network Manager
- Under additional repos select "multilib" (if you want to use 32bit programs. Also requiered by a looooot of games & steam)
- Wait for Arch to finish installing
- Git clone this repo
´´´
git@github.com:MartianInGreen/Hannah-Archlinux.git
´´´
- run the script in the following order if you want them

## 'setup.py'
Installs all required packages and python modules for the rest of the scripts.

## 'packages.py'
Install packages by class, extra, and name.

## 'misc.py'
Setup folders, fish, and other miscellaneous stuff.

## 'update.py' & 'updateArchMirrors.py'
Updates the System and updates the Arch Linux mirrors by region.