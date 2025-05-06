import numpy as np
import matplotlib.pyplot as plt


def flip_coin(trials=10000, flips=10):
    heads_count = [0] * (flips + 1)
    for _ in range(trials):
        heads = np.random.binomial(flips, 0.5)
        heads_count[heads] += 1

    percentages = {i: (count / trials) * 100 for i, count in enumerate(heads_count)}
    return percentages


def draw_gaussian_distribution_graph(data):
    x = list(data.keys())
    y = list(data.values())

    plt.plot(x, y, marker='o', color='blue')
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.xticks(x)
    plt.ylim(0, max(y) + 5)
    plt.grid()
    plt.show()


result = flip_coin()
print(result)

draw_gaussian_distribution_graph(result)
