import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_flips = 10000
    results = [0] * 11
    for _ in range(num_flips):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1
    return {i: round(results[i] / num_flips * 100, 2) for i in range(11)}


def draw_gaussian_distribution_graph() -> None:
    call = flip_coin()
    x_points = range(11)
    y_points = [call[i] for i in x_points]
    plt.plot(x_points, y_points)
    plt.plot(x_points, y_points, marker="o")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of heads in 10 coin flips")
    plt.grid(True)
    plt.show()
