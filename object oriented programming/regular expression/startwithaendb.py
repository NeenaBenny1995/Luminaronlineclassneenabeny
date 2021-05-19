###combination of uppercase and lowercase numbers ending with a number
# import re
# word=(input("enter"))
# x="(^a+[a-zA-Z0-9\w]*b$)"
# match=re.fullmatch(x,word)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

##minimum length 8 and max 15,except digit
# import re
# word=(input("enter"))
# x="([\D]{8,15}$)"
# match=re.fullmatch(x,word)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#kerala vehicle registrtaion
import re
word=(input("enter"))
x="([K][L][ ]\d{2}[ ][A-Z]{2}[ ]\d{4}$)"
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("invalid")