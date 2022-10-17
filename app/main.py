import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res = {i: 0 for i in range(11)}

    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                count += 1
        res[count] += 1

    for key, value in res.items():
        res[key] = value * 100 / 10000

    return res


def draw_gaussian_distribution_graph(result: dict) -> None:
    plt.figure(figsize=(12, 7))
    x, y = zip(*sorted(result.items()))
    plt.plot(x, y, color="blue")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph(flip_coin())
