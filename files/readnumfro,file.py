# f=open("numbers","r")
# lst=[]
# for num in f:
#     print(num)
#     lst.append(int(num.rstrip("\n")))
# sum=0
# for i in lst:
#     sum=sum+i
#
#
# print(lst)#rstrip remove last character
# print(sum)

"""remove element from sarting use lstrip"""
data="hello"
data1=data.lstrip("h")
print(data1)