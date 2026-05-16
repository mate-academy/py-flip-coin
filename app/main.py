import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:

    number_of_entries = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                         6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    coin = ["Head", "Tail"]

    for _ in range(10_000):
        number_of_heads = 0
        for _ in range(10):
            if random.choice(coin) == "Head":
                number_of_heads += 1
        number_of_entries[number_of_heads] += 1
    for i in range(11):
        number_of_entries[i] = number_of_entries[i] / 100
    return number_of_entries


res = flip_coin()


def write_gaussian_distribution_graph(res: dict) -> None:
    res_keys = list(res.keys())
    res_values = list(res.values())
    xpoints = np.array(res_keys)
    ypoints = np.array(res_values)

    plt.plot(xpoints, ypoints)
    plt.show()


write_gaussian_distribution_graph(res)
