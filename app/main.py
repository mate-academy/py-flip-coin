import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_count = {i: float(0) for i in range(11)}

    for _ in range(10000):
        heads = sum(random.choices([0, 1], k=10))
        heads_count[heads] = round(heads_count[heads] + 0.01, 2)

    return heads_count


def draw_gaussian_distribution_graph() -> None:
    heads_count = flip_coin()
    path_x = list(heads_count.keys())
    path_y = list(heads_count.values())
    plt.plot(path_x, path_y)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
