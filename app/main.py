import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coins = ["heads", "tails"]
    results = []

    for _ in range(10000):
        heads_count = 0
        for flip in range(1, 11):
            item = random.choice(coins)
            if item == "heads":
                heads_count += 1
        results.append(heads_count)

    counts = {i: 0 for i in range(11)}
    for key in counts:
        count = results.count(key)
        value = (count / 10000) * 100
        counts[key] = value

    return counts


def draw_gaussian_distribution_graph(counts: dict) -> None:
    axis_x = list(counts.keys())
    axis_y = list(counts.values())

    plt.plot(axis_x, axis_y, marker="o")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Percentage (%)")
    plt.show()
