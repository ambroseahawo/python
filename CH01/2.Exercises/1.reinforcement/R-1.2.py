"""Write a short Python function, is even(k), that takes an integer value and
cannot use the multiplication, modulo, or division operators."""


def is_even(integer):
    """use bitwise operations"""
    return bool(integer & 1 == 0)

integer_input = int(input("Enter an integer value:\n"))
print(is_even(integer_input))
