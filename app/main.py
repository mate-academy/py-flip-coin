import random

import matplotlib.pyplot as plt

CASES = 10000
FLIPS = 10


def flip_coin() -> dict[int, float]:
    results = {heads: 0 for heads in range(FLIPS + 1)}

    for _ in range(CASES):
        heads = sum(random.randint(0, 1) for _ in range(FLIPS))
        results[heads] += 1

    return {
        heads: round(count / CASES * 100, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
        color="blue",
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
