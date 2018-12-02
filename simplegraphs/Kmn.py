#Sketching a Bipartite graph manually.
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

m = int(input())
n = int(input())

for x in range(m):
    G.add_node(x)

for y in range(n):
    G.add_node(y+m)

for x in range(m):
    for y in range(n):
        G.add_edge(x,y+m)

print nx.info(G)
nx.draw(G)
plt.show()
