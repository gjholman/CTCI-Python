# Given a binary tree, find the lowest common ancestor

# My initial 'brute force' idea was depth first search left side for the numbers, then the right side
# and if they were on opposite sides then we have our lca, but if they're on the same side,
# we traverse the tree in that direction and do it again. This is inefficient though

# The solution I came up with is depth first search and keep track of the path using memoization,
# then when I find the path for both numbers I compare the paths for the lca.

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def lca(n1, n2, head):
    if n1 == n2:
        return n1
    # result_1, path_1 = dfs(n1, head, [])
    # result_2, path_2 = dfs(n2, head, [])
    path_1 = path(n1, head)
    path_2 = path(n2, head)

    if path_1 and path_2:
        ancestor = head.value # This is assuming we want to return the value, not the node.
        i = 0
        print('path 1:')
        for p in path_1:
            print(p.value)
        print('path 2:')
        for p in path_2:
            print(p.value)
        while i < len(path_1) and i < len(path_2):
            if path_1[i].value != path_2[i].value:
                break
            else:
                ancestor = path_1[i].value
                i += 1
        print('result: ')
        return ancestor 
    return False
#       1
#   2       3
#4    5    6   7

# n= 4          n=4         4
# head = 1      head=2      4
# path = [1]    path=[1,2]  [1,2,4]
                            
# This function was close, but not quite what I wanted... better solution below
def dfs(n, head, path):
    if head is None:
        return False, path
    if head.value == n:
        return True, path.append(head)
    else:
        result_left, path_left = dfs(n, head.left, path)
        if result_left:
            path.append(head)
            return True, path_left
        result_right, path_right = dfs(n, head.right, path)
        if result_right:
            path.append(head)
            return True, path_right
    return False, path

# New version, better path finding method 
def path(n, head):
    if not head:
        return []
    print('checking node: {0}'.format(head.value))
    if head.value == n:
        return [head]
    res = path(n, head.left)
    if res:
        return [head] + res
    res = path(n, head.right)
    if res:
        return [head] + res
    return []

head_node = Node(1)
head_node.left = Node(2)
head_node.right = Node(3)
head_node.left.left = Node(4)
head_node.left.right = Node(5)
head_node.right.left = Node(6)
head_node.right.right = Node(7)

print(lca(3, 7, head_node))


# How did I do: I messed up the path finding function... The general thought is correct,
# however I ended up with an error of non iterable NoneType object... not entirely sure
# Also it took me a while, but I'm getting better with tree-based problems
# This problem took me a little over an hour, mostly just some confusion on the path recursion function
# I should remember more about how to use the path algorithm.

# This has a runtime of O(2*(N + log(N))) which is O(N + log(N)) because we have N nodes in the tree, and each path has a maximum of log(N) length and we check the length.

