car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print('\nOriginal dictionary: {0}\n'.format(car))

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
is_25_in_squares_dict = 25 in squares_dict  # returns false
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
# iterating every key in the dictionary
for every_key in squares_dict:
    print("Dict key: {0}".format(every_key))
print("\n")

# iterating each key value pair
for key_value_tuple in car.items():
    print("Dict key value pair item: {0}".format(key_value_tuple))

# delete the whole dictionary itself
del car
del squares_dict
