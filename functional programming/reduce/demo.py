import functools
lst=[4,5,8,4,7,3]
sum=functools.reduce(lambda no1,no2:no1+no2,lst)
print(sum)
heighest=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(heighest)