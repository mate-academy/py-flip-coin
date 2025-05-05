import random
import matplotlib.pyplot as plt


def flip_coin(trials=10000, flips=10):
    heads_count = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        heads_count[heads] += 1

    for key in heads_count:
        heads_count[key] = round((heads_count[key] / trials) * 100, 2)

    return heads_count


def draw_gaussian_distribution_graph(distribution):
    x = list(distribution.keys())
    y = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color="blue", alpha=0.7)
    plt.title("Distribution of Heads in Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(x)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


result = flip_coin()
print(result)

draw_gaussian_distribution_graph(result)
