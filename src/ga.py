import numpy as np
import random


def rand_points(num):
    return np.random.randint(0, 100, (num, 2))


def rand_path(num):
    res = np.arange(num)
    np.random.shuffle(res)
    return res


def evaluate(points, order):
    if order is None:
        return None
    res = 0
    last = order[0]
    for curr in order[1:]:
        x = points[int(last)][0] - points[int(curr)][0]
        y = points[int(last)][1] - points[int(curr)][1]
        res += (x**2 + y**2)**.5
        last = curr
    return res


def get_child(parents, mut_rate):
    start = random.randint(0, parents[0].size - 1)
    end = random.randint(start + 1, parents[0].size)
    res = parents[0][start: end]
    for val in parents[1]:
        if val not in res:
            res = np.append(res, val)
    if random.uniform(0, 1) < mut_rate:
        #print("Mutation!")
        idx = np.random.choice(range(res.size), 2, True)
        tmp = res[idx[0]]
        res[idx[0]] = res[idx[1]]
        res[idx[1]] = tmp
    return res


def get_gen(points, prev_gen, gen_size, mut_rate):
    gen = np.empty((0, points.shape[0]))
    avg_len = 0
    best = None
    if prev_gen is None:
        for i in range(gen_size):
            path = rand_path(points.shape[0])
            gen = np.append(gen, [path], axis=0)
    else:
        lengths = np.array([])
        for ind in prev_gen:
            lengths = np.append(lengths, evaluate(points, ind))
        bestidx = np.argmin(lengths)
        best_length = lengths[bestidx]
        best = prev_gen[bestidx]
        avg_len = np.sum(lengths) / lengths.size
        evaluation = 1 / lengths**4
        evaluation = evaluation / np.sum(evaluation)
        avg_parent_length = 0
        for i in range(gen_size):
            parentidx = np.random.choice(prev_gen.shape[0], 2, False, evaluation)
            avg_parent_length += np.sum(lengths[parentidx])
            parents = prev_gen[parentidx]
            gen = np.append(gen, [get_child(parents, mut_rate)], axis=0)
        print("avg parent len: {0}".format(avg_parent_length / (gen_size * 2)))
    return gen, avg_len, best
