from src.ga import *

iterations = 50
gen_size = 50
points = rand_points(50)


def find_path():
    prev_gen = None
    for i in range(iterations):
        cur_gen, avg_len = get_gen(points, prev_gen, gen_size)
        print("{0} avg len: {1}".format(i, avg_len))
        prev_gen = cur_gen


find_path()
