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

# A -> B -> C -> D -> None

# Iterative solution to print LL
def print_ll(head):
    current = head
    while current is not None:
        print (current.val)
        current = current.next


# Recursive solution to print LL
def print_ll_recur(head):
    if head is None:    # base case: means list is empty
        return
    print(head.val)
    print_ll_recur(head.next)


if __name__ == '__main__':
    print_ll(a)
    print("-----")
    print_ll_recur(a)