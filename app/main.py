import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_sides = ["head", "tails"]
    counts = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            action = random.choice(coin_sides)
            if action == "head":
                heads += 1
        counts[heads] += 1
    result = {k: round(v / 10000 * 100, 2) for k, v in counts.items()}
    return result


data = flip_coin()
x_coord = list(data.keys())
y_coord = list(data.values())
plt.bar(x_coord, y_coord)
plt.show()
