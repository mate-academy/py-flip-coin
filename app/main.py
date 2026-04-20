from random import randint
# from matplotlib import pylab as plt


def flip_coin() -> dict:
    samples = {}
    for i in range(10000):
        key = sum(randint(0, 1) for _ in range(10))
        samples[key] = samples.setdefault(key, 0) + 1
        pers_dict = {key: value / 100 for key, value in samples.items()}
    return dict(sorted(pers_dict.items()))


# def draw_gaussian_distribution_graph(points: dict) -> None:
#     lists = sorted(points.items())
#     x, y = zip(*lists)
#     plt.plot(x, y)
#     plt.show()
