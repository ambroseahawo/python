"""Write a short Python function that takes a positive integer n and returns
he sum of the squares of all the odd positive integers smaller than n."""


def sum_odd_squares(positive_integer: int):
    """implementation"""
    # initialise empty list to contain the squares
    squares = []
    # initialise initial sum as zero
    total_sum = 0

    # iterate from one to n exclusive
    for ele in range(1, positive_integer):
        # evaluate if element is odd
        if ele % 2 != 0:
            # get square of the odd integer
            squares.append(ele*ele)

    # iterate through the squares
    for ele in squares:
        # add each element to the total_sum
        total_sum += ele

    return total_sum  # return sum of the squares

integer_input = int(input("Enter a number: "))
while integer_input < 2:
    integer_input = int(input("Please enter a number greater than 1: "))

squares_sum = sum_odd_squares(integer_input)
print("Squares sum: {0}".format(squares_sum))
