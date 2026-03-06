import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    heads_counts = {i: 0 for i in range(11)}
    final_result = {}

    for i in range(10000):
        count = 0
        for _ in range(10):
            count += random.randint(0, 1)
        heads_counts[count] += 1

    for i in range(11):
        final_result[i] = round((heads_counts[i] / 10000) * 100, 2)

    return final_result


def draw_gaussian_distribution_graph(ls: dict[int, float]) -> None:
    plt.plot(ls.keys(), ls.values(), marker="o", linestyle='-')
    plt.title("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")

    plt.ylim(0, 100)
    plt.grid(True, alpha=0.3)
    plt.show()
