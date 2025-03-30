import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for i in range(11):
        result[i] = 0
    for i in range(10001):
        head_count = 0
        for flip in range(10):
            if random.choice([0, 1]) == 1:
                head_count += 1
        result[head_count] += 1
    for key in result:
        result[key] = round(result[key] / 100, 2)
    return result


# def draw_gaussian_distribution_graph() -> None:
#     plot_data = flip_coin()
#     x_axis = list(plot_data.keys())
#     y_axis = list(plot_data.values())
#     y_min = 0
#     y_max = 100
#
#     plt.plot(x_axis, y_axis, color="red", linewidth=1)
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.ylim(y_min, y_max)
#     plt.show()
