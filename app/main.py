import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    dic = {k: 0 for k in range(0, 11)}

    for _ in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        dic[heads] += 1
    for _ in dic.keys():
        dic[_] = round(dic[_] / 10000 * 100, 2)
    return dic


def draw_gaussian_distribution_grap() -> None:

    data = flip_coin()
    plt.plot(list(data.keys()), list(data.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Winnings")
    plt.ylabel("Drop percentage %")
    plt.show()
