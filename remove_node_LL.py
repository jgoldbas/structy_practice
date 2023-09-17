"""
Write a function, remove_node, that takes in the head of a linked list and a target value
as arguments. The function should delete the node containing the target value from the linked
list and return the head of the resulting linked list. If the target appears multiple times
in the linked list, only remove the first instance of the target in the list.

Do this in-place.
You may assume that the input list is non-empty.
You may assume that the input list contains the target.

Complexity (iterative):             Complexity (recursive):
n = # of nodes in LL                n = # of nodes in LL
Time: O(n)                          Time: O(n)
Space: O(1)                         Space: O(n)
"""


# Solution 1 (iterative)
def remove_node1(head, target):
    if head.val == target:  # if target is at head of LL, to remove that node, just return all nodes after that node
        return head.next

    curr = head
    prev = None

    while curr:
        if curr.val == target:
            prev.next = curr.next
            break   # break out of loop so subsequent similar nodes are not removed (only remove 1st occurrence)

        prev = curr
        curr = curr.next

    return head


# Solution 2 (recursive)
def remove_node2(head, target):
    # Base case 1 - you've hit the end of the LL
    if head is None:
        return None
    # Base case 2 - same as 1st if block of iterative solution
    if head.val == target:
        return head.next
    # If no match found at head, recurse
    head.next = remove_node2(head.next, target)
    return head