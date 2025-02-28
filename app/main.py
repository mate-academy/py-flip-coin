import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {x : 0 for x in range(11)}
    for _ in range(10000):
        results[sum(random.choices([0, 1], k=10))] += 1
    results = {x : y / 100 for x, y in results.items()}
    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.keys(), data.values(), color="r")
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.show()
