import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin(num: int = 10000) -> dict:
    freq = Counter(
        sum(
            random.randint(0, 1)
            for _ in range(10)
        ) for _ in range(num)
    )

    return {
        count: round((freq.get(count, 0) / num) * 100, 2)
        for count in range(11)
    }


def draw_gaussian_distribution_graph(data: dict) -> None:
    # put data into plot
    plt.plot(data.keys(), data.values())

    # --------------setup plot---------------
    # labes and title
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    # limits for axis
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    # ticks for axis
    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))
    # enable grid
    plt.grid(True)

    # show plot
    plt.show()
