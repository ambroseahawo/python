"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
"""

def element_wise_multiplication(arr1, arr2):
    """implementation"""
    return [ele1*ele2 for ele1,ele2 in zip(arr1, arr2)]
