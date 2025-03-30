from random import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
              8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        temp = 0
        for _ in range(10):
            flip = random()
            if flip > 0.500000000:
                temp += 1
        result[temp] += 1
    for key, value in result.items():
        result[key] = value / 100
    return result

#
# dict_after_flipping = flip_coin()
#
#
# def draw_gaussian_distribution_grap(dic: dict) -> None:
#     x_cord = [0]
#     y_cord = [0]
#     for key, value in dic.items():
#         x_cord.append(key)
#         y_cord.append(value)
#     plt.plot(x_cord, y_cord)
#     plt.ylim(0, 100)
#     plt.show()
#
#
# draw_gaussian_distribution_grap(dict_after_flipping)
