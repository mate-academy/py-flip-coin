import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    heads_distribution = {i: 0.0 for i in range(11)}
    total_experiments = 10000
    for _ in range(total_experiments):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 0:
                heads += 1
        heads_distribution[heads] += 1

    for key, count in heads_distribution.items():
        heads_distribution[key] = (count / total_experiments) * 100
    return heads_distribution


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    x_key = []
    y_value = []
    for key, value in distribution.items():
        x_key.append(key)
        y_value.append(value)
    plt.plot(x_key, y_value)
    plt.xlabel("Heads count")
    plt.ylabel("Heads percentage (%)")
    plt.title("Gaussian distribution")
    plt.show()


draw_gaussian_distribution_graph()
