import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    chanse = {i: 0 for i in range(11)}

    for i in range(10000):
        heads_count = sum(random.choice([0, 1]) for y in range(10))
        chanse[heads_count] += 1

    for key in chanse:
        chanse[key] = round(chanse[key] / 10000 * 100, 2)

    return chanse


data = flip_coin()

x_key = list(data.keys())
y_value = list(data.values())

plt.plot(x_key, y_value)

plt.title("Gaussian distribution")
plt.xlabel("Head count")
plt.ylabel("Drop percentage %")
