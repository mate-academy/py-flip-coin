import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    result_10k_times = {num: 0 for num in range(11)}
    for _ in range(10000):
        result_10_flips = {
            "heads": 0,
            "tails": 0
        }
        for _ in range(10):
            result = random.choice(("heads", "tails"))
            result_10_flips[result] += 1
        result = result_10_flips["heads"]
        result_10k_times[result] += 1
    return {num: round(res / 100, 2) for num, res in result_10k_times.items()}


def draw_gaussian_distribution_graph() -> None:
    result_10k_times = flip_coin()
    percentage = np.array([chance for chance in result_10k_times.values()])
    plt.plot(percentage)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.ylim(0, 100)
    plt.show()
