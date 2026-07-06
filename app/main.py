import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice([0, 1]) == 1:
                heads += 1
        results[heads] += 1

    for key in results:
        results[key] = round((results[key] / 10000) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    plt.bar(data.keys(), data.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


draw_gaussian_distribution_graph()
