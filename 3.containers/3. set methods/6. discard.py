fruits = {"apple", "banana", "cherry"}

print("\nOriginal fruits set: {0}".format(fruits))

# remove specified item
# discard does not raise an error if specified item does not exist
fruits.discard("pawpaw")
print("Fruits set after discard: {0}".format(fruits))

fruits.discard("apple")
print("Fruits set after discard: {0}".format(fruits))