import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_cases = 10000
    rounds = 10
    result = {i: 0.0 for i in range(rounds + 1)}
    for _ in range(total_cases):
        heads = sum(random.randint(0, 1) for _ in range(rounds))
        result[heads] += 0.01
    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    axis_x = list(data.keys())
    axis_y = list(data.values())
    plt.figure(figsize=(10, 6))
    plt.bar(axis_x, axis_y)
    plt.title("Gaussian distribution)")
    plt.xlabel("Heads count")
    plt.ylabel("Drop porcentage %")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
