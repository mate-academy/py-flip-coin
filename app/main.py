import matplotlib.pyplot as plt
import random

def flip_coin():
    n_trials = 10000
    n_flips = 10
    results = {i: 0 for i in range(11)}

    for x in range(n_trials):
        heads_count = sum(random.randint(0, 1) for _ in range (n_flips))
        results[heads_count] += 1

    return {heads: (count/ n_trials) * 100 for heads, count in results.items()}


def draw_gaussian_distribution_graph(data):
    heads_dropped = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_dropped, percentages, marker='o', linestyle='-', color='b')
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Cases")
    plt.xticks(range(11))
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

distribution_data = flip_coin()
print(distribution_data)
draw_gaussian_distribution_graph(distribution_data)
