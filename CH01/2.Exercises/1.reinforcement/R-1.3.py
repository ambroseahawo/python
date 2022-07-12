"""Write a short Python function, min_max(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""


def min_max(data: list):
    """implementation"""
    smallest = data[0]
    largest = data[0]

    for each in data:
        if each < smallest:
            smallest = each

    for each in data:
        if each > largest:
            largest = each

    return (smallest, largest)

# populating list method 1
print("")
print("Populating list method 1")
data_input = []
number_of_integers = int(input("Enter number of elements: "))

for values in enumerate(range(0, number_of_integers)):
    element = int(input("Enter integer {0}: ".format(values[0])))

    data_input.append(element)

print(data_input)


print(min_max(data_input))

# populating list method 2
print("")
print("Populating list method 2")
data_input2 = [int(integer) for integer in input("Enter a string of numbers: ")]

print("Confirm integers in array: {0}".format(data_input2))

print(min_max(data_input2))
