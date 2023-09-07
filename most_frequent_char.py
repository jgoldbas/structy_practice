"""
Write a function, most_frequent_char, that takes in a string as an argument.
The function should return the most frequent character of the string. If there are ties,
return the character that appears earlier in the string.

You can assume that the input string is non-empty.
EX. input: 'bookeeper'
    output: 'e'

    input: 'mississippi'
    output: 'i' <-- because 'i' comes first in the string before 's'

Complexity:
n = input string length
Time: O(n)
Space: O(n) because we need to store the frequencies object
"""
def most_frequent_char(s):
    frequencies = {}
    # Populate the frequencies dict
    for letter in s:
        if letter not in frequencies:
            frequencies[letter] = 0
        else:
            frequencies[letter] += 1
    # print(frequencies)

    most_frequent = None
    # Iterate over input again to hit the chars in the order they appear in the string
    for letter in s:
        if most_frequent is None or frequencies[letter] > frequencies[most_frequent]:
            most_frequent = letter # replace the most frequent w/ the current letter

    return most_frequent

# Solution 2 using built-in Python method, Counter
from collections import Counter

def most_frequent_char2(s):
    frequencies = Counter(s) # creates a dictionary of counts of letters from the input string

    most_frequent = None
    for letter in s:
        if most_frequent is None or frequencies[letter] > frequencies[most_frequent]:
            most_frequent = letter

    return most_frequent

print("The most frequent letter in 'potato' is {}".format(most_frequent_char("potato")))
print(most_frequent_char2("mississippi")) # should be 'i'