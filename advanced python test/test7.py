
import re
f=open("phone","r")
fp=open("phonevalid","w")
for lines in f:
    data=lines.rstrip("\n ").split(",")
    phone=data[0]
    x="[+][9][1]\d{10}$"
    match=re.fullmatch(x,phone)
    if match is not None:
        fp.write(phone)
        fp.write("\n")


