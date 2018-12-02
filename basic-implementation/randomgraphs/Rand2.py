import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = int(input()) #no. of edges
m = float(input()) #seed for random generator
G = nx.gnp_random_graph(n,m)

#Generates a graph with 'n' vertices; each edge has a probabilty of (seed).
#Large sample size, n(edges)~[(nC2)*(seed)]

sample = int(input())
edges_ = []
for x in range(sample):
    H = nx.gnp_random_graph(n,m)
    size = H.size()
    edges_.append(size)

print (np.average(edges_))
print nx.info(G)
nx.draw(G,with_labels=1)
plt.show()
