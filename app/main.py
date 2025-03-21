import random
import matplotlib.pyplot as plt


def flip_coin():
    results = {i: 0 for i in range(11)}

    for _ in range(10000):  # 10 000 спроб
        count_heads = sum(random.randint(0, 1) for _ in range(10))
        results[count_heads] += 1

    for key in results:
        results[key] = round(results[key] / 10000 * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: dict):
    plt.plot(
        list(results.keys()),
        list(results.values()),
        marker='o',
        linestyle='-',
        color='blue'
    )

    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of Heads in 10 Coin Flips (10,000 trials)")

    plt.xticks(range(11))
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.show()
