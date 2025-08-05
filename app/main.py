import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    experiments = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(experiments):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1


    for k in results:
        results[k] = (results[k] / experiments) * 100
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    keys = sorted(results.keys())
    values = [results[k] for k in keys]
    plt.bar(keys, values, color="skyblue")

    plt.xlabel("Number of heads in 10 coin flips")
    plt.ylabel("Frequency")
    plt.title("Distribution of the number of eagles in 10,000 simulations")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    draw_gaussian_distribution_graph(results)
