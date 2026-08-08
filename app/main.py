import random

from matplotlib import pyplot as plt


def flip_coin(num_cases: int = 10000, flips_per_case: int = 10) -> dict:
    result = {i: 0 for i in range(flips_per_case + 1)}
    for i in range(num_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(flips_per_case))
        result[heads_count] += 1
    percentage = {k: round(v / num_cases * 100, 2) for k, v in result.items()}
    return percentage


data = flip_coin()
x_list = [k for k in data.keys()]
y_list = [v for v in data.values()]

plt.xlabel("Heads count")
plt.ylabel("Drop of percentage")
plt.title("Gaussian Distribution")
plt.xlim(0, 10)
plt.ylim(0, 100)

plt.plot(x_list, y_list)
plt.show()
