"""
Write a function, compress, that takes 1 string as an argument. The function should return a
compressed version where consecutive occurrences of the same letters are compressed into the
number of occurrences followed by that character. Single character occurrences should not be
changed.
EX. 'aaa' compresses to '3a'
    'cc' compresses to '2c'
    't' should stay as 't'
EX. input: 'ccaaatsss'
    output: '2c3at3s'

Approach: use 2 pointers --> i & j --> want i to be the start of a consecutive streak & j to be
the end of a consecutive streak. j needs to search for the end of a streak.

Complexity:
n = input string length
Time: O(n)
Space: O(n)

Note: compress1 is likely closer to O(n^2) because of the concatenation of result. In order to
optimize, use a list instead --> compress2 function below.
"""
def compress1(s):
    s += '!'
    result = ""
    i,j = 0,0

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            count = j - i
            if count == 1:
                result += s[i]
            else:
                result += str(count) + s[i]
            i = j
    return result

def compress2(s):
    s += '!'
    result = []
    i,j = 0,0

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            count = j - i
            if count == 1:
                result.append(s[i])
            else:
                result.append(str(count))
                result.append(s[i])
            i = j

    return "".join(result)

if __name__ == '__main__':
    print(compress1("ccaaatsss"))

    print(compress2("ccaaatsss"))