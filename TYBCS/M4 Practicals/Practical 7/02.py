# Draw a directed graph G2 with vertex set V= {1, 2, 3, 4 } and directed edge set i. {(2,4) , (2,3),(1,3), (4,1), (3,2),(1,2)}. with specific labelled and give colors to vertices & edges .

import networkx as nx
import matplotlib.pyplot as plt

G2 = nx.DiGraph()

V= {1, 2, 3, 4 }
E = {(2,4) , (2,3),(1,3), (4,1), (3,2),(1,2)}

G2.add_nodes_from(V)
G2.add_edges_from(E)    


nx.draw(G2, with_labels=True, node_color="red", edge_color="blue")

plt.title("Directed Graph G2")
plt.show()