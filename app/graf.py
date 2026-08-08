import matplotlib.pyplot as plt
from app.main import flip_coin


data = flip_coin()


def draw_gaussian_distribution_graph(data: dict) -> None:

    keys = data.keys()
    values = data.values()

    plt.figure(figsize=(10, 6))
    plt.bar(keys, values, color="blue")
    plt.xlabel("Number of Heads in 10 flips")
    plt.ylabel("Percentage from 10000 trials")
    plt.title("Simulated Gaussian Distribution of coin flips")
    plt.grid(True)
    plt.show()
