import json
# dictinoary

# person = {"name":"Ali",
#           "languages":["python","c#"]}

# result = person["name"]
# result = person["languages"]
# result = person["languages"][0]

# JSON string to Dict
person_string = '{"name":"Ali", "languages":["python","c#"]}'   # Azn önce tanımladığımız dict'in string hali
result = json.loads(person_string)
# print(type(result))
# print(result["name"])

# with open("c:/Users/Mert/Desktop/Python/python_lesson/persons.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])
    
# Dict to JSON string
person_dict = {
    "name":"Mert",
    "languages":["C","Python","C++"]
}

result = json.dumps(person_dict)
# print(result)
# print(type(result))     #type = String

with open("c:/Users/Mert/Desktop/Python/python_lesson/persons.json","w",encoding="utf-8") as f:
    json.dump(person_dict, f)

result = json.dumps(person_dict, indent=3, sort_keys= True)
print(result)