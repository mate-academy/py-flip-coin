import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    counts = {heads_count: 0 for heads_count in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads] += 1

    return {
        heads: round((count / trials) * 100, 2)
        for heads, count in counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    heads_points = list(distribution.keys())
    percentage_points = list(distribution.values())

    plt.plot(heads_points, percentage_points, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()
