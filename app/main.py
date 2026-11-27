import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    sides_of_a_coin = ["heads", "tails"]
    result: dict[int, float] = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0
        for coin in range(10):
            if random.choice(sides_of_a_coin) == "heads":
                heads_count += 1
        result[heads_count] += 1
    for key, value in result.items():
        result[key] = value * 100 / 10000
    return result


def draw_gaussian_distribution_graph() -> None:
    result_for_graph = flip_coin()
    heads_counts = list(result_for_graph.keys())
    drop_percentages = list(result_for_graph.values())
    plt.plot(heads_counts, drop_percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()
