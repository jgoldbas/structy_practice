"""
Write a function, uncompress, that takes a string as an argument.
The function should return an "uncompressed" version of the string where
each 'char' of a group is repeated 'number' times consecutively.

The input string will be formatted into multiple groups according to this
pattern:
<number><char>
EX. '2c' or '3a'

EX. input: '2c3a1t'
    output: 'ccaaat'

Approach: use two pointers (two moving indices)
Time complexity: O(nm) where n=# of groups and
m=max # associated w/ any group
Space complexity: O(nm)

NOTE: in Python, concatenating strings is linear because strings are
immutable --> you're creating a whole new string in order to concatenate
therefore uncompress1 is actually closer to ~O(n^2m).

For better performance, use a list instead of concatenating the res, see
(uncompress2). Using lists, you can then append values which is constant
time.
"""
def uncompress2(s):
    res = []
    i, j = 0, 0
    num_str = '0123456789'

    # Main loop iterates while j is a valid index
    while j < len(s):
        # Current char is s[j], so chk if s[j] is numeric
        if s[j] in num_str:
            j += 1
        else: # otherwise, current char is a letter
            # slice the string beginning at i up to (not incl.) j, recast
            group_num = int(s[i:j])
            res.append(s[j] * group_num)
            j += 1
            # i needs to catch up to j
            i = j

    return "".join(res) # a linear-time operation

def uncompress1(s):
    res = ""
    i, j = 0, 0
    num_str = '0123456789'

    # Main loop iterates while j is a valid index
    while j < len(s):
        # Current char is s[j], so chk if s[j] is numeric
        if s[j] in num_str:
            j += 1
        else: # otherwise, current char is a letter
            # slice the string beginning at i up to (not incl.) j, recast
            group_num = int(s[i:j])
            res += s[j] * group_num
            j += 1
            # i needs to catch up to j
            i = j

    return res

if __name__ == '__main__':
    print(uncompress1("2c3a1t"))

    print(uncompress2("2c3a1t"))