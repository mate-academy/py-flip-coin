from random import randint
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    gauss = {i: 0 for i in range(11)}

    for i in range(trials + 1):
        gauss[sum([randint(0, 1) for _ in range(10)])] += 1

    gauss = {key: val / trials * 100 for key, val in gauss.items()}

    return gauss


gauss_distribution = flip_coin()
x_axis = gauss_distribution.keys()
y_axis = gauss_distribution.values()

plt.plot(x_axis, y_axis)
plt.xlabel("N of heads")
plt.ylabel("% of flips")


if __name__ == "__main__":
    plt.show()
