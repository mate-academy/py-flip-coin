import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_experiments = 10000
    num_flips = 10
    results = {k: 0 for k in range(num_flips + 1)}

    for _ in range(num_experiments):
        heads_count = 0
        for _ in range(num_flips):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1
        results[heads_count] += 1

    # convert to percentages
    for k in results:
        results[k] = (results[k] / num_experiments) * 100

    return results


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    coordinat_x = list(distribution.keys())
    coordinat_y = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(coordinat_x, coordinat_y, color="blue")
    plt.show()
