import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node(3) 
G.add_node(4)
G.add_node(5)
G.add_edge(3,4)
G.add_edge(4,3)
G.add_edge(4,5)

"""can/cannot be a simple graph."""

print nx.info(G)
nx.draw(G,with_labels=2)
plt.show()
