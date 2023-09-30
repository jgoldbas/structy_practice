"""
Write a function, breadth_first_values that takes in the root of a Binary Tree and returns
a list of all the values of the BT in breadth-first order.
input:
        a
       / \
      b   c
     /\    \
    d e     f
output: ['a','b','c','d','e','f']           vs. DFS output: ['a','b','d','e','c','f']

While DFS uses a stack, BFS uses a queue.
BFS is the same as Level-Order Traversal.

Complexity of Solution 1 (iterative):
n = # of nodes in BT
Time: O(n^2) --> this is because the pop method runs in O(n) time due to shifting of remaining elements
Space: O(n)

Complexity of Solution 2 (also iterative but uses a deque data structure)
Time: O(n) --> now, the .popleft() operation runs in constant time (O(1))
Space: O(n)
"""


# Solution 1 (iterative, uses homemade queue from a list)
def breadth_first_values1(root):
    if not root:    # same as if root is None:
        return []

    my_queue = [root]
    output_vals = []

    while my_queue:
        curr = my_queue.pop(0)
        output_vals.append(curr.val)
        # Consider this newly-popped node's children; must chk if they exist first
        if curr.left:
            my_queue.append(curr.left)
        if curr.right:
            my_queue.append(curr.right)

    return output_vals


# Solution 2 (also iterative, instead uses a deque)
from collections import deque
def breadth_first_values2(root):
    if not root:
        return []

    my_queue = deque.([root])
    output_vals = []

    while my_queue:
        curr = my_queue.popleft()   # removes value from front of (deque) queue
        output_vals.append(curr.val)

        if curr.left:
            my_queue.append(curr.left)
        if curr.right:
            my_queue.append(curr.right)

    return output_vals