import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads += 1

        results[heads] += 1

    return {
        heads: round(count * 100 / cases, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.bar(
        list(distribution.keys()),
        list(distribution.values())
    )

    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Coin Flip Distribution")
    plt.show()
