import networkx as nx
import matplotlib.pyplot as plt

n = int(input())
G = nx.complete_graph(n)

print("Is it Eulerian ?")
if nx.is_eulerian(G):
    print("Yes")
else :
    print("No")

print list(nx.eulerian_circuit(G))

print nx.info(G)
nx.draw(G,with_labels=1)
plt.show()
