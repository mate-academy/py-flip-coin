import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    stat_dict = {}
    for _ in range(10000):
        heads_quant = 0
        for _ in range(10):
            if random.randint(0, 1) == 0:
                heads_quant += 1
        stat_dict[heads_quant] = round(stat_dict.get(heads_quant, 0) + 0.01, 2)
    stat_dict = dict(sorted(stat_dict.items()))
    print(stat_dict)
    return stat_dict


# def draw_gaussian_distribution_graph(stat_dict: dict) -> None:
#     x_points = [key for key in stat_dict.keys()]
#     y_points = [key for key in stat_dict.values()]
#     plt.plot(x_points, y_points)
#     plt.show()


# stat_info = flip_coin()
# draw_gaussian_distribution_graph(stat_info)
