# Using networkx from python code Generate graph B with vertex set { 1 , 2 , 3 , 4 , 5 } and edge set { ( 4 , 5 ) , ( 5 , 3 ) , ( 2 , 2 ) , ( 2 , 3 ) , ( 2 , 4 ) , ( 3 , 4 ) , ( 1 , 5 ) }. Draw graph B with vertices in red colour and edges in green and suitable title.

import networkx as nx
import matplotlib.pyplot as plt

B = nx.DiGraph()

V = {1, 2, 3, 4, 5}
E = {(4,5), (5,3), (2,2), (2,3), (2,4), (3,4), (1,5)}

B.add_nodes_from(V)
B.add_edges_from(E)


nx.draw(B, with_labels=True, node_color='red',edge_color='green',)

plt.title("Graph B with Vertices {1,2,3,4,5} and Given Edges")
plt.show()