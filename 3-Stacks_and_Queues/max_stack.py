# Design a stack with push, pop, max (return the max value in the stack), all with a run time of O(1)

# Stack = LIFO. Should be good for interviewer

# Implemented as a linked list
# Push will add to the stack, if it's greater than current max, then we set max to new max
# But doesn't work for popping!
# So we add a feature to the nodes that is the previous max
# Each node remembers the last node that was max

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev_max = None



class MaxStack:
    def __init__(self):
        self.max_node = None
        self.head = None
        return

    def push(self, n):
        new_node = Node(n)
        new_node.next = self.head
        #check if it's greater than the max
        if self.max_node is None or n > self.max_node.value:
            new_node.prev_max = self.max_node
            self.max_node = new_node
            print('new max set to {0}'.format(self.max_node.value))
        self.head = new_node

    def pop(self):
        if self.head is None:
            print('Nothing to pop!')
            return
        pop_node = self.head
        self.head = pop_node.next
        if pop_node == self.max_node:
            self.max_node = pop_node.prev_max
            print('new max set to {0}'.format(self.max_node.value))
        return pop_node.value

myStack = MaxStack()
myStack.push(1)
myStack.push(2)
myStack.push(1)
myStack.pop()
myStack.pop()


# Every operation runs in O(1) time
# The only problems i had were dealing with null pointers (it's called None in python... duh
# In general I was able to think about it the right way though, so that's good!



