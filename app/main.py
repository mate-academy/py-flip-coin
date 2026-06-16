import random


def flip_coin():
    result_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        count_head = 0
        for _ in range(10):
            count_head += random.randint(0, 1)
        result_dict[count_head] += 1

    for i in result_dict:
        result_dict[i] = result_dict[i] * 100 / 10000

    return result_dict


def draw_gaussian_distribution_graph(result_dict):
    import matplotlib

    dpi = 80
    fig = matplotlib.pyplot.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    matplotlib.rcParams.update({'font.size': 10})

    matplotlib.pyplot.axis([0, 10, 0, 100])

    matplotlib.pyplot.title('Gaussian distribution')
    matplotlib.pyplot.xlabel('Heads count')
    matplotlib.pyplot.ylabel('Drop percentage %')

    arr = []
    keys = []
    for i in result_dict:
        arr += [result_dict[i]]
        keys += [i]

    matplotlib.pyplot.plot(keys, arr, color='blue', linestyle='solid')
    matplotlib.pyplot.legend(loc='upper right')
    fig.savefig('Graph.png')
