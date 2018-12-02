#Sketching a Cycle graph manually.
#You can also use cycle_graph(n)
import networkx as nx 
import matplotlib.pyplot as plt

G = nx.Graph()

n = int(input())

for x in range(n):
    G.add_node(x+1)

u = n-1
for y in range(u):
    G.add_edge(y+1,y+2)

G.add_edge(n,1)

print nx.info(G)

nx.draw(G)

plt.show()
