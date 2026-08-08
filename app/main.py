import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    random_chances = {
        0: 0.0,
        1: 0.0,
        2: 0.0,
        3: 0.0,
        4: 0.0,
        5: 0.0,
        6: 0.0,
        7: 0.0,
        8: 0.0,
        9: 0.0,
        10: 0.0,
    }
    coin = ["head", "tail"]
    for _ in range(10000):
        counter = 0
        for _ in range(0, 10):
            flip = random.choice(coin)
            if flip == "head":
                counter += 1
        random_chances[counter] += 1
    for key, value in random_chances.items():
        random_chances[key] = round((value / 10000) * 100, 2)
    return random_chances


x_points = []
y_points = []
for key, value in flip_coin().items():
    x_points.append(key)
    y_points.append(value)

plt.plot(np.array(x_points), np.array(y_points))
plt.title("Gaussian distribution graph")
plt.xlabel("numbers of possible heads dropped")
plt.ylabel(
    "percentage of how many that number of heads dropped out of all cases")
plt.show()
