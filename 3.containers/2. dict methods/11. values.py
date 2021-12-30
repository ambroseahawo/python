car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

# values() returns a view object containing all dictionary values as a list
car_values_object = car.values() # returns an object
car_values_list = list(car_values_object)
print("Car dictionary values: {0}".format(list(car_values_list)))
