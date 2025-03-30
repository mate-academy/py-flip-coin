import random
# import matplotlib
# import matplotlib.pyplot


def flip_coin(number: int = 10000) -> dict:
    array = [[random.randint(0, 1) for _ in range(10)].count(0)
             for _ in range(number)]
    return {i: round((array.count(i) / 100), 2) for i in set(array)}


# def draw_gaussian_distribution_graph() -> None:
#     axis_x = flip_coin().keys()
#     axis_y = flip_coin().values()
#     matplotlib.use("TkAgg")
#     matplotlib.pyplot.plot(axis_x, axis_y)
#     matplotlib.pyplot.show()
