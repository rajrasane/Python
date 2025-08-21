# Draw underlying graph of G1, Find in degrees and out degrees of all vertices in G1 (Ex 1).

import networkx as nx
import matplotlib.pyplot as plt

V = {1, 2, 3, 4, 5}
E = {(1,4), (2,3), (1,2), (5,3), (5,1), (4,1), (3,2), (5,2), (5,4)}

G1 = nx.DiGraph()
G1.add_nodes_from(V)
G1.add_edges_from(E)

print("In-degrees:")
for node, deg in G1.in_degree():
    print(f"Vertex {node}: {deg}")

print("\nOut-degrees:")
for node, deg in G1.out_degree():
    print(f"Vertex {node}: {deg}")

nx.draw(G1)

plt.title("Underlying Graph of G1")
plt.show()
