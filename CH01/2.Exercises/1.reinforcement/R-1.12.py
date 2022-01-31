# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.

from random import randrange


def custom_choice(data):
    # randomize index from zero to len of dat exclusive
    index = randrange(0, len(data))
    # access random element via the random index
    random_element = data[index]

    return random_element

print(custom_choice(["python", "django", "flask", "nodejs"]))
