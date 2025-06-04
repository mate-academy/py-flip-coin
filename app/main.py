import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    results = {i: 0 for i in range(11)}
    experiments = 10000

    for _ in range(experiments):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    percent_results = {}
    for key in results:
        percent_results[key] = round((results[key] / experiments) * 100, 2)

    return percent_results


def draw_gaussian_distribution_graph(results: dict[int, float]) -> None:
    x = list(results.keys())
    y = list(results.values())
    plt.plot(x, y, marker='o')
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.title("Distribution of heads in 10 coin flips")
    plt.grid(True)
    plt.show()
