import random
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker


def flip_coin():
    dict = {}
    heads_all = 0
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                heads += 1

        heads_all += heads
        if heads in dict.keys():
            dict[heads] += 1
        else:
            dict.update({heads: 1})
    return dict


# def draw_gaussian_distribution_graph():
#     dict = flip_coin()
#     ls_x = []
#     ls_y = []
#     dict_sum = sum(dict.values())
#     for x in range(11):
#         ls_x.append(x)
#         y = dict[x] / dict_sum * 100
#         ls_y.append(y)
#     x = np.array(ls_x)
#     y = np.array(ls_y)
#     fig, ax = plt.subplots()
#     ax.plot(x, y, color='b', linewidth=2)
#     ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#     ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
#     ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
#     ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
#     ax.set_xlim([0, 10])
#     ax.set_ylim([0, 100])
#     fig.set_figwidth(12)
#     fig.set_figheight(8)
#     ax.set_title('Gaussian distribution')
#     ax.set_xlabel('Heads count')
#     ax.set_ylabel('Drop percentage %')
#     plt.show()
