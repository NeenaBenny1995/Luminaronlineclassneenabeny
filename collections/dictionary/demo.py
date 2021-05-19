dic={}
"""data stored as key value pair
**it support hetrogeniuos data
**insertion order is preserved
**duplication of key is not supported *
**support duplicate value but not supported duplicate key
**dictionary value is collected by using curresponding key"""
dict={"name":"luminar","location":"kakkanad","course":"python","mark":250,"data":2.25,"area":"kakkanadu"}
# print(dict["name"])
# for i in dict:
#     print(i,":",dict[i])
#update
dict["location"]="kochi"

dict["mark"]=50
#or dict["mark"]+=25
print(dict)

#deletiong
del dict["mark"]
print(dict)
# dict.pop()
# print(dict)
print("total" in dict)#check value is present
dict["total"]=150
print(dict)