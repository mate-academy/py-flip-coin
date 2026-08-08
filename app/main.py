import random
import matplotlib.pyplot as plt


def flip_coin():
    heads_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1

        heads_dict[heads] += 1

    for key, value in heads_dict.items():
        heads_dict[key] = int(round(value / 10000 * 100, 0))

    return heads_dict


def draw_gaussian_distribution_graph():
    x = flip_coin().keys()
    y = flip_coin().values()

    fig = plt.figure()
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 110, 10))
    plt.plot(x, y)
    fig.suptitle('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')
    fig.savefig('test.png')
    plt.show()
