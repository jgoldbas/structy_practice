"""
Write a function, longest_streak, that takes in the head of a linked list as an argument.
The function should return the length of the longest consecutive streak of the same value
within the list. Assume the list is non-empty.

Complexity:
n = # of nodes in LL
Time: O(n)
Space: O(1)
"""


def longest_streak(head):
    max_streak = 0
    curr_streak = 0
    curr = head
    prev_val = None

    while curr:
        if curr.val != prev_val:
            curr_streak = 1
        else:
            curr_streak += 1

        prev_val = curr.val

        if curr_streak > max_streak:
            max_streak = curr_streak

        curr = curr.next

    return max_streak

