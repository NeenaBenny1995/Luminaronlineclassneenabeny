##division by zero
# num1=int(input("enter"))
# num2=int(input("enter"))
# try:
#   div=num1/num2
#   print(div)
# except:
#   print("exception occured")
###list index out of range
lst=[1,6,2,3]
num1=int(input("enter index value"))
try:
    print(lst[num1])
except:
    print("list index out of range")
finally:
    print("print finally")

###finally block
