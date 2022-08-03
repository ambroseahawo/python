"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
"""

# integer inputs
int_1 = int(input("Enter first integer: ").strip())
int_2 = int(input("Enter second integer: ").strip())
int_3 = int(input("Enter third integer: ").strip())

print("Integers entered as follows First: {0}, Second: {1}, Third: {2}".format(
    int_1, int_2, int_3
))
