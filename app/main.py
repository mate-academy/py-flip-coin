from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    statistics = {x: .0 for x in range(0, 11)}

    experiments_count = 10000
    for _ in range(experiments_count):
        heads = 0
        for _ in range(10):
            heads += randint(0, 1)
        statistics[heads] += 1

    for count in range(11):
        statistics[count] = statistics[count] / experiments_count * 100

    return statistics


def draw_gaussian_distribution_graph(statistic: dict) -> None:

    x_data, y_data = zip(*statistic.items())

    plt.plot(x_data, y_data)

    plt.title("Gaussian Distribution")
    plt.xlabel("Head count")
    plt.ylabel("Drop percentage, %")
