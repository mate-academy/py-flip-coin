import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {coin: 0 for coin in range(11)}
    for chance in range(10000):
        eagle_monet = 0
        for coin in range(10):
            if random.choice(["eagle", "tails"]) == "eagle":
                eagle_monet += 1
        result[eagle_monet] += 1

    for key, values in result.items():
        result[key] = values / 100 * 1

    return result


def draw_gaussian_distribution_graph(x_point: list, y_point: list) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(x_point, y_point, 100, color="r")
    plt.show()
