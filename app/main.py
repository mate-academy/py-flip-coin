import matplotlib.pyplot as plt
import random

count_iteration = 10_000
flip_coin_times = 10


def flip_coin() -> dict:
    statistics = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                  5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for _ in range(count_iteration):
        count_goals = 0
        for coin in range(flip_coin_times):
            flip = random.randint(0, 1)
            if flip:
                count_goals += 1
        statistics[count_goals] += 1

    for stat in statistics.keys():
        statistics[stat] = statistics[stat] / count_iteration * 100

    return statistics


def draw_gaussian_distribution_graph(
        dict_to_graph: dict,
        title: str,
        x_label: str,
        y_label: str
) -> None:
    plt.plot(dict_to_graph.keys(), dict_to_graph.values())

    plt.title(title)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xlim(0, flip_coin_times)
    plt.ylim(0, 100)
    plt.show()

draw_gaussian_distribution_graph(
    flip_coin(),
    "Coin Flip",
    "numbers of possible heads dropped",
    "precent of heads dropped")
