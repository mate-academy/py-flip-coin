import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    """
    Simulates flipping a coin 10 times for at least 10000 cases.
    Returns a dictionary with the percentage of times each number of
    heads occurred.
    """
    num_cases = 10000
    num_flips = 10
    heads_count = {i: 0 for i in range(num_flips + 1)}

    # Run simulations
    for _ in range(num_cases):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        heads_count[heads] += 1

    # Convert counts to percentages
    heads_percentage = {
        k: round((v / num_cases) * 100, 2)
        for k, v in heads_count.items()
    }

    return heads_percentage


def draw_gaussian_distribution_graph() -> None:
    """
    Draws a graph showing the Gaussian distribution of coin flip results.
    """
    # Get the simulation data
    data = flip_coin()

    # Extract keys and values for plotting
    x_values = list(data.keys())
    y_values = list(data.values())

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, "b-", linewidth=2)

    # Set labels and title
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    # Set axis limits
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    # Add grid for better readability
    plt.grid(True, alpha=0.3)

    # Display the plot
    plt.tight_layout()
    plt.show()


# Test the functions
if __name__ == "__main__":
    print(flip_coin())
    print("\nDrawing graph...")
    draw_gaussian_distribution_graph()
