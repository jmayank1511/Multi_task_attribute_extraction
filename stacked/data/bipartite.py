import pickle
import matplotlib.pyplot as plt
with open("_dressDict.pkl", "rb") as i:
    a = pickle.load(i)
import matplotlib.pyplot as plt
X=set()
Y =set()
apple = {}
for i in a: 
    x = a[i] 
    for j in x: 
        if(j[2]+ " " + j[6] not in apple):
            apple[j[2]+ " " + j[6]]  =1
        else:
            apple[j[2]+ " " + j[6]]  +=1
        X.add(j[2])
        Y.add(j[6])        
edges = []
for i in apple:
    # print(i,apple[i])
    i = i.strip().split()
    edges.append((i[0],i[1]))

import networkx as nx
from networkx.algorithms import bipartite
B = nx.Graph()
B.add_nodes_from(X, bipartite = 0)
B.add_nodes_from(Y, bipartite = 1)
B.add_edges_from(edges)
pos = {}
for idx, i in enumerate(X):
    pos[i] = [0,idx]
for idx, i in enumerate(Y):
    pos[i] = [1,idx]
nx.draw(B, pos, with_labels=False)
nx.draw_networkx_labels(B, pos)

plt.show()