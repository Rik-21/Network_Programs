import networkx as nx
import matplotlib.pyplot as plt

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

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
for i in range(len(adjacency_matrix)):
    G.add_node(chr(i + ord('A')))

# Add edges to the graph
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] != float('inf'):
            G.add_edge(chr(i + ord('A')), chr(j + ord('A')), weight=adjacency_matrix[i][j])

# Draw the graph
pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Graph Representation of the Adjacency Matrix')
plt.show()
