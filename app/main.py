import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10_000) -> dict:
    results = {i: 0 for i in range(0, 11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    results = {k: v * 100 / trials for k, v in results.items()}

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_points = list(results.keys())
    y_points = list(results.values())
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution", loc="left")
    plt.plot(x_points, y_points)

    #   plt.show()
