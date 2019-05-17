import networkx as nx
import numpy as np


def get_f_g(n):
    f = 0
    number_of_components = n
    g = 0
    number_of_isolated_vertices = n
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    possible_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            possible_edges.append((i, j))
    for edge in np.random.permutation(possible_edges):
        graph.add_edge(*edge)
        if number_of_components > 1:
            number_of_components = nx.number_connected_components(graph)
            f += 1
        if number_of_isolated_vertices > 0:
            number_of_isolated_vertices = len(list(nx.isolates(graph)))
            g += 1
        if number_of_components == 1 and number_of_isolated_vertices == 0:
            break
    return f, g


def run():
    for n in range(100, 1100, 100):
        f_list = []
        g_list = []
        for i in range(100):
            f, g = get_f_g(n)
            f_list.append(f)
            g_list.append(g)
        expected_f = sum(f_list) / len(f_list)
        expected_g = sum(g_list) / len(g_list)
        print('n=%d, f=%f, g=%f' % (n, expected_f, expected_g))


if __name__ == '__main__':
    run()
