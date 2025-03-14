import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    coin_flip = {i: 0.0 for i in range(11)}

    for i in range(100000):
        heads_count = 0
        for index in range(10):
            heads_tails = random.randint(0, 1)
            if heads_tails == 1:
                heads_count += 1

        coin_flip[heads_count] += 1

    for key in coin_flip:
        coin_flip[key] = round((coin_flip[key] / 100000) * 100, 2)

    return coin_flip


def draw_gaussian_distribution_graph(coin_flip: dict) -> None:

    x_axis = [index for index in coin_flip]
    y_axis = [coin_flip[index] for index in coin_flip]

    plt.plot(x_axis, y_axis)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
