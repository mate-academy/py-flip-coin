import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:

    data_collector = {i: 0 for i in range(11)}
    coin_side = ["heads", "tails"]

    for _ in range(10000):
        flips = random.choices(coin_side, k=10)
        res = flips.count("heads")
        data_collector[res] += 10 / 1000

    return {key: round(value, 2) for key, value in data_collector.items()}


def draw_gaussian_distribution_graph(input_value: dict) -> None:
    res = flip_coin()
    x_coordinates = list(res.keys())
    y_coordinates = list(res.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(x_coordinates, y_coordinates)
    plt.show()


print(draw_gaussian_distribution_graph(flip_coin()))
