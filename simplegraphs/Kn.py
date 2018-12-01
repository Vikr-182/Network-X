import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

n = int(input())

for x in range(n):
    G.add_node(x)

for x in range(n):
    for y in range(n):
        G.add_edge(x,y)

print nx.info(G)
nx.draw(G)

plt.show()
