"""
Give an example of a Python code fragment that attempts to write an element to a
list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
"""

# specify array length
array_elements = int(input("Enter number of elements in the array: ").strip())
# initialize empty array
input_array = []

# populate the array
for values in enumerate(range(array_elements)):
    array_ele = int(input("Enter array element at position {0}: ".format(values[0])).strip())
    input_array.append(array_ele)

print("Original array: {0}".format(input_array))

try:
    ARRAY_LENGTH = len(input_array)
    data = input_array[ARRAY_LENGTH + 1]
except IndexError:
    print("\"Don’t try buffer overflow attacks in Python!\"")
