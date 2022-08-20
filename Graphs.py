"""

В этом блокноте рассмотрены некоторые базовые приемы создания и работы с графами посредством библиотеки NetworkX.
Для более детального изучения всех возможностей рекомендуем обратиться к официальной документации.

"""

import networkx as nx

# Создание графа (число вершин, ребер, ядро)
G = nx.dense_gnm_random_graph(44, 428, seed=68)

# Плотность
print(nx.classes.function.density(G))

# Количество различных путей от вершины 3 до вершины 38
print(len(list(nx.node_disjoint_paths(G, s=3, t=38))))

# Длина кратчайшего пути от вершины 3 до вершины 38
path = nx.shortest_path(G, source=3, target=38)
print(len(path))

# Количество вершин, входящих в клику наибольшего размера
cls = list(nx.enumerate_all_cliques(G))
print(max([len(i) for i in cls]))

print(list(nx.node_disjoint_paths(G, s=3, t=38)))

# Поиск кратчайшего пути для всех пар вершин
sp = dict(nx.all_pairs_shortest_path(G))
print(sp)
