"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2
"""

# user input integer greater than two
GREATER_THAN_2 = False
REMAINDER_LESS_2 = False
COUNTER = 0

while not GREATER_THAN_2:
    INT_INPUT = int(input("Enter an integer greater than 2: "))
    if INT_INPUT > 2:
        GREATER_THAN_2 = True

    while not REMAINDER_LESS_2:
        INT_INPUT /= 2
        if INT_INPUT > 2:
            COUNTER += 1
        else:
            REMAINDER_LESS_2 = True

print("Counter: {0}".format(COUNTER))
