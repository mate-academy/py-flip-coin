import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter


def flip_coin() -> dict:
    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    heads = 0
    for _ in range(10000):
        for i in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1
        results[heads] += 1
        heads = 0
    for i in range(11):
        results[i] = results[i] / 100
    return results


results = flip_coin()
xpoints = np.array(list(results))
ypoints = np.array(list(results.values()))

plt.plot(xpoints, ypoints)
plt.ylim(0, 100)
plt.xticks(range(0, 11))
plt.yticks(range(0, 101, 10))
plt.gca().yaxis.set_major_formatter(PercentFormatter())
plt.title("Percentege rate of heads in 10000 flip coins")
plt.xlabel("Heads in 10 flips")
plt.ylabel("Percentage of flips")
plt.show()
