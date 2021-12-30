# fromkeys() creates a dictionary from specified keys with specified value
keys = ('key1', 'key2', 'key3')
default_value = 0

new_dict = dict.fromkeys(keys, default_value)
print("\nNew dictionary: {0}".format(new_dict))