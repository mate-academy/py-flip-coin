import random


def flip_coin(count=10000):
    dic_head = {i: 0 for i in range(11)}
    for i in range(count):
        sum_head = 0
        for j in range(10):
            sum_head += random.randint(0, 1)
        dic_head[sum_head] += 1
    print(dic_head)
    for item in dic_head:
        dic_head[item] = dic_head[item] * 100 / count
    print(dic_head)
    return dic_head


def draw_gaussian_distribution_graph(dic):
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.axis([0, 10, 0, 100])

    plt.title('Coin flip')
    plt.xlabel('grade')
    plt.ylabel('per')
    arr = []
    keys = []
    for item in dic:
        arr += [dic[item]]
        keys += [item]

    plt.plot(keys, arr, color='blue', linestyle='solid')

    plt.legend(loc='upper right')
    fig.savefig('trigan.png')
