###combination of uppercase and lowercase numbers ending with a number
import re
word=(input("enter"))
x="[a-zA-Z]+\d{1}$"
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("invalid")