# continue statement causes the current iteration of
# a loop body to stop, but with subsequent passes of the
# loop proceeding as expected
import random

data = [103, 44, 56, 204, 384, 1882, 1830]
skip_value = random.choice(data)

print("\nTarget: {0}\n".format(skip_value))

for item in data:
    if item == skip_value:
        continue
    print("Value not skipped: {0}".format(item))
