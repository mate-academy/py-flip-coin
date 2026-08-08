from random import choice
# import numpy as np
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {0: 0,
              1: 0,
              2: 0,
              3: 0,
              4: 0,
              5: 0,
              6: 0,
              7: 0,
              8: 0,
              9: 0,
              10: 0}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            flip = choice([0, 1])
            if flip == 1:
                count += 1
        result[count] += 1
    for i in range(11):
        result[i] = round((result[i] / 10000) * 100, 2)

    # x = np.array(list(result.keys()))
    # y = np.array(list(result.values()))
    #
    # plt.plot(x, y)
    # plt.title("Gaussian distribution", loc='center')
    # plt.xlabel("Heads count")
    # plt.ylabel("Drop percentage %")
    #
    # plt.show()

    return result
