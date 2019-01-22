# check if a binary search tree is a binary search tree
# check_bst(head_node) = (true or false)

# Solution:
    # At first I was thinking a depth first search, but this wouldn't work as the children are also bounded by the parent nodes,
    # as well as the parent nodes above them, etc. 
    # Therefore, I came up with a solution that is a recursive function and essentially a depth first search
import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def check_bst(head, minimum=-math.inf, maximum=math.inf):
    #check if the child nodes are OK
        #If they are, move on and recursively call them on the child nodes, changing the max and min to either carry the parent as the max/min and the other to stay the same, depending on left or right node
        # Don't forget to make a case for if there is no child node there!
    if head is None:
        return True
    if head.value < minimum or head.value >= maximum:
        return False
    return (check_bst(head.left_child, minimum, head.value) and check_bst(head.right_child, head.value, maximum))

head = Node(5)
head_a = Node(2)
head.left_child = head_a
head_b = Node(7)
head.right_child = head_b
a_a = Node(1)
head_a.left_child = a_a
a_b = Node(3)
head_a.right_child = a_b
b_a = Node(6)
head_b.left_child = b_a
b_b = Node(8)
head_b.right_child = b_b


print(check_bst(head))


# How'd I do? 
# Did ok but messed up my base cases and made it more complicated than it had to be
# Then I went back and fixed m base cases and it worked fine in less lines of code.
