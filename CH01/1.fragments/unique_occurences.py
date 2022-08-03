"""
Get count of all unique occurrences in a list
"""

# import counter module
from collections import Counter

def count_occurrences(arr, item):
    """implementation"""
    return arr.count(item)


def unique_occurrences_combinations(arr):
    """implementation"""
    all_occurrences = Counter(arr)

    return all_occurrences

    # returns a collection set of all occurrences
    # e.g unique_occurrences_combinations("sample statement".split())
    # Counter({'e': 3, 't': 3, 's': 2, 'a': 2, 'm': 2, 'p': 1, 'l': 1, ' ': 1, 'n': 1})
