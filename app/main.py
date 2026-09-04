import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    wynik = np.random.choice(["head", "tail"], size=(10000, 10))
    heads = np.sum(wynik == "head", axis=1)
    zliczenia = np.bincount(heads, minlength=11)
    frequency = zliczenia / 10000 * 100
    procentage = dict(zip(range(11), frequency))
    return procentage


def draw_gaussian_distribution_graph(data: dict) -> None:

    x_axis = list(data.keys())
    y_axis = list(data.values())

    plt.plot(x_axis, y_axis)
    plt.xlabel("Liczba orłów")
    plt.ylabel("Procent przypadków (%)")
    plt.title("Rozkład liczby orłów w 10 rzutach monetą")
    plt.xticks(x_axis)

    plt.show()
