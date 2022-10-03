#!/usr/bin/env python3
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

with open("serial_1","rb") as f:
    a = f.readline()
    key = b"\xff"*len(a)

b = byte_xor(a,key)


byt = []

for i in range(0,len(b),9):
    if b[i] == 1:
        byt.append("1")
    else:
        byt.append("0")
with open("s1","w") as f:
    f.write("".join(byt))


with open("serial_2","rb") as f:
    c = f.readline()
    key2 = b"\xb7"*len(a)
    
d = byte_xor(c,key2)
with open("s2","wb") as f:
    f.write(d)
    
e = byte_xor(c,a)
with open("s3","wb") as f:
    f.write(e)