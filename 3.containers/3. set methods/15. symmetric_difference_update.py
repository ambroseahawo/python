fruits = {"apple", "banana", "cherry"}
another_set = {"google", "microsoft", "apple"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original another_set: {0}\n".format(another_set))

# symmetric_difference_update() removes the items present in both sets,
# AND inserts the items not present in both sets
fruits.symmetric_difference_update(another_set)

# symmetric_difference_update() is a mutator method
# changes the state of the data
print("New set after symmetric difference update: {0}".format(fruits))