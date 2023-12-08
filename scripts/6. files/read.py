# built-in open() function
# returns a file object, also called a file handle
# with statement, ensures that the file is closed when the block 
# inside the with statement is exited
# we don't need to explicitly call the close() method. it is done internally (implicitly)


with open("test.txt", encoding='utf-8') as f:
    # read() extracts a string that contains all xters in the file
    print(f.read())
    # bring file cursor to initial position
    f.seek(0)
    # read the first 4 characters
    print(f.read(4))

# readline(), readlines()