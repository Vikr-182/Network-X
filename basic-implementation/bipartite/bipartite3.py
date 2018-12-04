import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

n = int(input())
m = int(input())
G = nx.gnm_random_graph(n,m)

print ("Is it bipartite?")

if bipartite.is_bipartite(G):
    print("Yes")
    #If it is bipartite check if 2 nodes fall into same partition
    node1 = int(input())
    node2 = int(input())
    X = set([node1,node2])
    print bipartite.is_bipartite_node_set(G,X)

else:
    print("No")

print nx.info(G)
nx.draw(G,with_labels=1)
plt.show()
