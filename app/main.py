import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float | int]:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1

    return {k: round(v / 10000 * 100, 2) for k, v in results.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    var_x = list[int](data.keys())
    var_y = list[float | int](data.values())

    plt.bar(var_x, var_y)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Coin Flip Distribution")
    plt.show()
