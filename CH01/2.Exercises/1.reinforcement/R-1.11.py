# Demonstrate how to use Python’s list comprehension syntax to produce
# the list[1, 2, 4, 8, 16, 32, 64, 128, 256].

# list comprehension

list_ = [2**number for number in range(0, 9)]
print(list_)
