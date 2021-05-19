#apple,apple orenge,orenge
lst=["apple","orenge"]
double=[(i,i) for i in lst]
print(double)
#10,30 10,40 20,30 20,40
lst1=[10,20]
lst2=[30,40]
pairs=[ (i,j) for i in lst1 for j in lst2]
print(pairs)
##even numbers
lst=[1,5,2,4,78,5]
even=[i for i in lst if i%2==0]
print(even)