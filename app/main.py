import random
import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin():
    dict_coins = {i: 0 for i in range(11)}

    for _ in range(10000):
        sum_heads = 0

        for _ in range(10):
            heads = random.randint(0, 1)
            if heads:
                sum_heads += 1

        dict_coins[sum_heads] += 1

    return {key: round(value / 100) for key, value in dict_coins.items()}


def draw_gaussian_distribution_graph():
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.axis([0, 10, 0, 100])

    plt.title('Gaussian distribution')
    plt.xlabel('Heads count')
    plt.ylabel('Drop percentage %')

    x_line = []
    y_line = []
    dict_coin = flip_coin()

    for key, value in dict_coin.items():
        x_line.append(key)
        y_line.append(value)

    plt.plot(x_line, y_line, color='blue', linestyle='solid',
             label='flip coin')

    plt.legend(loc='upper right')
    fig.savefig('heads.png')
