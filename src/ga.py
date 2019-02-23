import numpy as np


def rand_points(num):
    return np.random.randint(0, 10, (num, 2))


def rand_path(num):
    res = np.arange(num)
    np.random.shuffle(res)
    return res


def evaluate(points, order):
    res = 0
    last = order[0]
    for curr in order[1:]:
        x = points[int(last)][0] - points[int(curr)][0]
        y = points[int(last)][1] - points[int(curr)][1]
        res += (x**2 + y**2)**.5
    return res


def get_child(parents):
    res = parents[0][: int(parents[0].size / 2)]
    for val in parents[1]:
        if val not in res:
            res = np.append(res, val)
    return res


def get_gen(points, prev_gen, gen_size):
    gen = np.empty((0, points.shape[0]))
    avg_len = 0
    if prev_gen is None:
        for i in range(gen_size):
            path = rand_path(points.shape[0])
            gen = np.append(gen, [path], axis=0)
    else:
        evaluation = np.array([])
        for ind in prev_gen:
            evaluation = np.append(evaluation, evaluate(points, ind))
        sum = np.sum(evaluation)
        avg_len = sum / evaluation.size
        evaluation = 1 / evaluation
        evaluation = evaluation / np.sum(evaluation)
        for i in range(gen_size):
            parents = prev_gen[np.random.choice(prev_gen.shape[0], 2, False, evaluation)]
            gen = np.append(gen, [get_child(parents)], axis=0)
    return gen, avg_len
