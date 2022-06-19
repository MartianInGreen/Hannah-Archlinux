#/bin/dash

#-----------------------------------------------------------------------------------------------
# DISCLAIMER
#-----------------------------------------------------------------------------------------------

printf "\n\n\n\n"
echo "-----------------------------------------------------------------------------------------------"
echo "MartianInGreen's Linux Scripts"
echo "Copyright (C) 2022 by Hannah Renners"
echo "Licenced under the ---> GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 <---"
echo "For more info read the LICENSE file"
echo "-----------------------------------------------------------------------------------------------"
printf "\n\n\n\n"

sleep 5

#Installing fish
echo 'Installing fish'

sudo pacman -Syu fish

fish s1.fish