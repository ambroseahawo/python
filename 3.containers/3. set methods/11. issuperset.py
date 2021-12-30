fruits = {"apple", "banana", "cherry", "mango", "avocado", "pawpaw"}
first_sub_fruits = {"avocado", "mango"}
second_sub_fruits = {"avocado", "mango", "guava"}

print("\nOriginal fruits set: {0}".format(fruits))
print("First sub fruits set: {0}".format(first_sub_fruits))
print("Second sub fruits set: {0}\n".format(second_sub_fruits))

# issuperset returns whether a set contains another set or not
# fruits contains first sub fruits set
fruits_contain_first = fruits.issuperset(first_sub_fruits)
print("Fruits contains first sub fruits: {0}".format(fruits_contain_first))
# fruits contains second sub fruits set
fruits_contain_second = fruits.issuperset(second_sub_fruits)
print("Fruits contains second sub fruits: {0}".format(fruits_contain_second))
