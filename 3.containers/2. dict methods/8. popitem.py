car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

# popitem() removes the last inserted key-value pair
car.popitem()
# popitem is a mutator method - data state is changed
print("Car dictionary after popitem: {0}".format(car))