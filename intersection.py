"""
Write a function, intersection, that takes in two lists, a,b, as arguments.
The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

Approach: use a set which has constant-time look-up. Loop through array 1 and add each element to the
set. Then loop through array 2 and check if array 2 element is in the set.

Complexity:
n=length of array 1
m=length of array 2
Time: O(n+m)
Space: O(n)
"""

def intersection(a,b):
    my_set = set()
    intersection_a_b = []

    for num in a:
        my_set.add(num)

    for i in range(len(b)):
        if b[i] in my_set:
            intersection_a_b.append(b[i])

    return intersection_a_b

print(intersection([4,2,1,6], [3,6,9,2,10]))