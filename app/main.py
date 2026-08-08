"""Module for simulating coin flips and calculating head frequencies."""
import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    """
    Simulate 10000 coin flips and calculate head frequency distribution.

    Returns:
        dict: A dictionary with keys 0-10 representing the number of heads
        in 10 flips, and values representing the frequency as a percentage.
    """
    head_frequency = {i: 0 for i in range(11)}
    for _ in range(10000):
        head_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                head_count += 1
        head_frequency[head_count] += 1
    for head_results in range(11):
        head_frequency[head_results] = head_frequency[head_results] / 100
    return head_frequency


def draw_gaussian_distribution_graph() -> None:
    """
    Draw a Gaussian distribution graph for the head frequencies of coin flips.
    """
    head_frequencies = flip_coin()
    x_val = np.array(list(head_frequencies.keys()))
    y_val = np.array(list(head_frequencies.values()))

    plt.bar(x_val, y_val, color="blue", alpha=0.7)
    plt.title("Head Frequency Distribution for 10 Coin Flips")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Frequency (%)")
    plt.xticks(x_val)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
