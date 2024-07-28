# Prims is an algorithm to generate an MST
# This template will assume that DFS takes in a set of edges because you should be optimizing your inputs anyway.
# edges = {source : (dest, cost)}

import heapq

def prims(edges, n) :
    # Initialize data structures
    visited = set()
    pq = []
    sum = 0

    # Start DFS
    # We can modify this to push a tuple so we can track other variables or create a path

    while (len(pq) > 0 and len(visited) != n) :
            # Pop Curr
            curr, cost = heapq.heappop(pq)

            # Add to Visited Set
            if (curr not in visited) :
                visited.add(curr)

                # Add to Edge Set
                sum += cost

            # Add Children not in Visited Set
            for edge in edges :
                if (edge not in visited) :
                     heapq.heappush(pq, (edge[0], edge[1]))
                    

    return sum