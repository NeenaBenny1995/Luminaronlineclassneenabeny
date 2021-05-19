import re
count=0
matcher=re.finditer("ab","abcdfabagfabhghdab")
for i in matcher:
    print("match find at",i.start())  #return position
    print("grup=",i.group()) #which object find matcher
    count+=1
print("count =",count)