f=open("data","r")
dic={}

for lines in f:
    print(lines)
    words = lines.split(" ")
    print(words)
    for i in words:
      if i not in dic:
        dic[i]=1
      else:
        dic[i]+=1
print(dic)


for k,v in dic.items():
    print(k,v)