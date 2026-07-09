import matplotlib.pyplot as plt

import random


def flip_coin() -> dict[int, float]:
    table_statistic = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        table_statistic[heads] += 1
    result = {
        k: round(v / 10000 * 100, 2)
        for k, v in table_statistic.items()
    }
    return result


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    heads_count = result.keys()
    drop_percentage = result.values()
    plt.plot(heads_count, drop_percentage)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
