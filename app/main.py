import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    trials = 10000
    coin_flips = 10

    for _ in range(trials):
        heads_count = sum(random.randint(0, 1) for _ in range(coin_flips))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / trials) * 100

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values, marker="o", linestyle="-", color="b")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    distribution_data = flip_coin()
    print(distribution_data)
    draw_gaussian_distribution_graph(distribution_data)
