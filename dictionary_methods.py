car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

## updating the dictionary

car.update({"year": 1950})
car.update({"country": "Germany"})

print(car)

# for key in car.keys():
#     print(key)
#
# for value in car.values():
#     print(value)
#
print(car.get("year"))