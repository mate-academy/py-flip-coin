import random
import matplotlib.pyplot as plt


def flip_coin():
    numer_of_flips = 10
    num_experiments = 10000
    result = {}
    updated_results = {}
    for _ in range(num_experiments):
        heads = 0
        for i in range(numer_of_flips):
            flip = random.choice(["H", "T"])
            if flip == "H":
                heads += 1
        result[heads] = result.get(heads, 0) + 1

    for head_count in sorted(result):
        probability_percentage = result[head_count] / num_experiments * 100
        print(f"{head_count} heads: {probability_percentage:.4f}%")
        updated_results[head_count] = probability_percentage
    return updated_results


def draw_gaussian_distribution_graph():
    prob_percentage = flip_coin()
    x_points = [key for key in prob_percentage]
    y_points = [value for value in prob_percentage.values()]
    plt.plot(x_points, y_points)
    plt.show()
