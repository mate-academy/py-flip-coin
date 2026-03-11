import matplotlib.pyplot as plt
import random


def flip_coin() -> None:
    heads_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    for _ in range(10000):
        sum_heads = 0
        for _ in range(10):
            sum_heads += random.choice([0, 1])
        heads_dict[sum_heads] += 1
    for i in heads_dict:
        heads_dict[i] = heads_dict[i] / 100
    return heads_dict


def draw_gaussian_distribution_graph(heads_dict: dict) -> None:
    plt.plot(list(heads_dict.keys()), list(heads_dict.values()))

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
