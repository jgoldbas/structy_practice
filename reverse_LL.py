"""
Write a function, reverse_list, that takes in the head of a linked list as an argument.
The function should reverse the order of the nodes in the linked list in-place and return
the new head of the reversed linked list.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

# Solution 1 (iterative)
def reverse_list(head):
    curr = head
    prev = None

    while curr is not None:
        next = curr.next    # save the next value first
        curr.next = prev    # change the direction of arrow
        prev = curr     # shift prev forward
        curr = next     # shift curr forward

    return prev     # prev is now the head of the reversed list


def print_ll(head):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


print("List before reversing:")
print_ll(a)

reverse_list(a)

print("List after reversing:")
print_ll(f)


