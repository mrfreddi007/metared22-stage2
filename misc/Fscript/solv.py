#!/usr/bin/env python
with open("whack.uh","r") as f:
    js = f.read()
    
chars = ""
for i in js:
    if i == "[":
        chars += "+"
    elif i == "]":
        chars += "!"
    elif i == "[":
        chars += i
    elif i == ")":
        chars += i
    elif i == "!":
        chars += i
    elif i == "+":
        chars += i    
        
print(chars)
flag = "CTFUA{WH4T_TH3_baNaNa_W42_TH4T}"
print(flag)