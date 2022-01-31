# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

string_s = "Sample String"
k = -2
print('n[k]: {0}'.format(string_s[k]))

j = k + len(string_s)
print('n[j]: {0}'.format(string_s[j]))