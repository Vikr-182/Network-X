import networkx as nx 
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from(["A","B","C","D","E"])
G.add_edges_from([("A","B"),("C","B"),("C","D"),("D","E"),("E","A")])

H = nx.cycle_graph(5)

print nx.info(G)
print nx.info(H)

print nx.is_isomorphic(G,H)#prints True/False

nx.draw(G)
nx.draw(H,with_labels=1)
plt.show()
