from random import choice
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_tails = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }

    heads_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(10000):
        heads = 0
        attempt = ("heads", "tails")
        for flip in range(10):
            if choice(attempt) == "heads":
                heads += 1
        heads_count[heads] += 1
    for index, value in enumerate(heads_count):
        heads_tails[index] = (value / sum(heads_count)) * 100
    return heads_tails


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot([point for point in points.values()], color="black")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
