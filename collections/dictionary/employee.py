employee={"id":101,"name":"kiran","desig":"manager","salary":10000}
print("employee name is :",employee["name"])
print("company" in employee)
employee["company"]="TCS"
print(employee)
employee["salary"]+=5000
print(employee)
for i in employee:
    print(i,":",employee[i])