import random
import matplotlib.pyplot as plt

def flip_coin(num_trials=10000):
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] * 100 / num_trials, 2)

    return results

def draw_gaussian_distribution_graph(distribution):
    x = list(distribution.keys())
    y = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title("Gaussian Distribution of 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()
