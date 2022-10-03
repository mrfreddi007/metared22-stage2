#!/usr/bin/env python3
import pandas as pd
import string

a = 875126856
b = 741258756
x = 534542575

workbook = pd.read_excel("grades.xlsm", header=None )

all = []

for j in range(1,100):
    temp = []
    for i in range(42):
        try:
            temp.append(chr(workbook[i][9] ^ x))
        except:
            pass
    if len(temp) > 1:
        all.append(temp)
    x = (a*b*x) % (2**32)
print(all[0])