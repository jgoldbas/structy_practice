"""
Write a function, tree_includes, that takes in the root of a binary tree and a target value.
The function should return a boolean indicating whether or not the value is contained in the tree.
"""


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f


# Solution 1 (using iterative BFS using a deque - a maximally efficient queue)
from collections import deque

def tree_includes1(root, target):
  if not root:
    return False

  my_queue = deque([root])

  while my_queue:
    curr = my_queue.popleft()
    # Processing the current node as it leaves the queue
    if curr.val == target:
      return True

    if curr.left:
      my_queue.append(curr.left)
    if curr.right:
      my_queue.append(curr.right)

  return False  # we've traversed the entire tree & never found the target so return False


# Solution 2 (using recursive DFS - inherent call stack as stack)
def tree_includes2(root, target):
  if not root:
    return False
  if root.val == target:
    return True

  return tree_includes2(root.left, target) or tree_includes2(root.right, target)


print(tree_includes1(a, 'e'))
print(tree_includes1(a, 'h'))
print(tree_includes2(a, 'x'))
