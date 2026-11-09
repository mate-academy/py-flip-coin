import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    result = {i: 0 for i in range(11)}
    for i in range(10000):
        count_of_heads = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                count_of_heads += 1
        result[count_of_heads] += 1
    for key, value in result.items():
        result[key] = value / 10000 * 100
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    plt.plot(result.keys(), result.values())
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of experiments (%)")
    plt.title("Gaussian distribution")
    plt.show()
