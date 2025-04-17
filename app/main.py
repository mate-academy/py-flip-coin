import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    stats = {}
    total = 10000

    for i in range(11):
        stats[i] = 0

    for _ in range(10000):
        result = []

        for i in range(10):
            result.append(random.choice(coin))

        count_heads = result.count("heads")
        stats[count_heads] += 1

    for key in stats:
        stats[key] = round((stats[key] / total) * 100, 2)

    return stats


def draw_gaussian_distribution_graph() -> plt:
    stats = flip_coin()

    x_values = list(stats.keys())
    y_values = list(stats.values())

    plt.plot(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.grid(True)
    plt.show()
