car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

# get() returns the value of the specified key
car_brand = car.get("brand")
print("Car brand: {0}".format(car_brand))