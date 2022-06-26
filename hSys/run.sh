#/bin/bash

printf "\n\n\n\n"
echo "-----------------------------------------------------------------------------------------------"
echo "MartianInGreen's Linux Scripts"
echo "Copyright (C) 2022 by Hannah Renners"
echo "Licenced under the ---> GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 <---"
echo "For more info read the LICENSE file"
echo "You run this program at your own risk!"
echo "-----------------------------------------------------------------------------------------------"
printf "\n\n\n\n"

sleep 5

echo "Installing dependencys!"

sudo pacman -Syu git python python-pip
pip install InquirerPy

python3 hSys.py