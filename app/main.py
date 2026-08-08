import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    ans = {}
    for _ in range(10000):
        counter_of_heads = 0
        for flip in range(10):
            if random.randint(1, 2) == 1:
                counter_of_heads += 1
        if counter_of_heads not in ans.keys():
            ans[counter_of_heads] = 1
        else:
            ans[counter_of_heads] += 1

    for key, value in ans.items():
        ans[key] = value / 100

    ans = dict(sorted(ans.items()))
    # x = ans.keys()
    # y = ans.values()
    #
    # plt.plot(x, y)
    # plt.ylim(0, 100)
    #
    # plt.show()
    # print(ans.values())
    return ans
