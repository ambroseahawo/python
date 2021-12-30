fruits = {"apple", "banana", "cherry", "avocado"}
second_fruits_set = {"apple", "banana", "cherry", "mango"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original second fruits set: {0}\n".format(second_fruits_set))

# difference_update() removes items in a set that are also included in another specified set
# difference_update() has no return value

# case 1: remove items in fruits set that are also in second fruits set
fruits.difference_update(second_fruits_set)
print("Fruits set with items not in second fruits set: {0}".format(fruits))

# difference_update() is a mutator - it changes the data state

# case 2: remove items in second fruits set that are also in fruits
fruits = {"apple", "banana", "cherry", "avocado"}
second_fruits_set = {"apple", "banana", "cherry", "mango"}

second_fruits_set.difference_update(fruits)
print("Second Fruits set with items not in fruits set: {0}".format(second_fruits_set))
