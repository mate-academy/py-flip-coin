import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 100_000, flips: int = 10) -> dict:
    counts = {heads: 0 for heads in range(flips + 1)}

    for _ in range(cases):
        heads = sum(random.random() < 0.5 for _ in range(flips))
        counts[heads] += 1
    return {
        heads: round(count / cases * 100, 2)
        for heads, count in counts.items()
    }


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
        color="blue",
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(11))
    plt.show()


draw_gaussian_distribution_graph()
