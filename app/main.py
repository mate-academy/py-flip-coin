import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    # Initialize dictionary with keys 0-10 set to 0
    results = {i: 0 for i in range(11)}
    trials = 10000
    flips_per_trial = 10

    for _ in range(trials):
        # Simulate 10 flips: 1 is heads, 0 is tails
        heads_count = sum(random.randint(0, 1) for _ in range(flips_per_trial))
        results[heads_count] += 1

    # Convert counts to percentages
    for heads in results:
        results[heads] = (results[heads] / trials) * 100

    return results


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    # Extract keys (number of heads) and values (percentages)
    x_values = list(data.keys())
    y_values = list(data.values())

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker="o", linestyle="-", color="b")

    # Adding Labels and Title
    plt.title("Coin Flip Distribution (10,000 cases)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")

    # Setting axis limits and ticks for clarity
    plt.xticks(range(11))
    plt.grid(True, linestyle="--", alpha=0.7)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    distribution_data = flip_coin()
    print(distribution_data)
    draw_gaussian_distribution_graph(distribution_data)
