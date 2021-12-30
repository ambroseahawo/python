car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

# clear() removes all elements from a dictionary
car.clear()
# clear() is a mutator method - data state is changed 
print("Car dictionary after clear: {0}".format(car))