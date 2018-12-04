import networkx as nx
import matplotlib.pyplot as plt

from networkx.algorithms import bipartite

B = nx.Graph()
B.add_nodes_from([1,2,3],bipartite=0)
B.add_nodes_from(['H1','H2','H3'],bipartite=1)

B.add_edges_from([(1,'H1'),(1,'H2'),(1,'H3'),(2,'H1'),(2,'H2'),(2,'H3'),(3,'H1'),(3,'H2'),(3,'H3')])
nx.draw(B,with_labels=1)
print nx.info(B)
plt.show()
