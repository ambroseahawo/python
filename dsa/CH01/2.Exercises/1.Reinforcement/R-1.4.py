"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n"""

def sum_squares(integer: int):
    """implementation"""
    # initialise empty list to store the squares
    squares = []

    # iterate from one to n exclusive
    for ele in range(1, integer):
        # get the square of eah element
        squares.append(ele*ele)

    return sum(squares) # return sum of the squares

integer_input = int(input("Enter a number: "))
while integer_input < 2:
    integer_input = int(input("Please enter a number greater than 1: "))

squares_sum = sum_squares(integer_input)
print("Squares sum: {0}".format(squares_sum))
