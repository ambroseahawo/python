fruits = ['apple', 'banana', 'cherry', 'avocado', 'guava']

print("\nOriginal fruits list: {0}\n".format(fruits))

# reverse() reverses the order of the list
# list.reverse()
fruits.reverse()

# reverse() is a mutator method - data state is changed
print("New reversed fruits list: {0}".format(fruits))