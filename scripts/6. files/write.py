# w mode overwrites initial file contents.
# a mode appends new content from the end of the initial content 

with open("test.txt", "a", encoding='utf-8') as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Contains three lines\n")