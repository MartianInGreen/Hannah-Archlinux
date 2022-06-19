set init_dir $PWD
set i_yay "true"

#-----------------------------------------------------------------------------------------------
# Package lists
#-----------------------------------------------------------------------------------------------

# Non AUR
set p_basic = "man-db neofetch alacritty git fish yakuake libqalculate"
set p_image = "krita gimp darktable inkscape"
set p_3d = "blender"
set p_code = "code python rustup cmake"
set p_office ="xournalpp libreoffice-fresh"
set p_util = "nextcloud-client qalculate-gtk"

# AUR
set pa_office = "notion-app-enhanced"
set pa_game = "polymc-bin steam heroic-games-launcher-bin"
set pa_util = "spotify brave-bin"

#-----------------------------------------------------------------------------------------------
# User configuration
#-----------------------------------------------------------------------------------------------

echo "You're user $USER. The following instalation requieres SUDO priviliges!"

# Aksing if yay should be installed
function q_installYay
    echo "You can only install AUR packages via this program if you install yay."
    echo "Do you want to install yay to make installing AUR packages easier? [Type y/n]"
    read installYay

    switch $installYay
        case 'y'
            echo "Yay will be installed!"
            set i_yay "true"
        case 'n'
            echo "Yay will NOT be installed!"
            set i_yay "false"
        case '*'
            echo "Please type y/n."
            q_installYay
    end
end
q_installYay

# Asking which packages should be installed
echo "Chose which of the following non-AUR packages will be installed"
echo "ID-1 Basic: $p_basic"
echo "ID-2 Image: $p_image"
echo "ID-3 3d: $p_3d"
echo "ID-4 code: $p_code"
echo "ID-5 office: $p_office"
echo "ID-6 Util: $p_util"
echo "Type all wanted ID's sperated by a space like so: '1 2 3 4 5 6'. If you do not want to install any packages just press enter."
read q_nonAURinput
set packages_IdNonAUR ""

set q_nonAURinput_idList (string split ' ' $q_nonAURinput)
for i in $q_nonAURinput_idList