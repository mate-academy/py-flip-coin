import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {index: 0 for index in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    return {key: (value / total_cases) * 100 for key, value in results.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.plot(
        heads_counts,
        percentages,
        color="blue",
        marker="o",
        linestyle="-"
    )

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.grid(False)

    plt.show()
