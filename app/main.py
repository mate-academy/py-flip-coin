import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results: dict[int, float] = {i: 0 for i in range(11)}
    trials = 10000
    for _ in range(trials):
        choice = sum(random.randint(0, 1) for _ in range(10))
        results[choice] += 1
    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    heads_count = list(results.keys())
    percentage = list(results.values())
    plt.plot(heads_count, percentage)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    plt.show()
