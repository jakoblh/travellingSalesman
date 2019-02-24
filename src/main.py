from src.ga import *
import networkx as nx
import matplotlib.pyplot as plt

iterations = 100
gen_size = 100
#points = np.array([(6, 0), (3, 1), (1, 2), (0, 3), (0, 4), (1, 5), (3, 6), (6, 7)])
points = rand_points(10)
mut_rate = .1


def find_path():
    prev_gen = None
    for i in range(iterations):
        prev_gen, avg_len, best = get_gen(points, prev_gen, gen_size, mut_rate)
        if best is not None:
            draw_graph(best, i)
        print("{0} avg len: {1}\n  best len:{2}".format(i, avg_len, evaluate(points, best)))


def draw_graph(ind, index):
    G = nx.Graph()
    prev = ind[0]
    nodes = dict()
    for i in range(points.shape[0]):
        nodes[i] = points[i]
    G.add_nodes_from(nodes.keys())
    for i in ind[1:]:
        p1 = int(prev)
        p2 = int(i)
        G.add_edge(p1, p2)
        prev = i
    nx.draw(G, nodes)
    plt.savefig("imgs/graph{0}.png".format(index), format="PNG")
    plt.clf()


'''
p1 = rand_path(10)
p2 = rand_path(10)
print(p1)
print(p2)
print(get_child([p1, p2], .2))
'''
find_path()
'''
p1 = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(evaluate(points, p1))
'''
