# Edge induced subgraph
import networkx as nx
import matplotlib.pyplot as plt

edges = {
    'e1': ('v1', 'v2'),
    'e2': ('v2', 'v3'),
    'e3': ('v3', 'v4'),
    'e4': ('v4', 'v5'),
    'e5': ('v5', 'v6'),
    'e6': ('v6', 'v1'),
    'e7': ('v2', 'v6'),
    'e8': ('v3', 'v5')
}

G = nx.Graph()
G.add_edges_from(edges.values())

S = ['e2', 'e4', 'e6', 'e8']
H = nx.Graph()
for e in S:
    u, v = edges[e]
    H.add_edge(u, v)

pos = {
    'v1': (0, 1),
    'v2': (1, 2),
    'v3': (2, 2),
    'v4': (3, 1),
    'v5': (2, 0),
    'v6': (1, 0)
}


# Original Graph
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={v: k for k, v in edges.items()})
plt.title("Original Graph G(V, E)")

# Edge Induced Subgraph
plt.subplot(1, 2, 2)
nx.draw(H, pos, with_labels=True)
nx.draw_networkx_edge_labels(H, pos, edge_labels={(edges[e][0], edges[e][1]): e for e in S})
plt.title("Edge-Induced Subgraph G(S)\nS = {e2, e4, e6, e8}")

plt.tight_layout()
plt.show()