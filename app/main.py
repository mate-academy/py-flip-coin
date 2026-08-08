import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1

        results[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    x_coordinate = list(distribution.keys())
    y_coordinate = list(distribution.values())

    plt.plot(x_coordinate, y_coordinate, marker="o")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.grid(True)

    plt.show()
