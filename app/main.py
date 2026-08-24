import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    percentage_of_dropped_heads = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0,
        10 : 0
    }
    for _ in range(10000):
        choices = [random.choice([True, False]) for _ in range(10)].count(True)
        percentage_of_dropped_heads[choices] += 1

    return {key : (0 if value == 0 else value / 100)
            for key, value
            in percentage_of_dropped_heads.items()}


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()
    xpoints = [x for x in points]
    ypoints = [y for y in points.values()]

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
