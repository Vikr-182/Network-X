import networkx as nx
import matplotlib.pyplot as plt

n = int(input())
m = int(input())
G = nx.gnm_random_graph(n,m)
#note-If m>(n*(n-1)/2); a complete graph is drawn.

nx.draw(G,with_labels=1)
print nx.info(G)
plt.show()
