import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["H", "T"]
    dict_counter = {}
    for _ in range(10000):
        count = 0
        for num in range(10):
            if random.choice(coin) == "H":
                count += 1
        if count not in dict_counter:
            dict_counter[count] = 0
        dict_counter[count] += 1
    for key in dict_counter.keys():
        dict_counter[key] /= 100
    return dict_counter


def draw_gaussian_distribution_graph() -> None:
    dict_counter = flip_coin()
    x_point = list(dict_counter.keys())
    y_point = list(dict_counter.values())

    plt.plot(x_point, y_point)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
