first=0
second=1
print(first)
print(second)
for i in range(2,10):
    fib=first+second
    first=second
    second=fib
    print(fib)


