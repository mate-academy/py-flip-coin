import random
import matplotlib.pyplot as plt


def generate_flip() -> int:
    coin_choices = [1, 0]
    return random.choice(coin_choices)


def simulate_10_flips() -> int:
    ten_flips = 0
    for flip in range(10):
        flipped_coin = generate_flip()
        if flipped_coin == 1:
            ten_flips += 1
    return ten_flips


def flip_coin() -> dict:
    result_flips = dict.fromkeys(range(0, 11), 0)
    for _ in range(10000):
        counts = simulate_10_flips()
        result_flips[counts] += 1

    for key in result_flips:
        result_flips[key] = round(result_flips[key] / 100, 2)

    return result_flips


import matplotlib.pyplot as plt


def draw_gaussian_distribution_graph():
    data = flip_coin()
    x = list(data.keys())
    y = list(data.values())

    plt.plot(x, y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()