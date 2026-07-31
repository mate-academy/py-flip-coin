import matplotlib.pyplot as plt
import numpy as np
import random
import copy as copy


def flip_coin() -> dict:
    count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    result = copy.deepcopy(count)
    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        count[heads] += 1
    for i in count.items():
        result[i[0]] = round((i[1] / 10000) * 100, 2)
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(np.array(list(data.keys())), np.array(list(data.values())))
    plt.title("Gaussian Distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 10))
    plt.xlim(0, 10)
    plt.xticks(np.arange(0, 11, 1))
    plt.show()
