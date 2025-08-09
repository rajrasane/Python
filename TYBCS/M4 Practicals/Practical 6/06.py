# Vertex induced subgraph
import networkx as nx
import matplotlib.pyplot as plt

edges = {
    'a': ('v1', 'v2'),
    'b': ('v1', 'v3'),
    'c': ('v2', 'v3'),
    'd': ('v2', 'v4'),
    'e': ('v4', 'v5'),
    'f': ('v3', 'v5')
}

G = nx.Graph()
G.add_edges_from(edges.values())

pos = {
    'v1': (0, 2),
    'v2': (-1, 1),
    'v3': (1, 1),
    'v4': (-1, 0),
    'v5': (1, 0)
}

edge_labels = {v: k for k, v in edges.items()}

selected_vertices = ['v1', 'v2', 'v3', 'v5']  
H = G.subgraph(selected_vertices)  

H_edge_labels = {edge: label for edge, label in edge_labels.items() if edge in H.edges() or (edge[1], edge[0]) in H.edges()}

# Plot original graph
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Original Graph")

# Plot vertex-induced subgraph
plt.subplot(1, 2, 2)
nx.draw(H, pos, with_labels=True)
nx.draw_networkx_edge_labels(H, pos, edge_labels=H_edge_labels)
plt.title("Vertex-Induced Subgraph")

plt.show()