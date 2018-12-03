import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from([1,2,3,4,5])

G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,1)])

G_ = nx.complement(G)

print nx.info(G)
print nx.info(G_)

nx.draw(G)
nx.draw(G_,with_labels=1)

print("Are they isomorphic ?")
print nx.is_isomorphic(G,G_)
#A 5-cycle DiGraph cannot be a complement of itself.
plt.show()
