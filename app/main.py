import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            random_result = random.randint(0, 1)
            if random_result == 1:
                heads += 1
        result[heads] = result.get(heads, 0) + 1

    return {key: (value / 10000) * 100 for key, value in result.items()}


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_coord = list(range(11))
    y_coord = [result.get(i, 0.0) for i in x_coord]

    plt.plot(x_coord, y_coord, marker="o")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.ylim(0, 100)
    plt.show()
