# the following function multiplies all entires of 
# a numeric data set by a given factor

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

    return data


data = [103, 44, 56, 204, 103, 384, 1882, 103, 1830]
print("\nNew data: {0}".format(scale(data, 5)))