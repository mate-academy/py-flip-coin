import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads_count = sum(random.random() < 0.5 for _ in range(10))
        results[heads_count] += 1

    return {
        heads: (count / cases) * 100
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_counts, percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
