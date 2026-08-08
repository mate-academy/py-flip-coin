import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    result_dict = {}
    coin = ["head", "tail"]
    total_flips = 15000
    for _ in range(total_flips):
        count = 0
        for i in range(10):
            option = random.choice(coin)
            if option == "head":
                count += 1
        if count in result_dict:
            result_dict[count] += 1
        else:
            result_dict[count] = 1

    for key, value in result_dict.items():
        result_dict[key] = round((value / total_flips) * 100, 2)
    return dict(sorted(result_dict.items()))


# def draw_gaussian_distribution_graph(data: dict) -> None:
#     x_points = np.array(list(data.keys()))
#     y_points = np.array(list(data.values()))
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#
#     plt.xticks(np.arange(0, 11, 1))
#     plt.yticks(np.arange(0, 101, 10))
#
#     plt.plot(x_points, y_points, color="darkblue")
#     plt.xlim(0, 10)
#     plt.ylim(0, 100)
#     plt.show()
