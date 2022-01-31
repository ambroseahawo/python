# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n

def sum_squares(n):
    # initialise empty list to store the squares
    squares = []
    # initialise initial sum as zero
    total_sum = 0

    # iterate from one to n exclusive
    for ele in range(1, n):
        # get the square of eah element
        squares.append(ele*ele)
    
    # iterate through the squares
    for ele in squares:
        # add each element to the total_sum
        total_sum += ele
    
    return total_sum # return sum of the squares


squares_sum = sum_squares(5)
print(squares_sum)
