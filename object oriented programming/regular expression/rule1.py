# import re
# x="[124]" #either a,b,c
# matcher=re.finditer(x,"125786589642665871")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="[^124]" #except 1,2,4
# matcher=re.finditer(x,"125786589642665871")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="[a-z]" #small letters a to z
# matcher=re.finditer(x,"ajghfghkkhj355@#$dhs%3jhd")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="[A-Z]" #capital letters A to Z
# matcher=re.finditer(x,"AJghfghkkhj355@#$dhs%3jhd")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="[a-zA-Z]" #both capital and small
# matcher=re.finditer(x,"2AJgh")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="[0-9]"
# matcher=re.finditer(x,"2AJgh")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="[^a-zA-Z0-9]"
# matcher=re.finditer(x,"@ 2AJgh")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="\s"
# matcher=re.finditer(x,"@ 2AJgh")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())


# import re
# x="\d"
# matcher=re.finditer(x,"@ 2AJgh")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())


# import re
# x="\D"
# matcher=re.finditer(x,"@ 2AJgh")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())


import re
x="\w"
matcher=re.finditer(x,"@ 2AJgh")
for i in matcher:
    print("position =",i.start())
    print("group =",i.group())

#
# import re
# x="\W"
# matcher=re.finditer(x,"@ 2AJgh")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())