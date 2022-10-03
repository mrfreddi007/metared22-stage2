#!/usr/bin/env python

enc = "CT0N_2TR2_T4F411HFUNT243A21NT}{P0T_"

i = 0
j = 6
k = 12
l = 18
m = 24
n = 30

flag = ""

while "}" not in flag:
    flag += enc[i]
    flag += enc[j]
    flag += enc[k]
    flag += enc[l]
    flag += enc[m]
    flag += enc[n]
    i+=1
    j+=1
    k+=1
    l+=1
    m+=1
    n+=1

print(flag)