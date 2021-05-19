f=open("customer","r")
dic={}
for lines in f:
    words = lines.rstrip("\n ").split(",")
    prof=words[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)
