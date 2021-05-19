num1=int(input("enter"))
num2=int(input("enter"))
try:
  div=num1/num2
  print(div)
except:
  print("exception occured")
finally:
    print("finally")
