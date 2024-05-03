

def dfs(graph, visited, node, component):
    visited[node] = True
    component.append(chr(node + ord('A')))

    for neighbour in range(len(graph)):
        if graph[node][neighbour] != float('inf') and not visited[neighbour]:
            dfs(graph, visited, neighbour, component)

def connected_components(graph):
    visited = [False] * len(graph)
    components = []

    for node in range(len(graph)):
        if not visited[node]:
            component = []
            dfs(graph, visited, node, component)
            components.append(component)

    return components

def main():
    adjacency_matrix = [
        [0, 2, float('inf'), 3, float('inf'), 4, float('inf'), 1],
        [2, 0, 4, 1, 5, float('inf'), 1, float('inf')],
        [float('inf'), 4, 0, 6, 1, 3, 1, 3],
        [3, 1, 6, 0, 5, float('inf'), float('inf'), 2],
        [float('inf'), 5, 1, 5, 0, 4, 5, 2],
        [4, float('inf'), 3, float('inf'), 4, 0, 3, float('inf')],
        [float('inf'), 1, 1, float('inf'), 5, 3, 0, float('inf')],
        [1, float('inf'), 3, 2, 2, float('inf'), float('inf'), 0]
    ]

    components = connected_components(adjacency_matrix)

    # print(components)

    if len(components) == 1:
        print("The graph is connected.")
    else:
        print("The graph is disconnected.")
        for i, component in enumerate(components, 1):
            print("Component", i, ":", component)

if __name__ == "__main__":
    main()
