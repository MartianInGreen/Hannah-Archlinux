import subprocess

def update():
    cmd = 'sudo python updateArchMirrors.py'
    subprocess.run(cmd.split())

    cmd = 'sudo pacman -Syyu'
    subprocess.run(cmd.split())

    cmd = 'yay'
    subprocess.run(cmd.split())

update()