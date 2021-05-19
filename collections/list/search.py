lst=[10,12,45,7,85]
flag=0
n=input("enter a number:")
for i in lst:
    if i==n:
        flag=1
        break
    else:
       pass
if flag>0:
    print("element found")
else:
    print("not found")


#linear search
#program complexity increase

