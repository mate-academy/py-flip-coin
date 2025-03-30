import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dict_store = {}
    repeat = 10000
    for _ in range(repeat):
        heads = [random.randint(0, 1) for _ in range(10)]
        how_many_heads = len([h for h in heads if h == 1])
        tmp = dict_store.get(how_many_heads, 0)
        dict_store[how_many_heads] = dict_store.get(how_many_heads, 0) + 1

    res = {k: (v / repeat) * 100 for k, v in dict_store.items()}
    return res


def draw_gaussian_distribution_graph(res) -> None:
    x = res.keys()
    y = res.values()
    plt.plot(x, y)
    plt.show()


res = flip_coin()
draw_gaussian_distribution_graph(res)
