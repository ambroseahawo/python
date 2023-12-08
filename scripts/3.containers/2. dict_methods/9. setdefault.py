car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

# setdefault() returns the value of the specified key.
# if the key does not exist: insert the key, with specified value
color_value = car.setdefault("color", "Teal")
# if the key does not exist, setdefault() becomes a mutator method
print("Car dictionary after setdefault: {0}\n".format(car))

print("Color value: {0}".format(color_value))
print("Color value: {0}".format(car.get("color")))