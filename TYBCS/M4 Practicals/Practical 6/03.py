# Vertex induced subgraph
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([
    ('v1', 'v2'), ('v2', 'v6'), ('v6', 'v7'), ('v7', 'v1'),  
    ('v2', 'v5'), ('v5', 'v4'), ('v4', 'v3'), ('v3', 'v2')   
])

S = ['v1', 'v2', 'v3', 'v4', 'v7']
H = G.subgraph(S)

pos = {
    'v1': (-2, 0),
    'v2': (-1, 1),
    'v6': (-2, 2),
    'v7': (-3, 1),
    'v5': (0, 2),
    'v4': (1, 1),
    'v3': (0, 0)
}   

# Original Graph
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True)
plt.title("Original Graph")

# Vertex Induced Subgraph 
plt.subplot(1, 2, 2)
nx.draw(H, pos, with_labels=True)
plt.title("Vertex Induced Subgraph")

plt.show()