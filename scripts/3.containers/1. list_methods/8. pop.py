fruits = ['apple', 'banana', 'cherry', 'avocado', 'guava']

print("\nOriginal fruits list: {0}\n".format(fruits))

# pop() removes the element at the specified position
# list.pop(pos)

# remove the fourth element in fruits list
fruits.pop(3)

# pop() is a mutator method - data state is changed
print("New fruits list: {0}".format(fruits))