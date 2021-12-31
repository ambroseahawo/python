fruits = ['apple', 'cherry', 'banana', 'cherry']

print("\nOriginal fruits list: {0}\n".format(fruits))

# remove() removes the first item with the specified value
# list.remove(element)

# remove first occurrence of cherry from fruits list
fruits.remove("cherry")

# remove() is a mutator method - the data state is changed
print("New fruits list: {0}".format(fruits))