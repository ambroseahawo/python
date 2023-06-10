
from collections import Counter

def unique_occurrences_combinations(arr):
    """implementation"""
    all_occurrences = Counter(arr)

    return all_occurrences

# def decipher(encoded: list[str], order: str):
match = {
    "P": "A", "X": "B", "M": "C", "S": "D", "A": "E", "C": "F",
    "Z": "G", "E": "H", "V": "I", "G": "J", "I": "K", "J": "L",
    "D": "M", "K": "N", "N": "O", "F": "P", "O": "Q", "R": "R",
    "L": "S", "H": "T", "T": "U", "U": "V", "W": "W", "B": "X",
    "Y": "Y", "Q": "Z"
}

# sorted_dict = OrderedDict(
#     sorted(newList.items(), key=lambda kv: kv[1], reverse=True))
# for color in sorted_dict:
#     print(color, sorted_dict[color])

sample_list_str = {"XX YYY Z YYY XX",
                   "WWWWWZWWWWW"}
sample_frequency_order = "XYZ"
unique_xters = []

for text in sample_list_str:
    new_text = list(text)
    occurrences_counter = unique_occurrences_combinations(new_text)
    unique_xters = list(occurrences_counter)
    print(unique_xters)

# for each_xter in unique_xters:

