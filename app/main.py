import random


import matplotlib.pyplot as plt


def flip_coin() -> dict:
    numbers = {x: 0 for x in range(11)}
    flip = ["orel", "reshka"]

    for i in range(10000):
        results = random.choices(flip, k=10)
        num_heads = results.count("orel")
        numbers[num_heads] += 1

    for key in numbers:
        numbers[key] = round(numbers[key] / 10000 * 100, 2)

    return numbers


flip = flip_coin()

x_coordinate = list(flip.keys())
y_coordinate = list(flip.values())

plt.plot(x_coordinate, y_coordinate)
plt.xlabel("Number of series")
plt.ylabel("Number of drop percentage")
plt.show()
