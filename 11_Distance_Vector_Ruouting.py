INF = float('inf')

# Adjacency matrix representing the network
adj_matrix = [
    [0, 2, INF, 3, INF, 4, INF, 1],
    [2, 0, 4, 1, 5, INF, 1, INF],
    [INF, 4, 0, 6, 1, 3, 1, 3],
    [3, 1, 6, 0, 5, INF, INF, 2],
    
    [INF, 5, 1, 5, 0, 4, 5, 2],
    [4, INF, 3, INF, 4, 0, 3, INF],
    [INF, 1, 1, INF, 5, 3, 0, INF],
    [1, INF, 3, 2, 2, INF, INF, 0]
]

def bellman_ford(source, destination, adj_matrix):
    num_nodes = len(adj_matrix)
    distance = [INF] * num_nodes
    distance[source] = 0

    # Perform relaxation for num_nodes - 1 times
    for _ in range(num_nodes - 1):
        for u in range(num_nodes):
            for v in range(num_nodes):
                if adj_matrix[u][v] != INF:
                    if distance[u] + adj_matrix[u][v] < distance[v]:
                        distance[v] = distance[u] + adj_matrix[u][v]

    # Check for negative cycles
    for u in range(num_nodes):
        for v in range(num_nodes):
            if adj_matrix[u][v] != INF:
                if distance[u] + adj_matrix[u][v] < distance[v]:
                    print("Graph contains negative cycle")
                    return

    # Print shortest distance from source to destination
    print("Shortest distance from", chr(ord('A') + source), "to", chr(ord('A') + destination), "is", distance[destination])

    # Find all possible paths from source to destination
    print("All possible paths from", chr(ord('A') + source), "to", chr(ord('A') + destination), "are:")
    find_paths(source, destination, adj_matrix)

def find_paths(source, destination, adj_matrix):
    stack = [(source, [source])]
    while stack:
        (node, path) = stack.pop()
        if node == destination:
            
            print(" -> ".join([chr(ord('A') + node) for node in path]))
        else:
            for next_node, weight in enumerate(adj_matrix[node]):
                if weight != INF and next_node not in path:
                    stack.append((next_node, path + [next_node]))

# Main function
if __name__ == "__main__":
    source_node = 0  # Source node A
    destination_node = 4  # Destination node E
    bellman_ford(source_node, destination_node, adj_matrix)
