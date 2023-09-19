"""
Same problem as Leetcode's Two Sum variation: https://leetcode.com/problems/two-sum/
Note: The only difference between the Leetcode version and this version is that Leetcode
requires you to return a list and Structy requires you to return a tuple.

Write a function, pair_sum, that takes in a list and a target sum as arguments.
The function should return a TUPLE containing a pair of indices whose elements sum to the
given target. The indices returned must be unique.

Return the INDICES, not the elements themselves.

There is guaranteed to be exactly one pair that sums to the target.

EX. inputs: [3,2,5,4,1] target = 8
    output: (0,2)

    inputs: [4,7,9,2,5,1] target = 5
    output: (0,5)

Solution 1 (Brute Force): considers every possible pair via 2 nested loops where
n=length of input array
Time: O(n^2)
Space: O(1)

Solution 2 (Optimized): use a hash map (dictionary in Python) for efficient look-up which is constant
time (O(1)) --> iterate through input array only once. In the dictionary, keys are the #s coming
from the input array and their values are the respective index positions in the input array. Must
also fine the complement = target - current_number and subsequent check in dictionary for that
complement. Now the efficiency becomes:
Time: O(n)
Space: O(n)  where n=length of input array

Solution 3: (also optimized) --> returns a list instead of a tuple
"""
# Some enumerate practice
l1= ["eat", "sleep", "repeat"]
for el in enumerate(l1):
    print (el)

for count, ele in enumerate(l1):
    print(count)
    print(ele)


# Solution 1: Brute force
def pair_sum1(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


# Solution 2: Optimized w/ dictionary (hash map)
def pair_sum2(nums, target):
    prev_dict = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in prev_dict: # chks if the complement exists in the dict as a key
            return prev_dict[complement], index
        else: # if not, add this number and its corresponding index to the dict
            prev_dict[num] = index


# Solution 3: Leetcode solution to the Two Sum problem (returns a list)
def two_sum(nums, target):
    prev_dict = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in prev_dict:
            return [prev_dict[diff], index]
        prev_dict[num] = index
    return


if __name__ == '__main__':
    print(pair_sum1([3, 2, 5, 4, 1], 8))
    print(pair_sum2([4, 7, 9, 2, 5, 1], 5))
    print(two_sum([4, 7, 9, 2, 5, 1], 5))