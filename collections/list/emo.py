# lst=[1,2,3,4,5,6]
# element=int(input("enter a number"))
#
# for i in range(len(lst)-1):
#     for j in range(i+1,len(lst)):
#        if lst[i]+lst[j]==element:
#            print("pair found",(lst[i],lst[j]))


# print("not found")

lst=[5,4,3]
newlist=[]
sum=sum(lst)
# print(sum(lst))
for i in lst:
    r=sum-i
    newlist.append(r)
print(newlist)



# consider each element except the last
# for i in range(len(lst) - 1):
#
#     # start from the i'th element until the last element
#     for j in range(i + 1, len(lst)):
#
#         # if the desired sum is found, print it
#         if lst[i] + lst[j] == sum:
#             print("Pair found", (lst[i], lst[j]))
#
#
# # No pair with the given sum exists in the list
# print("Pair not found")