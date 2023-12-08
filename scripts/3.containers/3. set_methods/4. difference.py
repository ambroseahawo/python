fruits = {"apple", "banana", "cherry", "avocado"}
second_fruits_set = {"apple", "banana", "cherry", "mango"}

print("\nOriginal fruits set: {0}".format(fruits))
print("Original second fruits set: {0}\n".format(second_fruits_set))

# return set containing the difference between two or more sets

# case 1: return items that only exist in second_fruits_set but not in fruits
sets_difference = second_fruits_set.difference(fruits)
print("Case 1 - Items(s) in second fruits set but not in fruits set: {0}".format(
    sets_difference))

# difference method is an accessor - doesn't change the data state

# case 2: return items that only exist in fruits but not in second_fruits_set
sets_difference = fruits.difference(second_fruits_set)
print("Case 2 - Items(s) in fruits set but not in second fruits set: {0}\n".format(
    sets_difference))
