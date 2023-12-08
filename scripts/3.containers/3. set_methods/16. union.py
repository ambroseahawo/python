fruits = {"apple", "banana", "cherry"}
another_set = {"google", "microsoft", "apple"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original another_set: {0}\n".format(another_set))

# union() returns a set containing all items from both sets,
# duplicates are excluded
union_set = fruits.union(another_set)
print("Union set: {0}".format(union_set))