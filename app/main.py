import matplotlib.pyplot as plt
from random import randint


def flip_coin() -> dict:
    result = {0: 0,
              1: 0,
              2: 0,
              3: 0,
              4: 0,
              5: 0,
              6: 0,
              7: 0,
              8: 0,
              9: 0,
              10: 0}

    for _ in range(10000):
        count = 0
        for key in range(10):
            flip = randint(0, 1)
            if flip == 0:
                count += 1
        result[count] += 0.01

    return result


def draw_gaussian_distribution_graph(dict_of_values: dict) -> None:
    plt.ylim(0, 100)
    plt.plot(dict_of_values.keys(), dict_of_values.values())
    plt.show()
