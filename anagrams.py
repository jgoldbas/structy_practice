"""
Write a function, anagrams, that takes in two strings as arguments. The function should
return a boolean indicating whether or not the strings are anagrams. Anagrams are strings
that contain the same characters, but in any order.

EX. inputs: restful, fluster
    output: True

    inputs: cats, tocs
    output: False

Approaach: Need to count the frequency of chars in each string --> create a hash map for each string
where the keys are the unique chars and the corresponding values are the count of that char.
--> In Python, use dictionaries

Complexity:
if n = string1 length
m = string2 length
Time: O(n+m)
Space: ~O(n+m) because we have to store the character-count objects

"""
from collections import Counter # For anagrams2 function


# Solution 1
def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)


def char_count(s):
    count = {}
    for letter in s:
        if letter not in count:
            count[letter] = 0
        else:
            count[letter] += 1

    return count


# Solution 2 using Python built in method, Counter
def anagrams2(s1, s2):
    return Counter(s1) == Counter(s2)


# Solution 3 (older)
def anagrams3(s, t):
    if (len(s) != len(t)):
        return False

    dict_s, dict_t = {}, {}

    for el in s:
        dict_s[el] = dict_s.get(el, 0) + 1  # if el is not in dict_s, put 0 for its value, otherwise add 1

    for el in t:
        dict_t[el] = dict_t.get(el, 0) + 1

    return dict_s == dict_t


print(char_count('catss'))
print(anagrams('restful', 'fluster'))
print(anagrams2('cats', 'tacos'))
print(anagrams3("anagrams", "aaangrms"))