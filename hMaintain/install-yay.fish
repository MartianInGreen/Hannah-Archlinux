set init_dir $PWD
cd /opt

echo "Cloning git"

sudo git clone https://aur.archlinux.org/yay-git.git 

echo "Making package"

sudo chown -R $USER:$USER ./yay-git
cd yay-git
makepkg -si

cd $init_dir