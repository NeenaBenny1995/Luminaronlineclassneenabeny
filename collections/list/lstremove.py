l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
print(l)
# ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Alice')
print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Bob')
print(l)
# ['Charlie', 'Bob', 'Dave']