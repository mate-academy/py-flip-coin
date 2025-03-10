import random
import math
import matplotlib.pyplot as plt
import numpy as np

def flip_coin():
    result_dict = {i: 0 for i in range(11)}
    heads = 1
    count = 0

    for i in range(10000):
        for j in range(10):
            if random.randint(0,1) == heads:
                count += 1
        result_dict[count] += 1
        count = 0
    print(result_dict)

    total = sum(result_dict.values())
    percentages = {key: (value / total) * 100 for key, value in result_dict.items()}
    print([value for key, value in percentages.items()])
    return [value for key, value in percentages.items()]

print(flip_coin())

def draw_gaussian_distribution_graph():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array(flip_coin())

    plt.title("Gaussian distribution", loc='center')
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x, y)
    plt.ylim(0, 100)
    plt.show()

draw_gaussian_distribution_graph()