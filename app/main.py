import random
# import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[str, float]:
    raw_heads_dict = {_: 0 for _ in range(11)}
    for _ in range(10000):
        number_of_heads_in_ten_flips = 0
        for _ in range(10):
            number_of_heads_in_ten_flips += random.choice([0, 1])
        raw_heads_dict[number_of_heads_in_ten_flips] += 1

    percent_heads_dict = {_: round(raw_heads_dict[_] / 100, 2)
                          for _ in raw_heads_dict}

    return percent_heads_dict
#
#
# def draw_gaussian_distribution_graph(func: Callable) -> None:
#     heads = func()
#     x_axis = heads.keys()
#     y_axis = heads.values()
#     plt.plot(x_axis, y_axis)
#     plt.title("Coin flip distribution")
#     plt.xlabel("Heads Count (times per 10 flips)")
#     plt.ylabel("Drop percentage, %")
#     plt.show()
