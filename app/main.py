import random
import matplotlib.pyplot as plt


def flip_coin(
        trials: int = 10000,
        flipping_times: int = 10
) -> dict:
    results = {i: 0 for i in range(flipping_times + 1)}

    for _ in range(trials):
        heads = sum(random.randint(0, 1) for _ in range(flipping_times))
        results[heads] += 1

    for per in results:
        results[per] = round((results[per] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())

    plt.bar(keys, values, color="skyblue", edgecolor="black")
    plt.xlabel("Number of Heads in 10 Tosses")
    plt.ylabel("Percentage [%]")
    plt.title("Distribution of Heads in Coin Toss Simulation")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.xticks(range(0, 11))
    plt.show()