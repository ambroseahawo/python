"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
"""

def element_wise_multiplication(arr1, arr2):
    """implementation"""
    if len(arr1) != len(arr2) or arr1 is None or arr2 is None:
        return 0
    return [ele1*ele2 for ele1,ele2 in zip(arr1, arr2)]


# driver code
if __name__ == "__main__":
    # determine number of elements in the array
    array1_count = int(input("Enter the number of array 1 elements: ").strip())
    # initialize the array as empty
    input_arr1 = []

    # populate the array form user input
    for values in enumerate(range(0, array1_count)):
        array_ele = int(
            input("Enter array element {0}: ".format(values[0])).strip())
        input_arr1.append(array_ele)

    print("Original array 1: {0}".format(input_arr1))
    print()

    # determine number of elements in the array
    array2_count = int(input("Enter the number of array 2 elements: ").strip())
    # initialize the array as empty
    input_arr2 = []

    # populate the array form user input
    for values in enumerate(range(0, array2_count)):
        array_ele = int(
            input("Enter array element {0}: ".format(values[0])).strip())
        input_arr2.append(array_ele)

    print("Original array 2: {0}".format(input_arr2))

    print(element_wise_multiplication(input_arr1, input_arr2))
