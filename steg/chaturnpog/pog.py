#!/usr/bin/env python3
from PIL import Image

img = Image.open("POG.jpg")

baits = []

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if x > (img.size[0] - 4) or y > (img.size[1] - 5):
            baits.append(sum(img.getpixel((x,y))))
        
print(baits)
print(img.size)