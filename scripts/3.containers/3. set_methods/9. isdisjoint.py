fruits = {"apple", "banana", "cherry", "avocado"}
second_fruits_set = {"apple", "pawpaw", "cherry", "mango"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original second fruits set: {0}\n".format(second_fruits_set))

# isdisjoint returns whether two sets have an intersection or not
# returns true if no intersection, false if intersection present
is_disjoint = fruits.isdisjoint(second_fruits_set)
print("Fruits isdisjoint with second fruits set: {0}".format(is_disjoint))