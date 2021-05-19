##square of a number
# lst=[1,2,3,4,5]
# def square(num):
#     return num**2
# sq=list(map(square,lst))
# print(sq)
lst=[1,2,3,4,5]
sq=list(map(lambda num:num**2,lst))
print(sq)
