"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""

def remove_punctuations(string_char):
    """implementation"""
    new_string = string_char.replace("'", "")

    return new_string


if __name__ == "__main__":
    # read user input string of chars
    string_characters = input("Enter a string of characters: ").strip()
    print(remove_punctuations(string_characters))
