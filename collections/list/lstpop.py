l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(0))
# 0

print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(3))
# 4

print(l)
# [1, 2, 3, 5, 6, 7, 8, 9]

print(l.pop(-2))
# 8

print(l)
# [1, 2, 3, 5, 6, 7, 9]

print(l.pop())
# 9

print(l)
# [1, 2, 3, 5, 6, 7]