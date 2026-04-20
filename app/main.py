import matplotlib.pyplot as plt
import random


def flip_coin():
    number_of_experiments = 10_000
    number_of_flips = 10

    experiments_results = {i: 0 for i in range(number_of_flips + 1)}

    for _ in range(number_of_experiments):
        # 1 for head, 0 for other
        cur_result = {1: 0, 0: 0}
        for flip_index in range(number_of_flips):
            cur_result[random.randint(0, 1)] += 1
        experiments_results[cur_result[1]] += 1

    for key in experiments_results:
        experiments_results[key] = int(
            (experiments_results[key] / number_of_experiments) * 100
        )

    return experiments_results


def create_graph():
    data = flip_coin()
    plt.bar(*zip(*data.items()))
    plt.ylim([0, 100])
    plt.show()
