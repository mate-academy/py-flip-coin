import random

# import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    dict_cases = {i: 0 for i in range(11)}
    sum_t = sum(random.randint(0, 1) for _ in range(10))
    for i in range(cases):
        sum_t = sum(random.randint(0, 1) for _ in range(10))
        dict_cases[sum_t] += 1
    return {i: round(((dict_cases[i] / cases) * 100), 2) for i in dict_cases}

#
# def draw_gaussian_distribution_graph() -> None:
#     x_keys = list(flip_coin().keys())
#     y_percent = list(flip_coin().values())
#     plt.plot(x_keys, y_percent)
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.ylim([0, 100])
#     plt.xlim([0, 10])
#     plt.show()
