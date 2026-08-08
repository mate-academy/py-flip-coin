import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dict_result = {}
    for _ in range(0, 10000):
        heads = 0
        for _ in range(0, 10):
            if random.randint(0, 1) == 0:
                heads += 1
        if heads in dict_result:
            dict_result[heads] += 1
        else:
            dict_result[heads] = 1
    for key, value in dict_result.items():
        dict_result[key] = round((value / 10000) * 100, 2)
    sorted_dict = dict(sorted(dict_result.items()))
    return sorted_dict


def draw_gaussian_distribution_graph(value_chance: dict) -> None:
    x_coordinate = [key for key in value_chance.keys()]
    y_coordinate = [value for value in value_chance.values()]
    plt.plot(x_coordinate, y_coordinate)
    return plt.show()
