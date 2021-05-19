f=open("fileop","r")
f2=open("secondfile","w")
for lines in f:
    f2.write(lines)

print(f2)