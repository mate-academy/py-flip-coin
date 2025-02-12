import random
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        heads = sum(random.randint(0, 1) for _ in range(num_flips))
        results[heads] += 1

    percentages = {
        key: (value / num_cases) * 100
        for key, value in results.items()
    }

    return percentages


def draw_gaussian_distribution_graph(results) -> None:
    heads = list(results.keys())
    percentages = list(results.values())

    plt.plot(heads, percentages, marker='o')

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
