# Using networkx from python code Generate graph B with vertex set { x , y , z , w } and edge set { ( x , y ) , ( x , z ) , ( y , w ) , ( z , w ) , ( y , z ) }. Draw graph B with vertices in red colour and edges in green and suitable title.

import networkx as nx
import matplotlib.pyplot as plt

B = nx.DiGraph()

V = {'x', 'y', 'z', 'w'}
E = {('x', 'y'), ('x', 'z'), ('y', 'w'), ('z', 'w'), ('y', 'z')}

B.add_nodes_from(V)
B.add_edges_from(E)


nx.draw(B, with_labels=True, node_color='red',edge_color='green',)

plt.title("Graph B")
plt.show()