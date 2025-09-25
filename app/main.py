import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_counts = {}

    for _ in range(10000):
        bird = 0
        for _ in range(10):
            result = random.choice([True, False])
            if result:
                bird += 1
        if bird in heads_counts:
            heads_counts[bird] += 1
        else :
            heads_counts[bird] = 1
    for i, x in heads_counts.items():
        heads_counts[i] = x / 10000 * 100
    return heads_counts


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    birds = list(result.keys())
    percent = list(result.values())
    plt.bar(birds, percent)
    plt.xlabel("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.title("Heads count")
    plt.show()