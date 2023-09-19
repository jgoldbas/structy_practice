"""
Write a function, insert_node, that takes in the head of a linked list, a value, and an index.
The function should insert a new node with the value into the list at the specified index.
Consider the head of the linked list as index 0. The function should return the head of the
resulting linked list.

Do this in-place.
You may assume that the input list is non-empty and the index is not greater than the
length of the input list.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Solution 1 (iterative)
def insert_node(head, value, index):
    # if you're inserting at the head of the LL
    if index == 0:
        new_head = Node(None)
        new_head.next = head
        return new_head

    count = 0
    curr = head

    while curr:
        if count == index - 1:
            temp = curr.next
            curr.next = Node(value)
            curr.next.next = temp
        count += 1
        curr = curr.next

    return head


