"""import matplotlib
import numpy as np
import matplotlib.pyplot as plt"""

import random

# matplotlib.use('TkAgg')


def flip_coin() -> dict:
    percentage_dict = {}

    for _ in range(10000):

        random_number = 0
        for _ in range(10):
            random_number += random.randint(0, 1)
        if random_number in percentage_dict:
            percentage_dict[random_number] += 1
            continue
        percentage_dict[random_number] = 1

    for key, value in percentage_dict.items():
        percentage_dict[key] = value / 10000 * 100

    return percentage_dict


"""statistic_dict = flip_coin()

# Sort the data by key
sorted_items = sorted(statistic_dict.items())
x, y = zip(*sorted_items)  # Unpack keys and values

# Convert to numpy arrays
x = np.array(x)
y = np.array(y)

plt.plot(x, y, marker='o', linestyle='-', color='b')

plt.axhline(y=100, color='r', linestyle='--', label='Загальна межа 100%')
plt.xlabel("Heads count")
plt.ylabel("Drop percentages (%)")
plt.title("Distribution of Heads Count in 10 Coin Flips")


plt.grid(True)
plt.show()"""
