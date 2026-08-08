import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    n_trials = 10000
    n_flips = 10
    results = {i: 0 for i in range(n_flips + 1)}

    for _ in range(n_trials):
        heads_count = sum(random.randint(0, 1) for _ in range(n_flips))
        results[heads_count] += 1

    return {k: (v / n_trials) * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph(data: dict) -> None:
    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_counts, percentages, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()
