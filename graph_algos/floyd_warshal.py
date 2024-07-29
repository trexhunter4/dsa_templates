# Floyd Warshal is a graph algorithm that finds the fastest path from to all pairs of nodes
# This template will assume that Floyd Warshal takes in a list of edges
# We also take in n, the number of edges
# edges in the format (source, dest, cost)

def floyd_warshal(edges, n) :
    # Create adjacency matrix
    graph = [[float('inf')] * n for _ in range(n)]

    # Set 0's for distance to nodes self
    for i in range(n) :
        graph[i][i] = 0
    
    # Put edges into graph
    for edge in edges :
        graph[edge[0]][edge[1]] = edge[3]

    # Floyd Warshal
    for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Update shortest path from i to j through k
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    return graph