f=open("customer","r")
for lines in f:
    words = lines.rstrip("\n ").split(",")
    fname=words[1]
    # if words[-1]=='india':
    #     print(words[1],words[3],words[-1])
    # age=50
    # if words[3]>"50":
    #     print(words[1],words[2],words[3],words[4])
    if words[4]=="Doctor":
        print(words[1],",",words[2],",",words[3],",",words[4],",",words[5])

