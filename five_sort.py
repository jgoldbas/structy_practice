"""
Similar problem to Leetcode's Move Zeroes variation: https://leetcode.com/problems/move-zeroes/
The main difference between Leetcode's and Structy's is Leetcode requires
elements that are not 0s to remain in their original order.

Write a function, five_sort, that takes in a list of numbers as an argument.
The function should rearrange elements of the list such that all 5s appear at the end.
Your function should perform this operation in-place by mutating the original list.
The function should return the list.

Elements that are not 5 can appear in any order in the output, as long as all 5s are at the
end of the list.

Approach: Brute force would have nested loops --> not covered here. A better solution uses 2
pointers starting at either end of the input array.

Complexity:
n=array length
Time: O(n)
Space: O(1) --> must be done in place
"""

def five_sort(nums):
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        else:   # current index i is not a 5
            i += 1

    return nums


# Neetcode solution to Leetcode's Move Zeroes problem
def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right]: # if element at right is non-zero, then swap w/ element at left
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums


if __name__ == '__main__':
    print(five_sort([5, 5, 2, 5, 4, 3]))
    print(moveZeroes([9, 0, 1, 0, 5, 0, 4]))