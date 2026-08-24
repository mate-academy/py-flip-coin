import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    ndict = {}
    for _ in range(10000):
        head = 0
        for _ in range(10):
            if random.randint(0, 1):
                head += 1
        ndict[head] = ndict.get(head, 0) + 1
    another_dict = {
        key: round((val / 10000) * 100, 2)
        for key, val in {
            key: val for key, val in sorted(ndict.items(), key=lambda x: x[0])
        }.items()
    }
    return another_dict


result = flip_coin()

x_coordinate = np.array(list(result.keys()))
y_coordinate = np.array(list(result.values()))

plt.plot(x_coordinate, y_coordinate)
plt.show()
