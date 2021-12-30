fruits = {"apple", "banana", "cherry", "avocado"}
second_fruits_set = {"apple", "pawpaw", "cherry", "mango"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original second fruits set: {0}\n".format(second_fruits_set))

# intersection_update removes items in a set that are 
# not present in other specified set

# intersection_update() is a mutator - it changes the data state

# remove items in fruits set that are not present in second fruits set
fruits.intersection_update(second_fruits_set)
print("Fruits set with items also in second fruits set: {0}".format(fruits))
