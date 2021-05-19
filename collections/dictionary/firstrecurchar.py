pattern='abcdbca'
dic={}
for words in pattern:
    if words not in dic:
        dic[words]=1
    else:
        print(dic[words])
        break
