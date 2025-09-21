import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_count = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            result = random.choice(["H", "T"])
            if result == "H":
                heads += 1
        heads_count[heads] += 1
    for key in heads_count:
        heads_count[key] = heads_count[key] / 10000 * 100
    return heads_count


toss_result = flip_coin()
heads_counts = list(toss_result.keys())
percentages = list(toss_result.values())


def draw_gaussian_distribution_graph(
        heads_counts: list[int],
        percentages: list[float]
) -> None:
    plt.bar(heads_counts, percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()

