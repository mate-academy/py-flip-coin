import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts = {n: 0 for n in range(11)}
    coin = ["heads", "tails"]
    for i in range(10000):
        shot = random.choices(coin, k=10)
        number_of_heads = shot.count("heads")
        counts[number_of_heads] += 1
    percentage_counts = {n: counts[n] / 10000 * 100 for n in range(11)}
    return percentage_counts


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_axis = list(data.keys())
    y_axis = list(data.values())
    plt.plot(x_axis, y_axis)
    plt.show()
