"""

Some basic techniques for creating and working with graphs, NetworkX library.

"""

import networkx as nx

# Creating a graph (number of vertices, edges, core)
G = nx.dense_gnm_random_graph(44, 428, seed=68)

# Density
print(nx.classes.function.density(G))

# Number of different paths from vertex 3 to vertex 38
print(len(list(nx.node_disjoint_paths(G, s=3, t=38))))

# Length of the shortest path from vertex 3 to vertex 38
path = nx.shortest_path(G, source=3, target=38)
print(len(path))

# Number of vertices included in the clique of the largest size
cls = list(nx.enumerate_all_cliques(G))
print(max([len(i) for i in cls]))

print(list(nx.node_disjoint_paths(G, s=3, t=38)))

# Finding the shortest path for all pairs of vertices
sp = dict(nx.all_pairs_shortest_path(G))
print(sp)
