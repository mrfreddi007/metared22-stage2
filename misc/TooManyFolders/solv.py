#!/usr/bin/env python3
import os
import sys
import glob

dirs = []

for file in glob.iglob("./**/**", recursive=True):
    dirs.append(file)
    
for dir in dirs:
    try:
        with open(dir+".keep","r") as f:
            print(f.read()) 
    except:
        pass