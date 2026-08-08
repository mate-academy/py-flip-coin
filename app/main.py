import random

from matplotlib import pyplot as plt


def flip_coin(trials: int = 10000) -> dict[int, float]:
    results: dict[int, int] = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads_count = 0
        for _ in range(10):
            toss = random.randint(0, 1)
            if toss == 1:
                heads_count += 1
        results[heads_count] += 1

    percentages: dict[int, float] = {}

    for heads_count, count in results.items():
        percentages[heads_count] = count / trials * 100

    return percentages


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    x_values = sorted(data.keys())
    y_values = [data[k] for k in x_values]

    plt.plot(x_values, y_values)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
