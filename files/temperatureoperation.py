f=open(r"C:\Users\user\Downloads\Temperature","r")
dic={}
for lines in f:
    words = lines.rstrip("\n ").split(" ")
    print(words)

    year=words[0]


    if year not in dic:

        dic[year]=words[1]
    else:
        temp = words[1]


        if (int(dic[year])<temp):
            dic[year]=temp
# print(dic[year])
print(dic)


