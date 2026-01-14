import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    counters = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for __ in range(10):
            if random.random() < 0.5:
                count += 1
        counters[count] += 1
    for kounter in counters:
        percentage = counters[kounter] / 10000 * 100
        counters[kounter] = round(percentage, 2)
    return counters


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    label_x = list(data.keys())
    label_y = list(data.values())

    plt.figure()
    plt.plot(label_x, label_y, marker="o")
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Percentage")
    plt.title("Coin flip distribution (10000 experiments)")
    plt.grid(True)
    plt.show()
