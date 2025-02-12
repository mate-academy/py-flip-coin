import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        eagle_count = sum(random.choice([0, 1]) for _ in range(10))
        results[eagle_count] += 1

    percentages = {key: (val / 10000) * 100 for key, val in results.items()}
    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(keys, values, markeredgecolor="black")
    plt.title("Distribution of the number of heads in 10 tosses", fontsize=16)
    plt.xlabel("Number of eagles", fontsize=14)
    plt.ylabel("percentage of cases (%)", fontsize=14)
    plt.xticks(keys)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()
    pass
