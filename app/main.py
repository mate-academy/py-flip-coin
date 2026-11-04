import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    flips_count = 10
    results = {i: 0 for i in range(flips_count + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips_count))
        results[heads] += 1

    percentage_results = {
        k: round((v / trials) * 100, 2) for k, v in results.items()
    }

    return percentage_results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    keys = list(data.keys())
    values = list(data.values())

    plt.plot(keys, values, color="blue")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.xticks(keys)
    plt.yticks(range(0, 101, 10))
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.grid(False)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
