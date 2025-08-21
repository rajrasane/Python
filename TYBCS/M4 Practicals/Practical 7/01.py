# 1. Draw a directed graph G1 with vertex set V= {1, 2, 3, 4, 5} and directed edge set E ={(1,4) ,
# (2,3), (1,2), (5,3), (5,1), (4,1), (3,2),(5,2), (5,4)} with specific labelled and give colors to vertices
# & edges .

import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.DiGraph()

V= {1, 2, 3, 4, 5}
G1.add_nodes_from(V)

E ={(1,4),(2,3), (1,2), (5,3), (5,1), (4,1), (3,2),(5,2), (5,4)}
G1.add_edges_from(E)

nx.draw(G1, with_labels=True, node_color='lightblue', edge_color='orange')
plt.title("Directed Graph G1")
plt.show()