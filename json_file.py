import json

new_data = {
    "Amazon": {
        "name": "Dibyaranjan",
        "age": 30
    }
}

with open("data.json", mode="w") as file:
    json.dump(new_data, file, indent=4)
