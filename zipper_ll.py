"""
Write a function, zipper_lists, that takes in the head of two linked lists as arguments.
The function should zipper the two lists together into single linked list by alternating nodes.
If one of the linked lists is longer than the other, the resulting list should terminate with
the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.

Appraoch: maintain two pointers, 1 for each LL --> also keep a count variable. When count is even,
pull node from LL2; when count is odd, pull node from LL1. This will give you the alternatiing
pattern.

Complexity (iterative):
n = # nodes in LL1
m = # nodes in LL2
Time: O(min(n,m))
Space: O(1)

Complexity (recursive):
n = # nodes in LL1
m = # nodes in LL2
Time: O(min(n,m))
Space: O(min(n,m))
"""


# Solution 1 (iterative)
def zipper_lists(head1, head2):
    tail = head1    # initialize mutated list w/ the first node of LL1
    curr1 = head1.next
    curr2 = head2
    count = 0

    while curr1 is not None and curr2 is not None:
        if count % 2 == 0:  # if count is even, take node from LL2
            tail.next = curr2
            curr2 = curr2.next  # advance curr2 to the next node of LL2

        else:   # otherwise count is odd so take node from LL1
            tail.next = curr1
            curr1 = curr1.next
        # In either scenario above, must advance tail and increment count
        tail = tail.next
        count += 1

    # If 1 LL exits the while loop early (meaning it's shorter than the other list), just tack on
    # the remainder of the other (longer) list
    if curr1 is not None:
        tail.next = curr1
    if curr2 is not None:
        tail.next = curr2

    return head1    # return the head of the mutated zippered list


# Solution 2 (Recursive)
def zipper_lists2(head1, head2):
    # Base cases:
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    # End base cases ^
    # Save head1's next & head2's next FIRST before overwriting
    next1 = head1.next
    next2 = head2.next

    head1.next = head2
    head2.next = zipper_lists2(next1, next2)

    return head1



