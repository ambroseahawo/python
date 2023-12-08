car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

# update() - updates the dictionary with the specified key-value pair

# case 1: update new key-value pair
car.update({"color": "Teal"})
print("Car dictionary after new update: {0}".format(car))

# case 2: update existing key-value pair
car.update({"year": 1886})
print("Car dictionary after existing update: {0}".format(car))
