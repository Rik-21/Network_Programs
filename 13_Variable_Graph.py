import sys
import time
import random

def dijkstra(graph, src, dest):
    nodes = len(graph)
    visited = [False] * nodes
    distance = [sys.maxsize] * nodes
    parent = [-1] * nodes

    distance[ord(src) - ord('A')] = 0

    for _ in range(nodes - 1):
        min_distance = sys.maxsize
        for v in range(nodes):
            if not visited[v] and distance[v] < min_distance:
                min_distance = distance[v]
                u = v

        visited[u] = True

        for v in range(nodes):
            if not visited[v] and graph[u][v] != sys.maxsize and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]
                parent[v] = u

    path = []
    current = ord(dest) - ord('A')
    while current != -1:
        path.append(chr(current + ord('A')))
        current = parent[current]

    return path[::-1]

def find_stable_path(graph, src, dest, iterations, interval):
    paths = {}

    for _ in range(iterations):
        # Simulate node position changes
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] != sys.maxsize:
                    graph[i][j] = random.randint(1, 10)

        path = dijkstra(graph, src, dest)
        path_str = '->'.join(path)
        if path_str in paths:
            paths[path_str] += 1
        else:
            paths[path_str] = 1

        time.sleep(interval)

    most_stable_path = max(paths, key=paths.get)
    return most_stable_path, paths[most_stable_path]

def main():
    adjacency_matrix = [
        [0, 2, sys.maxsize, 3, sys.maxsize, 4, sys.maxsize, 1],
        [2, 0, 4, 1, 5, sys.maxsize, 1, sys.maxsize],
        [sys.maxsize, 4, 0, 6, 1, 3, 1, 3],
        [3, 1, 6, 0, 5, sys.maxsize, sys.maxsize, 2],
        [sys.maxsize, 5, 1, 5, 0, 4, 5, 2],
        [4, sys.maxsize, 3, sys.maxsize, 4, 0, 3, sys.maxsize],
        [sys.maxsize, 1, 1, sys.maxsize, 5, 3, 0, sys.maxsize],
        [1, sys.maxsize, 3, 2, 2, sys.maxsize, sys.maxsize, 0]
    ]

    src = 'A'
    dest = 'E'
    iterations = 10  # Number of iterations to run Dijkstra's algorithm
    interval = 3  # Interval between iterations (seconds)

    most_stable_path, frequency = find_stable_path(adjacency_matrix, src, dest, iterations, interval)

    print("Most stable path from", src, "to", dest, "is:", most_stable_path)
    print("Frequency:", frequency)

if __name__ == "__main__":
    main()
