sample_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print("\nOriginal sample tuple: {0}\n".format(sample_tuple))

# index searches for the first occurrence of a specified value and returns its position
# tuple.index(value) - takes exactly one argument
position = sample_tuple.index(8)

print("Position of 8: {0}\n".format(position))

# index() is an accessor method -  data state does not change
print("Sample tuple after index(): {0}\n".format(sample_tuple))
