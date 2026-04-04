import random
# from typing import Callable
#
# from matplotlib import pyplot


def flip_coin(nr_cases: int = 10000, nr_of_flips: int = 10) -> dict:

    result = {num: 0 for num in range(0, 11)}

    for case in range(nr_cases):
        nr_of_heads_out_of_10 = 0
        for num in range(nr_of_flips):
            heads_or_tails = random.randint(0, heads := 1)
            if heads_or_tails == heads:
                nr_of_heads_out_of_10 += 1

        result[nr_of_heads_out_of_10] += 1

    return {key: value / nr_cases * 100 for key, value in result.items()}


"""
EXTRA TASK
def draw_gaussian_distribution_graph(func: Callable) -> None:
    result_dict = func()
    x_points = [key for key in result_dict.keys()]
    y_points = [value for value in result_dict.values()]

    pyplot.plot(
        x_points,
        y_points,
        "h-.m",
        ms=10,
        mec="k",
        mfc="#00CED1"
    )

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.xlim(0, 10)
    pyplot.ylim(0, 100)
    pyplot.show()
"""
