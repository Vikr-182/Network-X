import networkx as nx
import matplotlib.pyplot as plt\

G = nx.Graph()

for x in range(10):
    G.add_node(x)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,8)
G.add_edge(1,9)
G.add_edge(2,3)
G.add_edge(2,8)
G.add_edge(2,9)
G.add_edge(3,9)
G.add_edge(3,4)
G.add_edge(3,5)
G.add_edge(3,7)
G.add_edge(4,5)
G.add_edge(4,7)
G.add_edge(4,8)
G.add_edge(5,6)
G.add_edge(5,8)
G.add_edge(6,7)
G.add_edge(7,8)
G.add_edge(8,9)

print nx.info(G)
nx.draw(G,with_labels=1)
print nx.is_eulerian(G)
plt.show()
