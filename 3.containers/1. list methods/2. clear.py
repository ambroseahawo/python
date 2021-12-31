fruits = ['apple', 'banana', 'cherry']

print("\nOriginal fruits list: {0}\n".format(fruits))

# clear() removes all the elements from the list
fruits.clear()
# clear() is a mutator method, data state is changed
print("New fruits list: {0}".format(fruits))