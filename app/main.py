import random
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[num_heads] += 1

    percentages = {
        key: (value / num_trials) * 100
        for key, value in results.items()
    }
    # draw_gaussian_distribution_graph(percentages)
    return percentages


def draw_gaussian_distribution_graph(points: dict) -> None:
    plt.plot(list(points.keys()), list(points.values()))
    plt.show()
