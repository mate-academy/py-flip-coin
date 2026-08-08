from random import randrange
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, int]:
    results = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for _ in range(10_000):
        count_successes = 0
        for _ in range(10):
            count_successes += randrange(0, 2)
        results[count_successes] += 1
    for key in results:
        results[key] = round(results[key] / 10_000 * 100, 2)
    return results


def draw_gaussian_distribution_graph(distribution: dict[int, int]) -> None:
    plt.plot(distribution.keys(), distribution.values())
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.xlim(0, 10)
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)

    plt.show()
