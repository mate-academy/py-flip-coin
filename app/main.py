import random
from collections import Counter

import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    counter = Counter()

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        counter[heads] += 1

    return {
        heads: counter[heads] / cases * 100
        for heads in range(flips + 1)
    }


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()

    plt.plot(list(result.keys()), list(result.values()), color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
