sample_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print("\nOriginal sample tuple: {0}\n".format(sample_tuple))

# count() returns the number of times specified value appears in the tuple
# get number of times 5 appears in the sample tuple
appearances = sample_tuple.count(5)

print("Number of 5 appearances: {0}\n".format(appearances))
# count() is an accessor method -  data state does not change
print("Sample tuple after count: {0}".format(sample_tuple))