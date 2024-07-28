# BFS is a graph algorithm that searches closer nodes first
# This template will assume that BFS takes in a set of edges because you should be optimizing your inputs anyway.

from collections import deque

def bfs(edges, start, target) :
    # Initialize data structures
    visited = set()
    queue = deque()

    # Start BFS
    # We can modify this to push a tuple so we can track other variables or create a path
    queue.appendleft(start)

    while (len(queue) > 0) :
        # Pop
        curr = queue.pop()

        # Check target
        if (curr == target) :
            return target
    
        # Append children
        for child in edges[curr] :
            if (child not in visited) :
                visited.add(child)
                queue.appendleft(child)

    return -1

