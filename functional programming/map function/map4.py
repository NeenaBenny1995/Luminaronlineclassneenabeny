employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
     {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
ename=list(map(lambda emp:emp["name"],employees))
print(ename)
esalary=list(map(lambda emp:emp["salary"],employees))
print(esalary)
lst=[4,5,2,8,3]
even=list(filter(lambda number:number%2==0,lst))
print(even)
greater=list(filter(lambda  number:number>5,lst))
print(greater)
dev=list(filter(lambda employees:employees["designation"]=="developer",employees))
dev_name=list(map(lambda employees:employees["name"],dev))
print(dev_name)
developername=list(map(lambda emp:emp["name"],(list(filter(lambda emp:emp["designation"],employees)))))
print(developername)

