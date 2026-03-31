import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_experiments = 10000
    flips_per_experiment = 10
    results = {heads: 0 for heads in range(flips_per_experiment + 1)}

    for _ in range(total_experiments):
        heads_count = 0
        for _ in range(flips_per_experiment):
            if random.randint(0, 1) == 1:
                heads_count += 1
        results[heads_count] += 1

    for heads in results:
        results[heads] = round((results[heads] / total_experiments) * 100, 2)
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    axis_x = results.keys()
    axis_y = [results[k] for k in axis_x]

    plt.plot(axis_x, axis_y, marker="o")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage%")
    plt.title("Distribution of Heads in 10 Flips")
    plt.grid(True)

    plt.show()


results = flip_coin()
draw_gaussian_distribution_graph(results)
