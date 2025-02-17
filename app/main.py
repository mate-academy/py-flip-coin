import random
import matplotlib.pyplot as plt


def flip_coin(num_experiments: int = 10000, num_flips: int = 10) -> dict:
    results = {}

    for _ in range(num_experiments):
        heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads] = results.get(heads, 0) + 1

    percentages = {
        heads: (count / num_experiments) * 100
        for heads, count in results.items()
    }

    return {i: percentages.get(i, 0) for i in range(num_flips + 1)}


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.figure(figsize=(10, 6))

    heads = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads, percentages, "b-")

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.grid(True)
    plt.show()
