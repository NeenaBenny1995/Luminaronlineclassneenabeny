list1=[]
listodd=[]
listeven=[]
for i in range(1,101):
    list1.append(i)
# print(list1)
for j in list1:
    if j%2==0:
        listeven.append(j)
    else:
        listodd.append(j)
print(list1)
print(listeven)
print(listodd)

