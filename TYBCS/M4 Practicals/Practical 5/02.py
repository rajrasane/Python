import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.Graph()
G2 = nx.Graph()

G1.add_nodes_from([0, 1, 2, 3, 4, 5])
G1.add_edges_from([(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (4, 0), (2, 3), (2, 5), (5, 0)])

G2.add_nodes_from([0, 1, 2, 3, 4, 5])  
G2.add_edges_from([
    (0, 1), (1, 2), (2, 0),
    (3, 4), (4, 5), (5, 3),
    (0, 3), (1, 4), (2, 5)
])

outer_radius = 2
inner_radius = 1

pos_g1 = {2: (0, 2), 1: (2, 1), 3: (-2, 1), 0: (2, -1), 4: (-2, -1), 5: (0, -2)}


pos_g2 = {
    0: (0, outer_radius),                                   
    1: (-outer_radius * 0.866, -outer_radius * 0.5),        
    2: (outer_radius * 0.866, -outer_radius * 0.5),         
    3: (0, inner_radius),                                    
    4: (-inner_radius * 0.866, -inner_radius * 0.5),        
    5: (inner_radius * 0.866, -inner_radius * 0.5)          
}


nx.draw(G1, pos=pos_g1, with_labels=True)
plt.title('Graph G₁')
plt.axis('equal')
plt.show()


nx.draw(G2, pos=pos_g2, with_labels=True)
plt.title('Graph G₂')
plt.axis('equal')
plt.show()

print(nx.is_isomorphic(G1,G2))