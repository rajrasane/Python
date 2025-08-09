# Edge induced subgraph
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [('u1', 'u2'), ('u2', 'u3'), ('u3', 'u4'), ('u4', 'u1')]
G.add_edges_from(edges)

pos = {
    'u1': (0, 1),
    'u2': (-1, 0),
    'u3': (0, -1),
    'u4': (1, 0)
}

selected_edges = [('u1', 'u2'), ('u2', 'u3'), ('u3', 'u4')]

H = G.edge_subgraph(selected_edges)

plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True)
plt.title("Original Diamond Graph")

plt.subplot(1, 2, 2)
nx.draw(H, pos, with_labels=True)
plt.title("Edge-Induced Subgraph")

plt.tight_layout()
plt.show()