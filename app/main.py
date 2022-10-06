import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    statistics_dict = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads_counter = sum(random.randint(0, 1) for _ in range(10))
        statistics_dict[heads_counter] += 100 / cases

    return statistics_dict


def draw_gaussian_distribution_graph() -> None:
    statistics_dict = flip_coin()

    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

    plt.axis([0, 10, 0, 100])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    x_points = list(statistics_dict.keys())
    y_points = list(statistics_dict.values())

    plt.plot(x_points, y_points, color="blue")

    fig.savefig("Gaussian distribution.png")
