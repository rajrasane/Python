# Using networkx from python code generate Directed graph G (Digraph) with vertex set { 1 , 2 , 3, 4 } and the edge set { ( 1 , 2 ) , ( 2 , 3 ) , ( 1 , 3 ) , ( 1, 4 ), (3, 4 ) , (2, 4 ) } . and also draw underlying graph.

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (1, 3), (1, 4), (3, 4), (2, 4)])
nx.draw(G)
plt.show()

UG = G.to_undirected()
nx.draw(UG,with_labels=True,node_color="lightgreen")
plt.title("Underlying Graph of G1")
plt.show()