# import re
# x="a+"
# matcher=re.finditer(x,"aa gghg aagggh aa ggaa a")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())


# import re
# x="a*"
# matcher=re.finditer(x,"aa abaa")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())
#
#
#output
#==========
# position = 0
# group = aa
# position = 2
# group =
# position = 3
# group = a
# position = 4
# group =
# position = 5
# group = aa
# position = 7
# group =


# import re
# x="a?"
# matcher=re.finditer(x,"aa gghg aagggh")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="a{2}"
# matcher=re.finditer(x,"aaaa gghg aagggh aaa aggaa a")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="a{1,3}"
# matcher=re.finditer(x,"aa gghg aaaa aa ggaa a")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())


# import re
# x="^a"
# matcher=re.finditer(x,"aa gghg aagggh aa ggaa a")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())

# import re
# x="a$"
# matcher=re.finditer(x,"aa gghg aagggh aa ggaa a")
# for i in matcher:
#     print("position =",i.start())
#     print("group =",i.group())