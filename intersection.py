"""
Write a function, intersection, that takes in 2 lists, a,b, as arguments.
The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

Approach: use a set which has constant-time look-up. Loop through array 1 and add each element to the
set. Then loop through array 2 and check if array 2 element is in the set.

Complexity of Solution 1 (Brute Force):
Time: O(nm)
Space: O(min(n,m)) --> bc the intersection of 2 arrays will never be more than the smallest array

Complexity of Solution 2 (optimized):
n=length of array 1
m=length of array 2
Time: O(n+m)
Space: O(n)
"""


# Solution 1 - Brute Force
def intersection1(a, b):
    result = []

    for item in a:
        if item in b:
            result.append(item)

    return result

# NOTE: The in operator does a linear scan under the hood, so line 27 runs in O(n). This brute
# force solution roughly translates to O(nm) runtime.

# Solution 2 - Optimized using a set for constant look-up
def intersection2(a, b):
    my_set = set()
    intersection_a_b = []

    for num in a:
        my_set.add(num)

    for i in range(len(b)):
        if b[i] in my_set:  # this lookup is now O(1) runtime
            intersection_a_b.append(b[i])

    return intersection_a_b


# Solution 3 - using Comprehensions
def intersection3(a, b):
    items_set = set(a)

    return [el for el in b if el in items_set]


if __name__ == '__main__':
    print(intersection1([4, 2, 1, 6], [3, 6, 9, 2, 10]))
    print(intersection2([4, 2, 1, 6], [3, 6, 9, 2, 10]))
    print(intersection3([4, 2, 1, 6], [3, 6, 9, 2, 10]))
