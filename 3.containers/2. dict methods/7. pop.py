car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

# pop() removes the element with the specified key
car.pop("model")
# pop() is a mutator method - data state is changed
print("Car dictionary after pop: {0}".format(car))