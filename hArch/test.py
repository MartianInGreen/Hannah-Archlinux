import subprocess

print("Installing packages now!\nBeginning with non AUR packages.")

pack_nonAUR = ['man-db', 'neofetch']
pack_AUR = ""
installAUR = False

string_pack_nonAUR = ""
strin_pack_AUR = ""

# Seperating packages into strings
for x in pack_nonAUR:
    string_pack_nonAUR = string_pack_nonAUR + x + " " 
if installAUR == True:
    for x in pack_AUR:
        string_pack_AUR = string_pack_AUR + " " + x

cmd = 'sudo pacman -Syu ' + string_pack_nonAUR 
subprocess.run(cmd.split())