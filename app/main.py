import random

import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10_000) -> dict:
    result = {i: 0 for i in range(11)}
    coin = ["head", "tail"]

    for tries in range(num_trials):
        heads = 0
        for _ in range(10):
            if random.choice(coin) == "head":
                heads += 1
        result[heads] += 1

    percentage = {
        head: (count / num_trials) * 100
        for head, count in result.items()
    }
    return percentage


def write_gaussian_distribution_graph(res: dict) -> None:
    keys = list(res.keys())
    values = list(res.values())

    plt.plot(keys, values)
    plt.show()


write_gaussian_distribution_graph(flip_coin())
