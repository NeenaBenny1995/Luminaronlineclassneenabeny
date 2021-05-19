lst=[2,5,4,8,6,10,12,22]
element=int(input("enter element"))
sorted_lst=sorted((lst))
print(sorted_lst)
low=0
upper=len(lst)-1
flag=0
print("upper",upper)
while(low<=upper):
   mid=int(low+upper//2)
   print("mid",mid)
   if element>lst[mid]:
      low=mid+1
   elif element<lst[mid]:
      upper=mid-1
   elif element==lst[mid] :
    flag=1
    break
if flag>0:
    print("found")
else:
    print("not found")
