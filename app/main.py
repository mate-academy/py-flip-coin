import random
import matplotlib.pyplot as plt

def flip_coin(num_experiments=100_000):
    results = {i: 0 for i in range(11)}  # Від 0 до 10 гербів

    for _ in range(num_experiments):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    # Перетворимо у відсотки
    for count in results:
        results[count] = round((results[count] / num_experiments) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data):
    x = list(data.keys())
    y = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='skyblue', edgecolor='black')
    plt.title("Distribution of Number of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(range(11))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


if __name__ == '__main__':
    simulation_results = flip_coin()
    print(simulation_results)
    draw_gaussian_distribution_graph(simulation_results)
