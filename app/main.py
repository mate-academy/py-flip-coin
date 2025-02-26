import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    findict = {i: 0.0 for i in range(11)}
    for _ in range(10000):
        total = 0
        for _ in range(10):
            key = random.choice([0, 1])
            total += key
        findict[total] += 1

    for key in findict:
        findict[key] = (findict[key] / 10000) * 100

    return findict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_axis = list(data.keys())
    y_axis = list(data.values())
    plt.plot(x_axis, y_axis, marker="o", linestyle="-", color="b")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()


draw_gaussian_distribution_graph()
