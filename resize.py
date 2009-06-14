import Image
import os, sys

width = 800
height = 600

for root, dirs, files in os.walk('/home/nate/'):
    for name in files:
        filename = os.path.join(root, name)
        if filename.endswith('.jpg'):
           print filename
           imin = Image.open(filename)
           imout = imin.resize((width, height), Image.bicubic)
           imout.save(filename)
