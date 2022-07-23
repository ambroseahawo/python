"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

def is_distinct(arr):
    """implementation"""

    # initialize new array for distinct elements
    distinct_arr = []

    for each_item in arr:
        if each_item in distinct_arr:
            return False
        distinct_arr.append(each_item)

    return True


# driver code
if __name__ == "__main__":
    # determine number of elements in the array
    array_count = int(input("Enter the number of array elements: ").strip())
    # initialize the array as empty
    input_arr = []

    # populate the array form user input
    for values in enumerate(range(0, array_count)):
        array_ele = int(
            input("Enter array element {0}: ".format(values[0])).strip())
        input_arr.append(array_ele)

    print("Original array: {0}".format(input_arr))
