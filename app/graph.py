import matplotlib.pyplot as plt
import numpy as np
from app.main import flip_coin


def draw_gaussian_distribution_graph(dots: dict) -> None:
    xpoints = np.array(list(dots.keys()))
    ypoints = np.array(list(dots.values()))

    plt.plot(xpoints, ypoints)
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
