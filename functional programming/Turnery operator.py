#map function

# lst=[1,2,3,4,5,6,7,8]
# def sq(num):
#     return num*num
# s=list(map(sq,lst))
# print(s)
####or usiing lamda
# s=list(map(lambda num:num*num,lst))
# print(s)
#list comprehension
#----------------------
# lst=[]
# for i in range(1,51):
#     lst.append(i)
# print(lst)
#####using list comprehension
# lst=[i for i in range(1,51)]
# print(lst)
#####even list
# lsteven=[i for i in range(1,51) if i%2==0]
# print(lsteven)
####if i is even print square of i else print cube
# lst=[(i*i,"odd") if i%2==0 else (i*i*i,"cube") for i in range(1,51)]
# print(lst)
####if a number is odd print odd else print even
# lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,51)]
# print(lst)


##if num>5 num+1 else num-1
lst=[7,8,9,4,3,2]
newlst=[]
for i in lst:
    newlst.append((i+1)) if i>5 else newlst.append(i-1)
print(newlst)
####using list comprehension
# lst=[7,8,9,4,3,2]
# newlst=[i+1 if i>5 else i-1 for i in lst]
# print(newlst)




