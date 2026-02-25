import matplotlib.pyplot as plt
from main import flip_coin


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    heads_counts = list(distribution.keys())
    percentages = list(distribution.values())

    plt.plot(heads_counts, percentages)
    plt.xlabel("Number of Heads (out of 10)")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution (10 flips)")
    plt.show()