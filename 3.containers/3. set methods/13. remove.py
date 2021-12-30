fruits = {"apple", "banana", "cherry"}

print("\nOriginal fruits set: {0}".format(fruits))

# remove() removes a specified element
fruits.remove("banana")
print("Fruits set after remove: {0}".format(fruits))
# remove() raises an error if specified element does not exist - compare with discard()
fruits.remove("avocado") # this will raise an error