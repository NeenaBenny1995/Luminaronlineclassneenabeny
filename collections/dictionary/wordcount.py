line="hai hello hai hello"
words=line.split(" ")
count=1

print(words)
dict={}
for i in words:

   if i not in dict:
     dict[i]=count
   else:
       dict[i]=count+1
print(dict)