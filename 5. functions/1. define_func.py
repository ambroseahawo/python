# function describe a traditional, stateless function that is invoked
# without the context of a particular class or an instance of that class
# e.g print(), sorted(data), input()

# the following function counts the number of occurrences of a
# given target value within any form of iterable data set.

def count_occurrences(data, target): # formal parameters
    count = 0

    for item in data:
        if item == target:
            count += 1

    return count

data = [103, 44, 56, 204, 103, 384, 1882, 103, 1830]
print(count_occurrences(data, 103)) # actual parameters

# positional arguments - matching actual parameters to the formal parameters
# keyword arguments - specified by explicitly assigning an actual parameter to a formal parameter by name