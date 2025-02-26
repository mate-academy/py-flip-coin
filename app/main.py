import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    findict = {i: 0.0 for i in range(11)}
    for i in range(10000):
        total = 0
        for j in range(10):
            key = random.choice([0, 1])
            total += key
        findict[total] += 1

    for key in findict:
        findict[key] = (findict[key] / 10000) * 100

    return findict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()


draw_gaussian_distribution_graph()




