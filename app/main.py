import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    result_dict = {}

    for _ in range(10000):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        result_dict[heads_count] = result_dict.get(heads_count, 0) + 1
    total_cases = sum(result_dict.values())

    for num in result_dict:
        result_dict[num] = round(result_dict[num] * 100 / total_cases, 2)
    return dict(sorted(result_dict.items()))


# def draw_gaussian_distribution_graph(stats: dict) -> None:
#     x_point = []
#     y_point = []
#     for key, value in stats.items():
#         x_point.append(int(key))
#         y_point.append(value)
#     plt.plot(np.array(x_point), np.array(y_point))
#     plt.xlabel("Heads Count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
