fruits = {"apple", "banana", "cherry", "mango", "avocado", "pawpaw"}

print("\nOriginal fruits set: {0}".format(fruits))

# pop() removes an element from the set
# takes no argument
# the first random element is removed
# return value is the element removed 
random_first_element = fruits.pop()
print("Random first element removed: {0}".format(random_first_element))
print("Fruits set after pop: {0}".format(fruits))