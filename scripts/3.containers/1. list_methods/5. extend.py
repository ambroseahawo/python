fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

print("\nOriginal fruits list: {0}".format(fruits))
print("Original cars list: {0}\n".format(cars))

# extend() adds the elements of a list, to the end of current list
# add car list elements to the end of fruits list
fruits.extend(cars) # takes exactly one argument
# extend() is a mutator method - the data state is changed
print("New extended fruits list: {0}".format(fruits))