fruits = ['apple', 'banana', 'cherry']

print("\nOriginal fruits list: {0}\n".format(fruits))

# insert() adds an element at the specified position
# list.insert(pos, element)

# add avocado as third element, position 2
fruits.insert(2, "avocado")

# insert() is a mutator method - data state is changed
print("New fruits list: {0}".format(fruits))