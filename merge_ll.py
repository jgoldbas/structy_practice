"""
Write a function merge_lists that takes the heads of two sorted linked lists as arguments.
The function should merge the 2 lists together into a single, sorted linked list. The function
should return the head of the merged linked list.

Do this in-place by mutating the original nodes.

Assume both input linked list are non-empty and contain increasing sorted numbers.

Complexity (iterative):
n = # of nodes in LL1
m = # of nodes in LL2
Time: O(min(n,m) --> only need the # of iterations for the smallest LL
Space: O(1)
"""


# Solution 1 (iterative)
def merge_lists1(head1, head2):
    dummy_head = Node(None)
    tail = dummy_head
    curr1 = head1
    curr2 = head2

    while curr1 is not None and curr2 is not None:
        if curr1.val < curr2.val:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next

    if curr1 is not None:   # if there are leftover nodes in LL1
        tail.next = curr1
    if curr2 is not None:   # likewise, if there are leftover nodes in LL2
        tail.next = curr2

    return dummy_head