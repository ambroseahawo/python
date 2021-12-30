fruits = {"apple", "banana", "cherry", "avocado"}
second_fruits_set = {"apple", "pawpaw", "cherry", "mango"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original second fruits set: {0}\n".format(second_fruits_set))

# intersection returns a set, with items common to two or more sets

# return items that exist in both fruits set and second fruits set
intersection_set = fruits.intersection(second_fruits_set)
print("Items both in fruits and second fruits set: {0}".format(intersection_set)) 