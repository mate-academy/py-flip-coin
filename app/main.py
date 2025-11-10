import random
import matplotlib.pyplot as plt

def flip_coin():
    num_simulations = 10000
    num_flips_per_simulation = 10

    heads_counts = {i: 0 for i in range(num_flips_per_simulation + 1)}

    for _ in range(num_simulations):
        current_simulation_heads = 0
        for _ in range(num_flips_per_simulation):
            if random.randint(0, 1) == 1:
                current_simulation_heads += 1
        
        heads_counts[current_simulation_heads] += 1

    percentages = {k: (v / num_simulations) * 100 for k, v in heads_counts.items()}

    return percentages

def draw_gaussian_distribution_graph():
    distribution = flip_coin() 

    x_axis = list(distribution.keys())
    y_axis = list(distribution.values())

    plt.plot(x_axis, y_axis)

    plt.title("Gaussian distribution")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Drop percentage (%)")

    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.show()
