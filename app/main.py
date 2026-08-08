import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    coin_flip_dict = {
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
        10: 0
    }

    for _ in range(10000):
        head_tail = {"head": 0, "tail": 0}
        for _ in range(10):
            res = random.choice(["head", "tail"])
            head_tail[res] += 1
        coin_flip_dict[head_tail["head"]] += 1

    new_dict = {}

    for key in coin_flip_dict:
        new_dict[key] = round((coin_flip_dict[key] / 10000) * 100, 2)

    return new_dict


def draw_gaussian_distribution_graph(coin_dictionary: dict) -> None:
    list1 = [key for key in coin_dictionary]
    list2 = [coin_dictionary[key] for key in coin_dictionary]

    x_cord = np.array(list1)
    y_cord = np.array(list2)

    plt.plot(x_cord, y_cord)

    plt.title("Coin Flip")
    plt.xlabel("Times Head Dropped")
    plt.ylabel("Percentage of head 10 times drop")

    plt.show()
