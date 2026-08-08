import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(total_cases):
        heads_count = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / total_cases * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    x_values = list(results.keys())
    y_values = list(results.values())

    plt.plot(x_values, y_values)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
