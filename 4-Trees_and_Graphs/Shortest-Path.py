# Given a directed graph, find the shortest path between two nodes if one exists

# 1 -------> 2
# ^ \        |
# |  \       |
#     --> 3  |
# |  /       |
# | /        \/
# 4 <------- 5

# shortestPath(2, 3) = 2,5,4,3

inputGraph = {  1 : set([2, 3]),
                2 : set([5]),
                3 : set([4]),
                4 : set([3,1]) }

# Essentially it is a depth first search but we store the nodes we visited
def shortestPath(start, end, graph = inputGraph):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop(0)
        if vertex == end:
            break
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print(shortestPath(2, 3))

