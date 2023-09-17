"""
Write a function, linked_list_find, that takes in the head of a linked list and a target value.
The function should return a boolean indicating whether or not the linked list contains the target.

Solution 2 (iterative)
Complexity:
n = # of nodes
Time: O(n)
Space: O(1)

Solution 3 (recursive)
Complexity:
n = # of nodes
Time: O(n)
Space: O(n) --> need to store the recursive calls on the call stack
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d


# Solution 1 (iterative)
def linked_list_find1(head, target):
    curr = head
    while curr:
        if curr.val != target:
            curr = curr.next
        else:
            return True
    return False


# Solution 2 (recursive)
def linked_list_find2(head, target):
    if head is None:
        return False
    if head.val == target:
        return True

    return linked_list_find2(head.next, target)


if __name__ == '__main__':
    print(linked_list_find1(a, 'C'))
    print(linked_list_find2(a, 'G'))
