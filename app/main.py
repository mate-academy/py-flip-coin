import random
import matplotlib.pyplot as plt


def flip_once() -> int:
    heads = 0
    for _ in range(10):
        if random.randint(0, 1) == 1:
            heads += 1
    return heads


def flip_coin() -> dict[int, float]:
    results: dict[int, int] = {i: 0 for i in range(11)}
    total_flips = 10000

    for _ in range(total_flips):
        heads = flip_once()
        results[heads] += 1

    percentage_results: dict[int, float] = {}
    for heads_count in results:
        percentage = (results[heads_count] / total_flips) * 100
        percentage_results[heads_count] = round(percentage, 2)

    return percentage_results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    head_counts = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(
        head_counts, percentages,
        marker="o",
        linestyle="-",
        color="blue"
    )
    plt.title("Gaussian Distribution of Coin Flips (10,000 simulations)")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage (%)")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()
