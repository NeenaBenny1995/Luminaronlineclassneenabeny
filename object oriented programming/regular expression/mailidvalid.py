import re
word=(input("enter email"))
x='[a-zA-Z0-9\W_.-+]+[@]\w+[.]+\w{2,3}$'
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("invalid")







    # "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    #"[a-zA-Z0-9._+-]+[@]+[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"