fruits = {"apple", "banana", "cherry"}
another_set = {"google", "microsoft", "apple"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original another_set: {0}\n".format(another_set))

# symmetric_difference returns a set that contains all items
# from both sets, except items that are present in both sets
symmetric_diff_set = fruits.symmetric_difference(another_set)
print("Symmetric difference set: {0}\n".format(symmetric_diff_set))

# symmetric_difference() is an accessor method
# doesn't change the data state
print("Fruits set after symmetric difference: {0}".format(fruits))
print("another_set after symmetric difference: {0}".format(another_set))