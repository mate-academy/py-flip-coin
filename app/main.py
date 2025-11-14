import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads = 1
    tails = 2
    total_runs = 10000
    counters = {a: 0 for a in range(0, 11)}
    chance_dict = {a: 0.0 for a in range(0, 11)}
    for _ in range(total_runs):
        list_of_chances = []
        for _ in range(10):
            list_of_chances.append(random.randint(heads, tails))
        count = list_of_chances.count(heads)
        counters[count] += 1

    for times in range(11):
        chance_dict[times] = counters[times] / total_runs * 100

    x_coordinate = np.array([key for key in chance_dict])
    y_coordinate = np.array([value for value in chance_dict.values()])

    plt.plot(x_coordinate, y_coordinate)

    plt.title("Chances of Flipping Coin and Getting Heads")
    plt.xlabel("Number of Heads in flipping 10 times")
    plt.ylabel("probability in %")

    plt.savefig("plot.png")

    return chance_dict
