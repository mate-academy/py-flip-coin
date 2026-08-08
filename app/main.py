from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0.0 for i in range(11)}
    for _ in range(15000):
        heads = 0
        for _ in range(10):
            flip = randint(0, 1)
            if flip == 1:
                heads += 1
        results[heads] += 1
    for key, value in results.items():
        results[key] = value / 15000 * 100

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_point = list(results.keys())
    y_point = list(results.values())
    plt.plot(x_point, y_point)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
