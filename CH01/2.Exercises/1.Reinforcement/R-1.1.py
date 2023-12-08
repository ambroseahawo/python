""" Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is , n = mi for some
integer i, and False otherwise."""


def is_multiple(first_integer: int, second_integer: int):
    """implementation"""
    return bool(first_integer % second_integer == 0)

first_integer_input = int(input("Enter first Integer:\n"))
second_integer_input = int(input("Enter second Integer:\n"))
print(is_multiple(first_integer_input, second_integer_input))
