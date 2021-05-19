import re
word=(input("enter string"))
x='[a][A-Za-z0-9\W.+-_]*[b]$'
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("invalid")

