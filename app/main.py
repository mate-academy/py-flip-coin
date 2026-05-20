import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {num_heads: 0 for num_heads in range(11)}
    for number in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        result[heads] += 1
    return {key: round(value / 10000 * 100, 2)
            for key, value in result.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_count = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_count, percentages, marker="o", color="blue")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Gaussian distribution of coin flips")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()


draw_gaussian_distribution_graph()
