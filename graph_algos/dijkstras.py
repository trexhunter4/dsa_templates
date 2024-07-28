# Dijkstra's is a graph algorithm that searches closer nodes first
# This template will assume that # Dijkstra's takes in a set of edges because you should be optimizing your inputs anyway.

import heapq

def dijkstras(edges, start, target) :
     # Initialize data structures
    visited = {}
    pq = []

    # Start UCS
    # We can modify this to push a tuple so we can track other variables or create a path
    heapq.heappush(pq, (0, start)) 

    while (len(pq) > 0 ) :
        # Pop
        cost, curr = heapq.heappop(pq)

        # Add Visited
        visited[curr] = cost

        # Check target
        if (curr == target) :
            return cost
        
        # Add Children
        for child in edges[curr] :
            # edges format [(dest, cost), ... , (dest, cost)]
            if (child[0] not in visited or cost + child[1] < visited[child]) :
                heapq.heappush(pq, (child[0], cost + child[1]))
    
    return -1


