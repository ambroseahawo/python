"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.

https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
"""

# import itertools module
import itertools

def all_possible_combinations(arr):
    """implementation"""
    for item in range(0, len(arr)+1):
        for subset in itertools.combinations(arr, item):
            if list(subset):
                print("".join(list(subset)))

# driver code
if __name__ == "__main__":
    # default array
    DEFAULT_ARRAY = ['c', 'a', 't', 'd', 'o', 'g']
    print("All Possible strings formed by using the characters: ", end='')
    for index,value in enumerate(DEFAULT_ARRAY):
        if index == len(DEFAULT_ARRAY) - 1:
            print(value)
        else:
            print(value, end=',')
    all_possible_combinations(DEFAULT_ARRAY)
