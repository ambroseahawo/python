print('\n')
print('---bool---')  # bool class is used to manipulate logical (boolean) values
# the default constructor, bool(), returns False
is_bool = bool(True)
print(is_bool)

print('\n')
print('---int---')
# the integer constructor, int(), returns value 0 by default
is_integer = int()
print(is_integer)

# if f represents a floating-point value, the syntax int(f) produces the truncated value of f
is_integer = int(3.14)
print(is_integer)

# if s represents a string, then int(s) produces the integral value
# that string represents
# string must use base 10
is_integer = int('137')
print(is_integer)

print('\n')
print('---float---')
# constructor form of float returns 0.0
is_float = float()
print(is_float)

is_float = float(2)
print(is_float)

is_float = float('3.14')
print(is_float)