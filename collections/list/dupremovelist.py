lst=[10,20,20,46,23,23,46]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)