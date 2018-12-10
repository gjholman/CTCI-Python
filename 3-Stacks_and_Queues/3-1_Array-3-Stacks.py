class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

'''
Multistack: using an array to implement several stacks
we split the array into n pieces, knowing where the head of each stack is at a certain point in the stack.
This also involves shifting over the values after popping. Which is weird and I don't like it particularly,
I can see that more using queues because then we don't have to shift, but rather just remember how long the queue is

[start_of_stack_1, *, *, *, ..., start_of_stack_2, *, *, *, ..., start_of_stack_3, *, *, *, ...]
'''

class MultiStack:
    def __init__(self, limit = 1000, number_of_stacks = 3):
        self.top_item = None
        self.limit = 100
        self.num_stacks = number_of_stacks
        self.values = [None for i in range(self.limit * self.num_stacks)]
        self.size = [0 for i in range(self.num_stacks)]
        return

    # Push the value of the new item onto the stack of choice
    def push(self, stack_num, value): 
        if self.has_space(stack_num):
            new_node = Node(value, self.top_item)
            self.top_item = new_node
            self.size += 1
        return

    def pop(self):
        return


    def is_empty(self):
        return self.size == 0

    def has_space(self, stack_num):
        return self.limit > self.sizes[stack_num]
