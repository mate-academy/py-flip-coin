import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res = {}
    for i in range(11):
        res[i] = 0

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads = heads + 1

        res[heads] = res[heads] + 1

    for key in res:
        res[key] = res[key] / 10000 * 100

    return res


def make_graph() -> None:
    data = flip_coin()

    a_x = list(data.keys())
    a_y = list(data.values())

    plt.plot(a_x, a_y)

    # Scale graph height to value: 30
    plt.ylim(0, 30)

    plt.xlabel("Heads")
    plt.ylabel("%")
    plt.title("Gaussian")

    plt.show()

# make_graph()
