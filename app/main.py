import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    head_tail = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):

            result = random.choice(["Head", "Tail"])
            if result == "Head":
                heads_count += 1
        head_tail[heads_count] += 1
    for key in head_tail:
        head_tail[key] = round(head_tail[key] / 10000 * 100, 2)
    return head_tail


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    head_counts = list(results.keys())
    percentages = list(results.values())

    plt.bar(head_counts, percentages, color="skyblue", edgecolor="black")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Occurrences")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
