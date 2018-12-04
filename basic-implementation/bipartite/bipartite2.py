import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

n = int(input())
m = int(input())
G = nx.gnm_random_graph(n,m)

print ("Is it bipartite?")

if bipartite.is_bipartite(G):
    print("Yes")
else:
    print("No")

print nx.info(G)
nx.draw(G,with_labels=1)
plt.show()
