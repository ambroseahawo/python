nums = [1, 2, 3]

i_nums = iter(nums)

# i_nums is an iterator object
# print(i_nums)

# shows func properties for i_nums
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# also implemented as
while True:
    try:
        item = next(i_nums)
        # print(item)
    except StopIteration:
        break

# n/b;- iterators can only go forward,
# no going backwards or resetting it, or creating a copy of it.

# class implementation that behaves like the built-in range function


class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


# generator function
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
