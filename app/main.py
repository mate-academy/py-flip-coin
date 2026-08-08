import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> dict:
    """
    Conducts 10,000 cases of flipping a coin 10 times.
    Returns a dictionary of percentages for each outcome (0-10 heads).
    """
    counts = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        counts[heads] += 1

    # Convert counts to percentages
    percentages = {k: (v / trials) * 100 for k, v in counts.items()}
    return percentages


def draw_gaussian_distribution_graph(data: dict) -> None:
    """
    Draws a bar graph showing the distribution of heads.
    """
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(x_values, y_values, color="skyblue", edgecolor="black", alpha=0.7)

    # Adding titles and labels
    plt.title(
        "Distribution of Heads in 10 Coin Flips (10,000 Trials)",
        fontsize=14
    )
    plt.xlabel("Number of Heads", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)

    # Ensure all numbers 0-10 show up on the x-axis
    plt.xticks(range(11))

    # Display the graph
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph(results)
