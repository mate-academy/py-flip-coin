import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_template = {}
    for _ in range(10_000):
        ls = [random.choice(["heads", "tails"]) for _ in range(10)]
        if ls.count("heads") in result_template:
            result_template[ls.count("heads")] += 1
        else:
            result_template[ls.count("heads")] = 1
    result = {
        key: round(value * 100 / 10_000, 2)
        for key, value in result_template.items()
    }
    return dict(sorted(result.items()))


def draw_gaussian_distribution_graph() -> None:
    plt.plot([value for value in flip_coin().values()])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(top=100)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()
