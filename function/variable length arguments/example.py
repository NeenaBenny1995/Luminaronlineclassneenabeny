def add(*args):#accept arguments in the form of tuples
    res=0
    for i in args:
        res+=i
    return res
print(add(10,20,40,50))
arr=[10,20]
a=sorted(arr)
arr.sort()