# *
# * * *
# * * * * *
"""for i in range(1,6,2):
    for j in range(1,i+1):
        print("*",end=' ')
    print()"""

#    *
#   * *
#  * * *
# * * * *
lst=[[1001,"arjun",27,1000],[1002,"arun",28,2000],[1003,"binu",28,4000],[1004,"vinu",28,5000]]
print(lst)
sum=0
for emp in lst:

  # print(emp[1])
  # print(emp[3])
  # if emp[3]>2000:
  #     print(emp[1])
  sum=sum+emp[3]
print(sum)
