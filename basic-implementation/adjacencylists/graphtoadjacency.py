import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = int(input())
G = nx.complete_graph(n)
A = nx.to_numpy_matrix(G)
H = nx.from_numpy_matrix(A)

nx.draw(G,with_labels=1)
nx.draw(H)
print (A)
print nx.info(G)
print nx.info(H)


plt.show()
