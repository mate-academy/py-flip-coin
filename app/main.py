import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {key: 0.0 for key in range(11)}
    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            if random.choice([True, False]):
                count_heads += 1
        result[count_heads] += 1
    for value in result:
        result[value] = round(result[value] / 10000 * 100, 2)
    return result


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    xpoints = list(distribution.keys())
    ypoints = list(distribution.values())

    plt.bar(xpoints, ypoints, color="skyblue", edgecolor="black")

    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Experiments")
    plt.title("Distribution of Heads in 10 Coin Flips")

    plt.show()

    distribution = flip_coin()
    draw_gaussian_distribution_graph(distribution)
