import random
import matplotlib.pyplot as plt

def flip_coin():
    results = {i: 0 for i in range(11)}
    trials = 10000  # Number of experiments

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    # Convert counts to percentages
    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results

def draw_gaussian_distribution_graph(data):
    plt.bar(data.keys(), data.values(), color="skyblue", edgecolor="black")
    plt.title("Gaussian Distribution of Coin Flips (10 flips, 10,000 trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(range(11))
    plt.show()

# Run the simulation
results = flip_coin()
print(results)

# Draw the graph
draw_gaussian_distribution_graph(results)
