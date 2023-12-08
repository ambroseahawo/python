car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

# items() returns a list containing a tuple for each key value pair
key_value_pair_lst = car.items()
print("List containing tuple for each key value pair: {0}".format(key_value_pair_lst))