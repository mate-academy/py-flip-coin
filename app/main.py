import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(cases):
        heads_count = 0
        for _ in range(10):
            heads_count += random.randint(0, 1)

        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / cases * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_values = list(data.keys())
    y_values = list(data.values())
    plt.figure(figsize=(8, 5))
    plt.bar(x_values, y_values)

    plt.title("Coin Flip Distribution(10 flips)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage(%)")
    plt.xticks(range(11))
    plt.grid(axis="y")

    plt.show()


draw_gaussian_distribution_graph()
