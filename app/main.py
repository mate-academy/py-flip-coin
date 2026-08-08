import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1
        result[heads_count] += 1

    total = sum(result.values())
    return {k: round((v / total) * 100, 2) for k, v in result.items()}


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    keys = sorted(distribution.keys())
    values = [distribution[k] for k in keys]

    plt.title("Gaussian distribution")
    plt.plot(keys, values)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
