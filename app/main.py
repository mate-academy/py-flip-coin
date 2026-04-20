import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        num_dropped_head = 0
        for _ in range(10):
            coin = ["head", "tails"]
            if random.choice(coin) == "head":
                num_dropped_head += 1
        result[num_dropped_head] += 1

    for key in result:
        result[key] = round(result[key] / 10000 * 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_osi = np.array(list(data.keys()))
    y_osi = np.array(list(data.values()))

    plt.plot(x_osi, y_osi, color="blue")

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)

    plt.show()
