fruits = {"apple", "banana", "cherry"}
another_set = {"google", "microsoft", "apple"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original another_set: {0}\n".format(another_set))

# update() inserts the items from one set into set to another

# case 1: inserts items from another_set set into fruits set
fruits.update(another_set)
print("Update fruits set: {0}\n".format(fruits))

# update() is a mutator method
# only the fruits set is updated, another_set remains intact
print("another_set after update: {0}".format(another_set))