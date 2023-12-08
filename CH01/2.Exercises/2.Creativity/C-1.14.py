"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.

1. Find the number of unique elements in an array. Let the number of
    unique elements be X.
2. The number of unique pairs would be X^2. This is because each unique element
    can form a pair with every other unique element including itself.
"""

from itertools import combinations

def distinct_pairs_count(arr, n):
    """implementation"""
    s = set()

    for i in range(n):
        s.add(arr[i])

    count = pow(len(s), 2)

    return count


def get_distinct_pairs(arr):
    """implementation"""
    # distinct_pairs_arr = [", ".join(map(set, comb)) for comb in combinations(arr, 2)]
    distinct_pairs_arr = [set(comb) for comb in combinations(arr, 2)]
    return distinct_pairs_arr

# driver code
if __name__ == "__main__":
    # determine number of elements in the array
    array_count = int(input("Enter the number of array elements: ").strip())
    # initialize the array as empty
    input_arr = []

    # populate the array form user input
    for values in enumerate(range(0, array_count)):
        array_ele = int(input("Enter array element {0}: ".format(values[0])).strip())
        input_arr.append(array_ele)

    print("Original array: {0}".format(input_arr))

    # get distinct pairs
    distinct_pairs = get_distinct_pairs(input_arr)
    print("Distinct pairs: {0}".format(distinct_pairs))

    # counter odd product pairs
    COUNTER = 0

    for each_set in distinct_pairs:
        # get product result
        RESULT = 1
        for each_item in each_set:
            RESULT *= each_item
        if RESULT % 2 != 0:
            COUNTER += 1

    print("Number of odd product pairs: {0}".format(COUNTER))
