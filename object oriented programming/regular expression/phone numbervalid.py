
import re
word=(input("enter phone number"))
x="[+][9][1]\d{10}$"
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("invalid")