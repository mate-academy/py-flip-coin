import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}

    for _ in range(10000):
        total = 0
        for _ in range(10):
            if random.randint(0, 1):
                total += 1
        result[total] += 1

    for key, value in result.items():
        result[key] = value / 100
    return result


# def draw_gaussian_distribution_graph() -> None:
#     flip_coin_cases = flip_coin()
#     x_axis = [key for key in flip_coin_cases.keys()]
#     y_axis = [value for value in flip_coin_cases.values()]
#
#     plt.plot(x_axis, y_axis)
#     plt.yticks(range(0, 101, 10))
#     plt.xticks(range(0, 11, 1))
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
