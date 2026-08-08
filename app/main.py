from random import choice
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts = Counter([sum([choice((0, 1)) for _ in range(10)])
                      for _ in range(10000)])
    counts_sorted = dict(sorted(counts.items()))
    all_cases = sum(counts_sorted.values())
    return {key: round(value / all_cases * 100, 2)
            for key, value in counts_sorted.items()}


def draw_gaussian_distribution_graph(flip_coin: dict) -> None:
    plt.figure()
    plt.plot(list(flip_coin.keys()),
             list(flip_coin.values()))
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))
    plt.title("Gaussian distribution")
    plt.show()
