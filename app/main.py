import random
import matplotlib.pyplot as plt


def flip_coin(n_experiments: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(n_experiments):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1

    return {k: v / n_experiments * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_cords = list(data.keys())
    y_cords = list(data.values())

    plt.figure()
    plt.plot(x_cords, y_cords, marker="o")
    plt.xlabel("Number of heads (0–10)")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution")
    plt.show()


draw_gaussian_distribution_graph()
