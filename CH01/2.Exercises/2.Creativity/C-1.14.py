"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.

1. Find the number of unique elements in an array. Let the number of
    unique elements be X.
2. The number of unique pairs would be X^2. This is because each unique element
    can form a pair with every other unique element including itself.
"""

def distinct_pairs_count(arr, n):
    """implementation"""
    s = set()

    for i in range(n):
        s.add(arr[i])

    count = pow(len(s), 2)

    return count


# driver code
if __name__ == "__main__":
    array_count = int(input("Enter the number of array elements: ").strip())
    input_arr = []

    for values in enumerate(range(0, array_count)):
        array_ele = int(input("Enter array element {0}: ".format(values[0])).strip())
        input_arr.append(array_ele)

    print("Original array: {0}".format(input_arr))

    print("Distinct pairs: {0}".format(distinct_pairs_count(input_arr, len(input_arr))))
