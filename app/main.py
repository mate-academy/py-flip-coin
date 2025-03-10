import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        counts = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                counts += 1
        result[counts] += 1

    return {j: v / 10000 * 100 for j, v in result.items()}


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.bar(x_values, y_values, color="sky blue", edgecolor="black")

    plt.xlabel("Heads counts")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian Distribution")

    plt.show()
