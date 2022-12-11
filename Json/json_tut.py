import json

data = '{"name" : "Dibyaranjan", "age": 30}'

json_data = json.loads(data)
print(json_data)
#
data2={
    "name": "DIbyaranjan",
    "cars": ['audi', 'bmw', 'ferrari']
}

jsonmp = json.dumps(data2)
print(jsonmp)