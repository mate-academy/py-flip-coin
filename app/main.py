import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    counts = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(10))
        counts[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    plt.plot(list(results.keys()), list(results.values()), color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.axis([0, 10, 0, 100])
    plt.show()
