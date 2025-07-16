import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    list_of_results = []
    drop_percentage = {}

    for _ in range(10000):
        amount_of_heads = 0
        for _ in range(10):
            result = random.choice(coin)
            if result == "heads":
                amount_of_heads += 1
        list_of_results.append(amount_of_heads)

    for heads_count in range(11):
        drop_rate = ((list_of_results.count(heads_count) * 100)
                     / len(list_of_results))
        drop_percentage[heads_count] = round(drop_rate, 2)

    return drop_percentage


def draw_gaussian_distribution_graph() -> None:
    coin_flipping_results = flip_coin()

    plt.plot(
        list(coin_flipping_results.keys()),
        list(coin_flipping_results.values())
    )

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.ylim(0, 100)

    plt.show()


draw_gaussian_distribution_graph()
