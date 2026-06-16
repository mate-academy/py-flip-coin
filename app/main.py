import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_times = 10
    flip_cases = 10000
    result = {i: 0 for i in range(11)}
    for _ in range(flip_cases):
        flip_result = sum(random.choice([0, 1]) for _ in range(flip_times))
        result[flip_result] += 1
    for key in result:
        result[key] = (result[key] / flip_cases) * 100

    return result


# def draw_gaussian_distribution_graph() -> None:
#     data = flip_coin()
#     x_values = data.keys()
#     y_values = data.values()
#
#     plt.plot(x_values, y_values)
#     plt.ylim(0, 100)
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.title("Gaussian distribution")
#     plt.show()
