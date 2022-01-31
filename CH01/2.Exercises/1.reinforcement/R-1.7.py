# Give a single command that computes the sum from Exercise R-1.6, 
# relying on Python’s comprehension syntax and the built-in sum function

def sum_odd_squares(n):
    # list comprehension
    squares = [number * number for number in range(1, n) if number % 2 != 0]

    # return sum of squares_list
    return sum(squares)


odd_squares_sum = sum_odd_squares(5)
print(odd_squares_sum)