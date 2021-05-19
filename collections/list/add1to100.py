#lst[0]**1,lst[1]**2..........

lst=[]
v=1
for i in range(1,10):
    lst.append(i)
    for j in lst:
       s=j**v
       v+=1
       print(s)
print(lst[:])

