# Vertex induced subgraph
import networkx as nx
import matplotlib.pyplot as plt

edges = {
    'a': ('v1', 'v2'),
    'b': ('v1', 'v3'),
    'c': ('v2', 'v3'),
}

G = nx.Graph()
G.add_edges_from(edges.values())

pos = {
    'v1': (0, 2),
    'v2': (-1, 1),
    'v3': (1, 1),
}

H = G.subgraph(['v2', 'v3'])

# Plot original graph
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True)
plt.title("Original Graph")

# Plot vertex-induced subgraph
plt.subplot(1, 2, 2)
nx.draw(H, pos, with_labels=True)
plt.title("Vertex-Induced Subgraph")
plt.show()