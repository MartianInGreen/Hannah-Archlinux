import os

# open '/tmp/mirrorlist'
file = open('/tmp/mirrorlist', 'r')
text = file.read()
file.close()

# write text to '/etc/pacman.d/mirrorlist'
file = open('/etc/pacman.d/mirrorlist', 'w')
file.write(text)
file.close()

# remove '/tmp/mirrorlist'
os.remove('/tmp/mirrorlist')
