# Edge induced subgraph
import networkx as nx
import matplotlib.pyplot as plt

edges = {
    'e1': ('v1', 'v2'),
    'e2': ('v2', 'v3'),
    'e3': ('v3', 'v5'),
    'e4': ('v5', 'v4'),
    'e5': ('v4', 'v3'),
    'e6': ('v5', 'v1')
}

G = nx.Graph()
G.add_edges_from(edges.values())

T = ['e1', 'e3', 'e4', 'e5']

H = nx.Graph()
for e in T:
    u, v = edges[e]
    H.add_edge(u, v)

pos = {
    'v1': (0, 0),
    'v2': (1, 0),
    'v3': (1, 1),
    'v5': (0, 1),
    'v4': (0.5, 2)
}

plt.figure(figsize=(8, 4))

# Plot Original Graph
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={v: k for k, v in edges.items()})
plt.title("G")

# Plot Edge Induced Subgraph
plt.subplot(1, 2, 2)
nx.draw(H, pos, with_labels=True)
nx.draw_networkx_edge_labels(H, pos, edge_labels={v: k for k, v in edges.items() if k in T})
plt.title("H = <T>")

plt.show()