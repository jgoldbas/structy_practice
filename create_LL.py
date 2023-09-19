"""
Write a function, create_linked_list, that takes in a list of values as an argument.
The function should create a linked list containing each item of the list as the values of the nodes.
The function should return the head of the linked list.

Complexity (iterative, solution 1):
n = # of elements in input list
Time: O(n)
Space: O(n) --> creating a node for each element in the list

Complexity (recursive, solution 2):
Time: O(n^2) --> slicing operation in itself is O(n), so for n recursive calls it becomes O(n^2)
Space: O(n)

Complexity (recursive, solution 3):
Time: O(n)
Space: O(n)
"""


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


# Solution 1 (iterative)
def create_linked_list1(values):
    dummy_head = Node(None)
    tail = dummy_head

    for val in values:
        # Create a node that starts at tail.next
        tail.next = Node(val)
        # Prepare for next iteration by progressing tail
        tail = tail.next

    return dummy_head.next


# Solution 2 (recursive v1)
def create_linked_list2(values):
    # Base case: given an empty input list, return empty LL
    if len(values) == 0:
        return None
    # Create a node w/ first element of input list
    head = Node(values[0])

    # Generate LL w/ everything after this node using slicing
    head.next = create_linked_list2(values[1:])

    return head


# Solution 3 (recursive v2)
def create_linked_list3(values, i=0):
    if i == len(values):
        return None

    head = Node(values[i])
    head.next = create_linked_list3(values, i + 1)
    return head


