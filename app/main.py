import random
import matplotlib.pyplot as plt


def flip_coin() -> float:
    num_trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / num_trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    point_x = list(data.keys())
    point_y = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.bar(point_x, point_y, color="sky_blue", edgecolor="black")

    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Cases (%)")

    plt.xticks(range(11))
    plt.grid(axis="point_y", linestyle="--", alpha=0.7)

    plt.show()
