import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    results_by_heads_count = {count: 0 for count in range(11)}
    total_trials = 10_000

    for _ in range(total_trials):
        heads_count = 0
        for _ in range(10):
            coin_side = random.randint(0, 1)
            if coin_side == 1:
                heads_count += 1
        results_by_heads_count[heads_count] += 1

    for heads_count in results_by_heads_count:
        percentage = results_by_heads_count[heads_count] / total_trials * 100
        results_by_heads_count[heads_count] = round(percentage, 2)

    return results_by_heads_count


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    head_counts = sorted(distribution.keys())
    percentages = [distribution[head_count] for head_count in head_counts]

    plt.figure(figsize=(10, 6))
    plt.bar(head_counts, percentages, color="skyblue", edgecolor="black")

    plt.title("Distribution of Heads in 10 Coin Flips (10,000 trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Occurrence")

    plt.xticks(head_counts)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    distribution_result = flip_coin()
    print(distribution_result)
    draw_gaussian_distribution_graph(distribution_result)
