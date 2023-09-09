"""
Write a function, linked_list_values, that takes in the head of a linked list as an argument.
The function should return a list containing all values of the nodes in the linked list.
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


def linked_list_values(head):
    res = []
    curr = head
    while curr is not None:
        res.append(curr.val)
        curr = curr.next

    return res


if __name__ == '__main__':
    print(linked_list_values(a))