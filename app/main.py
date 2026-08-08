import random
import matplotlib.pyplot as plt


def flip_coin():
    res_dict = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                heads += 1
        res_dict[heads] += 1
    for i in res_dict:
        res_dict[i] = res_dict[i] / 100

    y = list(res_dict.values())
    x = list(res_dict.keys())

    plt.axis([0, 10, 0, 100])
    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    plt.plot(x, y, )
    plt.show()
