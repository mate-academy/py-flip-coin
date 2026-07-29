import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    cases = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads += 1

        result[heads] += 1

    for key in result:
        result[key] = round(result[key] / cases * 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    x = list(distribution.keys())
    y = list(distribution.values())

    plt.plot(x, y)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.show()
