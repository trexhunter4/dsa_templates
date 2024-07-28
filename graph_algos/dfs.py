# DFS is a graph algorithm that searches further nodes first
# This template will assume that DFS takes in a set of edges because you should be optimizing your inputs anyway.

from collections import deque

def dfs(edges, start, target) :
    # Initialize data structures
    visited = set()
    stack = deque()

    # Start DFS
    # We can modify this to push a tuple so we can track other variables or create a path
    stack.append(start)

    while (len(stack) > 0) :
        # Pop
        curr = stack.pop()

        # Add to visited
        visited.add(curr)

        # Check target
        if (curr == target) :
            return target
    
        # Append children
        for child in edges[curr] :
            if (child not in visited) :
                stack.append(child)

    return -1