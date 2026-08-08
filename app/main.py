import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts = {i: 0 for i in range(11)}  # heads count 0–10

    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads] += 1

    return {
        heads: round(
            total / 10000 * 100, 2
        ) for heads, total in counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    plt.plot(list(data.keys()), list(data.values()), marker="o")
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
