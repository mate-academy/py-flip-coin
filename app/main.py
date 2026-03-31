import matplotlib.pyplot as plt
import numpy as np
import random


def flip_once() -> bool:
    """
        Chooses randomly True or False
        True means heads, Fals, not heads
    """
    return random.choice([True, False])


def flip_coin() -> dict:
    amount_of_tens = 10_000

    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }

    for _ in range(amount_of_tens):
        heads = 0
        for __ in range(10):
            if flip_once():
                heads += 1
        results[heads] += 1

    for result, amount in results.items():
        results[result] = round(amount / amount_of_tens * 100, 2)

    return results


results = flip_coin()


def draw_line() -> None:
    x_points = np.array(list(results.keys()))
    y_points = np.array(list(results.values()))

    plt.plot(x_points, y_points)

    plt.title("Coin flips experiment")
    plt.xlabel("Times Heads have dropped in ten flips")
    plt.ylabel("Percentage of this happening")

    plt.show()


draw_line()
