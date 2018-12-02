import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

B = np.matrix([[0,1,0,1],[1,1,1,0],[0,0,1,0],[0,0,0,0]])
G = nx.from_numpy_matrix(B)
B_ = nx.to_numpy_matrix(G)

print (B)
print(B_)

"""
Matrix given -
|0 1 0 1|
|1 1 1 0|
|0 0 1 0|
|0 0 0 0|
"""
"""
Matrix automatically converted to symmetric matrix-
|0 1 0 1|
|1 1 1 0|
|0 1 1 0|
|1 0 0 0|
Note:- Contains no self-loops,Hence the diagonal elementes are ignored.
"""
nx.draw(G,with_labels=1)
print nx.info(G)
plt.show()
