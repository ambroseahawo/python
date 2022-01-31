# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.


def minmax(data):
    smallest = data[0]
    largest = data[0]

    for each in data:
        if each < smallest:
            smallest = each

    for each in data:
        if each > largest:
            largest = each

    return (smallest, largest)


smallest_largest = minmax([14, 43, 27, 9, 39])
print(smallest_largest)