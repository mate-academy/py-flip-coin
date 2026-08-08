# from matplotlib import pyplot

import random


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    result = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        num_heads = sum(random.randint(0, 1) for _ in range(num_flips))
        result[num_heads] += 1

    for key, value in result.items():
        result[key] = (value / num_trials) * 100

    return result


# def draw_gaussian_distribution_graph() -> None:
#
#     x_heads = list(flip_coin().keys())
#     y_percentages = list(flip_coin().values())
#
#     pyplot.plot(x_heads, y_percentages)
#     pyplot.xlabel("Heads count")
#     pyplot.ylabel("Drop percentage %")
#
#     pyplot.show()
#
#
# draw_gaussian_distribution_graph()
