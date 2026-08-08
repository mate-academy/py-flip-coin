import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        throws = [random.choice(["H", "T"]) for _ in range(10)]
        heads = throws.count("H")
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / 10000 * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_axis = list(results.keys())
    y_axis = list(results.values())

    plt.plot(x_axis, y_axis)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.ylim(0, 100)
    plt.show()
