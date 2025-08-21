# Using networkx from python code Generate graph A with vertex set { a , b , c , d } and the edge set { ( a , d ) , ( b , c ) , ( b , d ) , ( a , c ) } . Draw graph A.

import networkx as nx
import matplotlib.pyplot as plt

A = nx.Graph()

v = { 'a' , 'b' , 'c' , 'd' }
e = { ( 'a' , 'd' ) , ( 'b' , 'c' ) , ( 'b' , 'd' ) , ( 'a' , 'c') }

A.add_nodes_from(v)
A.add_edges_from(e)

nx.draw(A)

plt.show()