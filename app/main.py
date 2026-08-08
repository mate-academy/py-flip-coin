import random

from matplotlib import pyplot as plt


def flip_coin() -> dict[int, float]:
    flip_dict = {amount: 0 for amount in range(11)}

    for _ in range(10000):
        heads = 0

        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 0:
                heads += 1

        flip_dict[heads] += 1

    result_dict = {
        amount: round((flip_dict[amount] / 10000) * 100, 2)
        for amount in range(11)
    }

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage (%)")
    plt.title("Gaussian distribution")
    plt.show()
