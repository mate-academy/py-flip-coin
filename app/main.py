import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    result = defaultdict(float)

    for i in range(trials):
        heads_count = sum(random.choice([0, 1]) for a in range(10))
        result[heads_count] += 1

    for key in result:
        result[key] = round((result[key] / trials) * 100, 2)

    return dict(result)


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_heads_counts = sorted(data.keys())
    y_percentages = [data[k] for k in x_heads_counts]

    plt.ylim(bottom=0, top=100)
    plt.xlim(left=0, right=10)

    plt.xticks([i for i in range(11)])
    plt.yticks(range(0, 101, 10))

    plt.plot(x_heads_counts, y_percentages, marker="o", color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


result = flip_coin()
print(result)
draw_gaussian_distribution_graph(result)
