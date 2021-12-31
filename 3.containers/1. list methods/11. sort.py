fruits = ['apple', 'banana', 'cherry', 'avocado', 'guava']

print("\nOriginal fruits list: {0}\n".format(fruits))

# sort() arranges the list ascending by default
# list.sort(reverse=True|False, key=sorting_func)
fruits.sort()
print("Fruits sorted ascending: {0}".format(fruits))

# sort descending order
fruits.sort(reverse=True)
print("Fruits sorted descending order: {0}\n".format(fruits))

# sort with sorting function
def sort_len(item):
    return len(item)

# sort fruits list based on item length, ascending
fruits.sort(key=sort_len)
print("Fruits list sorted on item length, ascending: {0}".format(fruits))
# sort fruits list based on item length, descending
fruits.sort(reverse=True, key=sort_len)
print("Fruits list sorted on item length, descending: {0}\n".format(fruits))

def sort_year(item):
    return item['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

print("Original cars list: {0}\n".format(cars))

# sort cars list based on the year, ascending order
cars.sort(key=sort_year)
print("Sorted cars list, ascending: {0}\n".format(cars))

# sort cars list based on the year, descending order
cars.sort(reverse=True, key=sort_year)
print("Sorted cars list, descending: {0}".format(cars))