import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    results = {}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] = results.get(heads, 0) + 1

    return {heads: (count / 10000) * 100 for heads, count in results.items()}


def draw_gaussian_distribution_graph(results: dict[int, float]) -> None:
    plt.bar(results.keys(), results.values())
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution")
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
