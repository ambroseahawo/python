car = {
    "brand": "Ford",
    "model": "Mustang",
    "color": "Teal",
    "year": 1964
}

print('Original dictionary: {0}\n'.format(car))

# return a list containing a tuple for each key value pair
key_value_list = car.items()
print('List containing tuple for each key value pair: {0}\n'.format(
    key_value_list))

# returns a copy of the specified dict
copy_car = car.copy()
print('Copy of original dictionary: {0}\n'.format(copy_car))

# return list containing the dictionary's keys
dict_keys = car.keys()
print('Dictionary keys list: {0}\n'.format(dict_keys))

# return list of all values in the dictionary
dict_values = car.values()
print('Dictionary values list: {0}'.format(dict_values))

# return value of specified key
model_value = car.get("model")
print('Model value: {0}\n'.format(model_value))

# update the dictionary with the specified key-value pairs
car.update({"brand": "Mercedes"})
print('Dictionary after updating existing element: {0}'.format(car))
car.update({"price": 20000})
print('Dictionary after updating new element: {}\n'.format(car))

# return value of specified key. If the key does not exist:
# insert the key, with the specified value
# setdefault returns the value specified
value = car.setdefault("km/ph", 280)
print('Return value: {0}'.format(value))
print('Dictionary after setdefault: {0}\n'.format(car))

# remove element with specified key
# value of the removed item is the return value of the pop() method
color_element = car.pop("color")
print('Element removed: {0}'.format(color_element))
print('New dictionary after pop: {0}\n'.format(car))

# remove the last inserted key-value pair
last_inserted_pair = car.popitem()
print('Last inserted pair: {0}'.format(last_inserted_pair))
print('New dictionary after popitem: {0}\n'.format(car))

# removes all elements from the dictionary
# but still keeps the dictionary itself as empty
# car.clear()
# print(car)

# return a dictionary with the specified keys and values
# takes two parameters, keys - required and value - optional
# each keys pairs with the specified value
new_keys = ("key1", "key2", "key3")
new_values = 0

new_dict = dict.fromkeys(new_keys, new_values)
print('New dictionary: {0}\n'.format(new_dict))

# dictionary comprehension
squares_dict = {integer: integer*integer for integer in range(1, 11)}
print("Squares dictionary: {0}".format(squares_dict))
# equivalent to
squares_dict = {}
for integer in range(1, 11):
    squares_dict[integer] = integer*integer
print("Squares dictionary: {0}\n".format(squares_dict))

# membership tests for dictionary
# membership tests for key only not value
is_25_in_squares_dict = 25 in squares_dict # returns false
print("Is key 25 in squares dict?: {0}\n".format(is_25_in_squares_dict))

# dictionary built-in functions, different from built-in methods
# return true if all keys of the dictionary are True
is_all_keys_true = all(squares_dict)
print("All keys true?: {0}".format(is_all_keys_true))
# return true if any key is true
is_any_key_true = any(squares_dict)
print("Is any key true?: {0}".format(is_any_key_true))
# return dictionary length
number_of_items = len(squares_dict)
print("Number of items: {0}".format(number_of_items))
# return sorted list of keys in dictionary
sorted_keys_list = sorted(car)
print("Sorted list of keys: {0}\n".format(sorted_keys_list))

# iterating through a dictionary
# item depicts every key in the dictionary
for item in squares_dict:
    print("Dict key: {0}".format(item))
print("\n")

# here item depicts each key value pair
for item in car.items():
    print("Dict key value pair item: {0}".format(item))

# delete the whole dictionary itself
del car
del copy_car
del new_dict
del squares_dict