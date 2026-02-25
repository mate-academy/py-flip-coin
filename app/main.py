import random
import matplotlib.pyplot as plt


def flip_coin():
    cases = 10000
    flips_per_case = 10
    results = {i: 0 for i in range(flips_per_case + 1)}

    for _ in range(cases):
        heads_count = sum(random.randint(0, 1) for _ in range(flips_per_case))
        results[heads_count] += 1

    percentages = {
        k: (v / cases) * 100 for k, v in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(data):
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values)
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Cases")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    distribution_data = flip_coin()
    print(distribution_data)
    draw_gaussian_distribution_graph(distribution_data)
