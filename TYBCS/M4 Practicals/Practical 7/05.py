# Using networkx from python code Generate graph G with vertex set { 1 , 2 , 3 , 4 } and the edge set { ( 1 , 2 ) , ( 2 , 3 ) , ( 3 , 4 ) , ( 1 , 4 ) , ( 2 , 4 ) } . Draw graph G.

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

v = {1,2,3,4}
e = {(1,2),(2,3),(3,4),(1,4),(2,4)}

G.add_nodes_from(v)
G.add_edges_from(e)

nx.draw(G)

plt.show()