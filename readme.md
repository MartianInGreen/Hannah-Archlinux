These are my personal setup & management & help scripts and programs for Arch Linux (https://archlinux.org/)

# hArch-v2
hArch is my personal Arch post-install script. It helps installing common programs I use and to set up my system.

To use the script you need to have installed Arch. You should probably also have installed a desktop envioerment.
You can do all those things with the 'Archinstall' command during the arch install.

Here is a basic guid (Full docs at https://github.com/archlinux/archinstall)
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
```
git clone https://github.com/MartianInGreen/Hannah-Archlinux
```
- Run the hArch/run.sh script
```
chmod +x hArch/run.sh script && .hArch/run.sh script
```

# hMaintain
A pretty self expanitory utility to help you manage your Arch install post install.