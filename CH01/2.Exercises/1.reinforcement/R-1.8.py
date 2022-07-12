"""Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used
for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j]
references the same element?"""

STRING_S = "Sample String"
print("Length: {0}".format(len(STRING_S)))
k = -5
print('s[k]: {0}'.format(STRING_S[k]))

j = k + len(STRING_S)
print('s[j]: {0}'.format(STRING_S[j]))
