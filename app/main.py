import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = 0
        for __ in range(10):
            if random.choice([0, 1]):
                heads += 1
        results[heads] += 1

    for i in results:
        results[i] = round(results[i] / trials * 100, 2)

    return results


def graw_gaussian_distribution_graph() -> None:
    x_points = [x for x in range(11)]
    y_points = [flip_coin()[i] for i in range(11)]

    plt.plot(x_points, y_points)
    plt.show()
