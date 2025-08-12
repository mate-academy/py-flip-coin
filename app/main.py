import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    outcomes_count = {number_of_heads: 0 for number_of_heads in range(11)}

    total_trials = 10000
    flips_per_trial = 10

    for trial in range(total_trials):
        heads_in_this_trial = sum(random.choice([0, 1])
                                  for flip in range(flips_per_trial))
        outcomes_count[heads_in_this_trial] += 1

    percentages = {
        number_of_heads: (count / total_trials) * 100
        for number_of_heads, count in outcomes_count.items()
    }
    return percentages


def draw_gaussian_distribution_graph(distribution: dict) -> None:

    x_axis = list(distribution.keys())
    y_axis = list(distribution.values())

    plt.figure(figsize=(8, 5))
    plt.bar(x_axis, y_axis, color="skyblue", edgecolor="black")
    plt.title("Distribution of Number of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    distribution = flip_coin()
    draw_gaussian_distribution_graph(distribution)
