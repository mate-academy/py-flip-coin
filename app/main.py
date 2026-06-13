import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {}
    coin = ["Heads", "Tails"]
    for flip in range(10000):
        heads_count = 0
        for i in range(10):
            heads_or_tails = random.choice(coin)
            if heads_or_tails == "Heads":
                heads_count += 1

        if heads_count in results:
            results[heads_count] += 1
        else:
            results[heads_count] = 1

    for key, value in results.items():
        value = round(value / 10000 * 100, 2)
        results[key] = value

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_graph = sorted(list(results.keys()))
    y_graph = [results[key] for key in x_graph]

    plt.plot(x_graph, y_graph)
    plt.show()
