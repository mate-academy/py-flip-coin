import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, flips_per_cases: int = 10) \
        -> dict[int, float]:
    result_counts = {i: 0 for i in range(flips_per_cases + 1)}
    for _ in range(cases):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_cases))
        result_counts[heads] += 1
    result_percentages = {k: round(v / cases * 100, 2)
                          for k, v in result_counts.items()}
    return result_percentages


def draw_gaussian_distribution_graph(distribution_data: dict[int, float]) \
        -> None:
    keys = sorted(distribution_data.keys())
    values = [distribution_data[k] for k in keys]
    plt.plot(keys, values, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
