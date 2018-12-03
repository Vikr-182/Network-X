import networkx as nx
import matplotlib.pyplot as plt

G = nx.cycle_graph(100)
H = nx.cycle_graph(100)

nx.draw_circular(G)
nx.draw_spectral(H,with_labels=1)

print nx.info(G)

print nx.is_isomorphic(G,H)
plt.show()
