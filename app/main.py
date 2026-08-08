import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10_000):
        heads = 0

        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1

        results[heads] += 1

    for i in results:
        results[i] = (results[i] / 10_000) * 100

    return results


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    plt.plot(list(distribution.keys()), list(distribution.values()))
    plt.xlabel("Heads count")
    plt.ylabel("Drop Percentage %")
    plt.title("Gaussian distribution")

    plt.ylim(0, 100)
    plt.xticks(range(11))

    plt.show()
