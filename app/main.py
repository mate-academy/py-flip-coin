import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            side_of_coin = random.randint(0, 1)
            if side_of_coin == 1:
                heads += 1
        result[heads] += 1

    for heads in result:
        result[heads] = (result[heads] / 10000) * 100

    return result


def draw_gaussian_distribution_graph() -> dict:
    x = [1, 2, 3, 4, 5]
    y = [10, 3, 8, 12, 5]

    plt.plot(x, y)
    plt.title("")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


draw_gaussian_distribution_graph()
print(flip_coin())
