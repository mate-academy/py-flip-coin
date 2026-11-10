import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    return {
        heads_count: round((count / trials) * 100, 2)
        for heads_count, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_counts, percentages, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
