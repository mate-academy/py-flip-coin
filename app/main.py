import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    flips_per_trial = 10
    results = {i: 0 for i in range(flips_per_trial + 1)}
    for _ in range(trials):
        count = 0
        for _ in range(flips_per_trial):
            flip = random.choice([0, 1])
            if flip == 1:
                count += 1
        results[count] += 1
    percentages = {
        heads: round(count / trials * 100, 2) for heads,
        count in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    x_keys = list(distribution.keys())
    y_values = list(distribution.values())
    plt.plot(x_keys, y_values, marker="o")
    plt.show()
