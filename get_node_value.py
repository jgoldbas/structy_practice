"""
Write a function, get_node_value, that takes in the head of a linked list and an index.
The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.

Approach: (iterative) --> use a count variable --> Solution 1
Complexity:
n = # of nodes
Time: O(n)
Space: O(1)

Recursive solution (Solution 2):
Complexity:
Time: O(n)
Space: O(n) --> storing every recursive call on the call stack
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
def get_node_value1(head, index):
    curr = head
    count = 0

    while curr is not None:
        if count == index:
            return curr.val
        count += 1
        curr = curr.next
    return None


# Solution 2 (recursive)
def get_node_value2(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val

    get_node_value2(head.next, index - 1)


if __name__ == '__main__':
    print(get_node_value1(a, 2))
    print(get_node_value2(a, 7))