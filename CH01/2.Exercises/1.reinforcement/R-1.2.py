# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

# use bitwise operations

def is_even(k):
    if k & 1 == 0:
        return True
    return False

print(is_even(100))