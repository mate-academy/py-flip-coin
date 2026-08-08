import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    flips = {i: 0 for i in range(11)}
    for _ in range(10000):
        head_count = 0
        for _ in range(10):
            if random.choice(["coin_head", "coin_tail"]) == "coin_head":
                head_count += 1
        flips[head_count] += 1
    return {key: round(flips[key] / 10000 * 100, 2) for key in flips}


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    head_counts = sorted(distribution.keys())
    percentages = [distribution[k] for k in head_counts]

    plt.figure(figsize=(8, 5))
    plt.plot(head_counts, percentages, marker="o",
             linestyle="-", color="darkblue")
    plt.title("Distribution of Number of Heads in 10 Coin Flips")
    plt.xlabel("Heads count")
    plt.ylabel("Drop Percentage %")
    plt.xticks(head_counts)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
