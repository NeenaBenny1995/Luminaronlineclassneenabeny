employee={1000:{"id":1000,"name":"anu","salary":100000},
          1001:{"id":1001,"name":"arjun","salary":122222}}
def emp(**kwargs):#{"id":}
    id=kwargs["id"]
    prop=kwargs["prop"]
    if id in employee:
        print(employee[id]["name"])
        print(employee[id][prop])
    else:
        print("invalid id")
emp(id=1000,prop="salary")