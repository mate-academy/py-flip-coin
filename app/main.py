import numpy as np
import matplotlib.pyplot as plt
import random


def flip_coin() -> dict[int, int]:
    result = {i: 0 for i in range(11)}
    total_experiments = 10000

    for _ in range(total_experiments):
        head_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                head_count += 1
        result[head_count] += 1

    for key in result:
        result[key] = round(result[key] / total_experiments * 100, 2)
    return result


result = flip_coin()
x_x = list(result.keys())
y_y = list(result.values())


plt.plot(x_x, y_y)
x_x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_y = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.title("Gaussian distribution")
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")

plt.show()
