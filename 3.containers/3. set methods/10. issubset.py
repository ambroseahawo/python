fruits = {"apple", "banana", "cherry", "mango", "avocado", "pawpaw"}
first_sub_fruits = {"avocado", "mango"}
second_sub_fruits = {"avocado", "mango", "guava"}

print("\nOriginal fruits set: {0}".format(fruits))
print("First sub fruits set: {0}".format(first_sub_fruits))
print("Second sub fruits set: {0}\n".format(second_sub_fruits))

# issubset returns whether another set contains specified set or not
# fruits contains first sub fruits set
fruits_contain_first = first_sub_fruits.issubset(fruits)
print("Fruits contains first sub fruits: {0}".format(fruits_contain_first))
# fruits contains second sub fruits set
fruits_contain_second = second_sub_fruits.issubset(fruits)
print("Fruits contains second sub fruits: {0}".format(fruits_contain_second))