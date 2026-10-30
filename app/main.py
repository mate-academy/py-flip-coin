from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    cases_count = 10000
    results = {heads: 0 for heads in range(11)}

    for _ in range(cases_count):
        heads_count = sum(randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    return {
        heads: round(count * 100 / cases_count, 2)
        for heads, count in results.items()
    }


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
    plt.show()
