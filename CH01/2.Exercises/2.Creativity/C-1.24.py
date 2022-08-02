"""
Write a short Python function that counts the number of vowels in a given
character string.
"""

# import module
from collections import Counter

def count_vowels(arr_chars):
    """implementation"""
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    counter = 0

    all_unique_occurrences = Counter(arr_chars)

    for each_vowel in vowels_list:
        counter += all_unique_occurrences[each_vowel]

    return counter


if __name__ == "__main__":
    print()
    # specify array length
    input_char_str = input("Enter a character string: ").strip()
    char_str = input_char_str.lower()

    print("Number of vowels in \"{0}\": {1}".format(input_char_str ,count_vowels(list(char_str))))
