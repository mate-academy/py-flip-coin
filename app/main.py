import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0.0 for i in range(11)}
    num_trials = 10000
    for _ in range(num_trials):
        heads_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_count += 1
        result[heads_count] += 1
    for key in result:
        result[key] = (result[key] / num_trials) * 100
    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())
    plt.plot(keys, values, marker="o", color="blue")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Gaussian distribution of coin flips")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()


data = flip_coin()
draw_gaussian_distribution_graph(data)
