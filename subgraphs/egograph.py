import networkx as nx
import matplotlib.pyplot as plt

m = int(input())
G = nx.cycle_graph(m)

point = int(input())
H = nx.ego_graph(G,point)#Draws all sub-graphs w.r.t "point"

nx.draw(H,with_labels=1)
print nx.info(H)
plt.show()
