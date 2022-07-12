"""Give a single command that computes the sum from Exercise R-1.6, 
relying on Python’s comprehension syntax and the built-in sum function"""


def sum_odd_squares(n):
    """implementation"""
    # list comprehension
    squares = [number * number for number in range(1, n) if number % 2 != 0]

    # return sum of squares_list
    return sum(squares)


integer_input = int(input("Enter a number: "))
while integer_input < 2:
    integer_input = int(input("Please enter a number greater than 1: "))

squares_sum = sum_odd_squares(integer_input)
print("Squares sum: {0}".format(squares_sum))
