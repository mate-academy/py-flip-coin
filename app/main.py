import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10_000):
        heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / 10_000 * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    xpoints = list(results.keys())
    ypoints = list(results.values())
    plt.plot(xpoints, ypoints)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
