def fibonacci():
    a = 0
    b = 1
    
    while True:
        yield a
        future = a + b
        a = b
        b = future

fib_nums = fibonacci()

# for num in fib_nums:
#     if num > 11:
#         break
#     print(num)

print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))