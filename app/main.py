from random import randint

import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count_heads_dict = {}
    for number_of_cases in range(1000):
        count_head = 0
        for number_of_flip in range(10):
            if randint(1, 2) == 1:
                count_head += 1
        if count_head in count_heads_dict:
            count_heads_dict[count_head] += 0.1
        else:
            count_heads_dict[count_head] = 0.1
    return dict(sorted({key: round(value, 2)
                        for key, value in
                        count_heads_dict.items()}.items()))


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    y_graph = np.array([val for val in result.values()])
    x_graph = np.array([keys for keys in result])
    plt.plot(x_graph, y_graph)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
