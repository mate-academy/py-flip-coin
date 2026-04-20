
import random

# Extra logic:
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dict_ = {index: 0 for index in range(11)}
    for i in range(10000):
        key = sum(random.choice([0, 1]) for i in range(10))
        dict_[key] += 1
    for i in range(len(dict_)):
        dict_[i] /= 100
    # Extra logic:
    # plt.title("Gaussian distribution")
    # plt.xlabel("Heads count")
    # plt.ylabel("Drop percentage %")
    # plt.plot(dict_.keys(), (dict_.values()))
    # plt.show()
    return dict_
