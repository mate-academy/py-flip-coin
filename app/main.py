import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin(count_cases: int = 10000, count_flips: int = 10) -> dict:
    result = {i: 0 for i in range(count_flips + 1)}
    for _ in range(count_cases):
        heads = sum(random.randint(0, 1) for _ in range(count_flips))
        result[heads] += 1
    return {
        key: (value / count_cases * 100) for key, value in result.items()
    }

# def draw_gaussian_distribution_graph() -> None:
#     x_line = np.array(flip_coin().keys())
#     y_line = np.array(flip_coin().values())
#     plt.plot(x_line, y_line)
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
