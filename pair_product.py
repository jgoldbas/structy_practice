"""
This problem follows the pair_sum problem.

Write a function, pair_product, that takes in a list and a target product as arguments.
The function should return a tuple containing a pair of indices whose elements multiply
to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

Approach: use a hashmap (dictionary in Python) --> calculate the divisor (complement) = target / current num
then check to see if it exists in the dictionary. If it does, you've found a pair whose product equals
the input target product.

Complexity:
n = input array length
Time: O(n)
Space: O(1)
dictionary look-up is O(1)
"""


def pair_product(nums, target_product):
    prev_dict = {}

    for index, num in enumerate(nums):
        complement = target_product / num
        if complement in prev_dict:
            return prev_dict[complement], index
        prev_dict[num] = index


print(pair_product([4,7,9,2,5,1], 35))  # should print (1,4) representing the 7 and 5 from the input arr
