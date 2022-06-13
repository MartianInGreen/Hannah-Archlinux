set init_dir $PWD
set user $USER
set packages_init "krita xournalpp neofetch blender man-db libqalculate libreoffice-fresh inkscape gimp darktable rustup python nextcloud-client qalculate-gtk guake alacritty discord gpick code git fish pcmanfm jre-openjdk yakuake "
set aur_packages_init "brave-bin polymc-bin notion-app-enhanced steam heroic-games-launcher-bin spotify whatsapp-nativefier "

#-----------------------------------------------------------------------------------------------
# User configuration
#-----------------------------------------------------------------------------------------------

echo "You're user $USER. The following instalation requieres SUDO priviliges!"

# Telling the user what will be installed!
echo "The following packages will be installed:"
echo "non-AUR (via pacman): $packages_init"
echo "AUR (via yay): $aur_packages_init"

# Asking user for packages
echo "Do you want to install more (non AUR) packages? [If not just press enter - Seperate by space]"
read non_aur_input
set -a packages $packages_init $non_aur_input

echo "Do you want to install more (AUR) packages? [If not just press enter - Seperate by space]"
read aur_input
set -a aur_packages $aur_packages_init $aur_input

#-----------------------------------------------------------------------------------------------
# Installing Yay
#-----------------------------------------------------------------------------------------------

cd /opt
sudo git clone https://aur.archlinux.org/yay-git.git 

sudo chown -R $user:$user ./yay-git
cd yay-git
makepkg -si

cd $init_dir

#-----------------------------------------------------------------------------------------------
# Installing packages
#-----------------------------------------------------------------------------------------------

sudo pacman -S $packages
yay -S $aur_packages

#-----------------------------------------------------------------------------------------------
# Making & copying configs
#-----------------------------------------------------------------------------------------------

# Creating Custom Fish configs
printf "if status is-interactive\n neofetch\n end"

alias -s nf="cd && fish"
alias -s please="sudo"
alias -s q="qalc"
alias -s wa="brave --homepage https://www.wolframalpha.com/"
alias -s pm="sudo pacman -Syu"
alias -s start_qemu="sudo systemctl start libvirtd.service"

#-----------------------------------------------------------------------------------------------
# Changin Shell
#-----------------------------------------------------------------------------------------------

chsh -s /bin/fish $user

#-----------------------------------------------------------------------------------------------
# Finishing up & cleaning
#-----------------------------------------------------------------------------------------------

echo "All done! Do you want to reboot now? [Type y/n]"
read reboot_question
if [ "$reboot_question" = "y"]
    echo "Rebooting in 10 seconds"
    sleep 10
    reboot
else if [ "$reboot_question" = "n"]
    echo "Not rebooting. Goody bye :>"
else
    echo "Please type y/n. Do you want to reboot?"
end
