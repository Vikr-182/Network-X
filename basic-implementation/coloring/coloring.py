import networkx as nx
import matplotlib.pyplot as plt

G = nx.star_graph(5)
print ("Dictionary is :")
print nx.coloring.greedy_color(G)

print nx.info(G)
nx.draw(G,with_labels=1,node_color = 'g',node_size=100)
plt.show()
