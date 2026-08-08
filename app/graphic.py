import numpy as np
import matplotlib.pyplot as plt
from app.main import flip_coin


def draw_gaussian_distribution_graph() -> None:
    x_axis = np.array([key for key in flip_coin().keys()])
    y_axis = np.array([value for value in flip_coin().values()])
    plt.plot(x_axis, y_axis)
    plt.title("Coin flip diagram")
    plt.xlabel("Heads count")
    plt.ylabel("Drop persentage %")
    plt.show()
