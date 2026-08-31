import random
import matplotlib.pyplot as plt


def flip_coin(
        coin: tuple = ("heads", "tails"),
        num_trials: int = 10000,
        num_tosses: int = 10
) -> dict:
    heads_stat = dict.fromkeys(
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        0.0
    )
    for _ in range(num_trials):
        counter = random.choices(coin, k=num_tosses).count("heads")
        heads_stat[counter] += 1
    for key, value in heads_stat.items():
        heads_stat[key] = (value * 100) / num_trials
    return heads_stat


def draw_gaussian_distribution_graph(
        heads: list,
        percents: list
) -> None:
    plt.plot(heads, percents)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()
