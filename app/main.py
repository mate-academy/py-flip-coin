import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def flip_coin() -> dict:
    results = {i: 0.0 for i in range(11)}
    for _ in range(10000):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1
    for count in results:
        results[count] = round(results[count] / 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    coins_flips = flip_coin()
    x_points = list(range(11))
    y_points = [percentage for percentage in coins_flips.values()]

    plt.plot(x_points, y_points)
    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.gca().yaxis.set_major_locator(MultipleLocator(10))
    plt.gca().yaxis.set_minor_locator(MultipleLocator(5))
    plt.gca().xaxis.set_major_locator(MultipleLocator(1))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
