"""
Implementation uof element wise multiplication of two lists
"""

def element_wise_multiplication(arr1, arr2):
    """implementation"""
    if len(arr1) != len(arr2) or arr1 is None or arr2 is None:
        return 0
    return [ele1*ele2 for ele1,ele2 in zip(arr1, arr2)]
