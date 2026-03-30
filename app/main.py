import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    total_experiments = 10000
    for _ in range(total_experiments):
        head_count = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                head_count += 1
        results[head_count] += 1

    for key in results:
        results[key] = round(results[key] / total_experiments * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    points = flip_coin()
    plt.plot(points.keys(), points.values())
    plt.title("Gaussian_distribution")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()
