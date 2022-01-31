# break immediately terminates a loop
# if applied within nested control structures, it causes termination of
# the most immediately enclosing loop

import random

data = [103, 44, 56, 204, 384, 1882, 1830]
found = False
target = random.choice(data)

print("Target: {0}".format(target))

for item in data:
    if item == target:
        found = True
        print('Found')
        break
        # print("This can't be executed")
    print("This still can be executed to some extent")