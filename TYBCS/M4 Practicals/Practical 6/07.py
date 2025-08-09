# Edge induced subgraph
import networkx as nx
import matplotlib.pyplot as plt

edges = {
    'a': ('v1', 'v2'),
    'd': ('v2', 'v4'),
    'g': ('v1', 'v4'),
    'h': ('v1', 'v6'),
    'k': ('v6', 'v4'),
    'l': ('v6', 'v5')
}

G = nx.Graph()
G.add_edges_from(edges.values())

T = ['a', 'g', 'l']  

H = nx.Graph()
for e in T:
    u, v = edges[e]
    H.add_edge(u, v)

pos = {
    'v1': (0, 1),
    'v2': (0, 0),
    'v4': (1, 0),
    'v6': (1, 1),
    'v5': (2, 0.8)
}

# Plot Original Graph 
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={v: k for k, v in edges.items()})
plt.title("Original Graph")

# Plot Edge Induced Subgraph
plt.subplot(1, 2, 2)
nx.draw(H, pos, with_labels=True)
nx.draw_networkx_edge_labels(H, pos, edge_labels={v: k for k, v in edges.items() if k in T})
plt.title("Edge Induced Subgraph")

plt.tight_layout()
plt.show()
