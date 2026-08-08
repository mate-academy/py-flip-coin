import random
import numpy as np
import matplotlib.pyplot as plt


def get_ten_flips() -> int:
    """
    Simulate 10 coin flips and return the number of heads.
    """
    coin_flip = ["head", "tail"]
    count = 0
    for _ in range(10):
        if random.choice(coin_flip) == "head":
            count += 1
    return count


def flip_coin(tries: int = 10000) -> dict:
    """
    Run multiple experiments of 10 coin flips and return
    a distribution of heads count in percentages.

    Args:
        tries: Number of simulation runs (default 10,000)

    Returns:
        dict: keys 0–10 (heads count), values — percentage occurrence.
    """
    results = {i: 0 for i in range(11)}

    for _ in range(tries):
        heads = get_ten_flips()
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / tries * 100, 2)

    return results


data = dict(sorted(flip_coin().items()))

data_x = list(data.keys())
data_y = list(data.values())

x_point = np.array(data_x)
y_point = np.array(data_y)

plt.plot(x_point, y_point)

plt.title("Gaussian distribution")
plt.xlabel("Heads count")
plt.ylabel("Drop percentage %")

plt.ylim(0, 100)
plt.yticks(range(0, 101, 10))
plt.xlim(0, 10)
plt.xticks(range(0, 11, 1))

plt.show()
