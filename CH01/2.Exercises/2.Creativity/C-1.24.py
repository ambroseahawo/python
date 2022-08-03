"""
Write a short Python function that counts the number of vowels in a given
character string.
"""

# import module
from collections import Counter

def count_vowels(arr_chars):
    """implementation"""
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    chars_count = 0

    # iterate vowels list and get count of each
    for each_vowel in vowels_list:
        chars_count += arr_chars.count(each_vowel)

    return chars_count

def unique_occurrences_combinations(arr_chars):
    """implementation"""
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    counter = 0

    all_unique_occurrences = Counter(arr_chars)
    print(all_unique_occurrences)

    for each_vowel in vowels_list:
        counter += all_unique_occurrences[each_vowel]

    return counter


if __name__ == "__main__":
    print()
    # specify array length
    input_char_str = input("Enter a character string: ").strip()
    char_str = input_char_str.lower()

    print("Number of vowels in \"{0}\": {1}".format(input_char_str ,unique_occurrences_combinations(list(char_str))))
    # print("Number of vowels in \"{0}\": {1}".format(input_char_str, count_vowels(list(char_str))))

# get all unique occurrences.
# https://stackoverflow.com/questions/34734933/access-contents-of-list-after-applying-counter-from-collections-module
# https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item
