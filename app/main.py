import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    result = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(10))
        result[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
        color="blue"
    )
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
