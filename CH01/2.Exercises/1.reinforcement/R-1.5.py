# Give a single command that computes the sum from Exercise R-1.4, 
# relying on Python’s comprehension syntax and the built-in sum function

def sum_squares(n):
    # list comprehension
    squares = [number * number for number in range(1, n)]

    # return sum of squares list
    return sum(squares)

squares_sum = sum_squares(5)
print(squares_sum)
