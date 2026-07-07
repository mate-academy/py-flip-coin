import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["Heads", "Tails"]
    count_heads_of_ten_flips = {0: 0,
                                1: 0,
                                2: 0,
                                3: 0,
                                4: 0,
                                5: 0,
                                6: 0,
                                7: 0,
                                8: 0,
                                9: 0,
                                10: 0}
    for _ in range(10000):
        result_of_flip = []
        for i in range(10):
            result_of_flip.append(random.choice(coin))
        count_heads_of_ten_flips[result_of_flip.count("Heads")] += 1
    for key, value in count_heads_of_ten_flips.items():
        count_heads_of_ten_flips[key] = value / 100
    return count_heads_of_ten_flips


def draw_gaussian_distribution_graph(count_heads_of_ten_flips: dict) -> None:
    xpoints = count_heads_of_ten_flips.keys()
    ypoints = count_heads_of_ten_flips.values()
    plt.plot(xpoints, ypoints)
    plt.show()
