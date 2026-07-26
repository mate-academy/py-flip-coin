import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(10000):
        heads_count = 0
        for i in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                heads_count += 1

        result[heads_count] += 1

    for key in result:
        result[key] /= 100

    return result


def draw_gaussian_distribution_graph(
        distribution: dict[int, float]
) -> None:
    heads_counts = list(distribution.keys())
    percentages = list(distribution.values())

    plt.plot(heads_counts, percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
