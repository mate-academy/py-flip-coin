import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    options = [1, 0]
    flip_dict = {i: 0 for i in range(11)}

    for toss in range(10000):
        heads = 0
        for attempt in range(10):
            result = random.choice(options)
            if result == 1:
                heads += 1
        flip_dict[heads] += 1

    for key, value in flip_dict.items():
        new_value = (value * 100) / 10000
        flip_dict[key] = round(new_value, 2)

    return flip_dict


def draw_gaussian_distribution_graph() -> None:
    flip = flip_coin()
    x_axis = list(flip.keys())
    y_axis = list(flip.values())
    plt.plot(x_axis, y_axis, marker="o")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()
