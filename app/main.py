import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    total_cases = 10000
    results = {i: 0.0 for i in range(11)}

    for _ in range(total_cases):
        heads_count = 0
        for _ in range(10):
            if random.choice([True, False]):
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / total_cases) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_counts, percentages)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.title("Gaussian Distribution - Coin Flip Simulation")
    plt.show()
