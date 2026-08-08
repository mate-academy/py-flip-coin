import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    results = {count: 0 for count in range(11)}

    for _ in range(trials):
        heads_count = random.getrandbits(10).bit_count()
        results[heads_count] += 1

    return {
        heads: round((amount / trials) * 100, 2)
        for heads, amount in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_counts = list(data.keys())
    drop_percentages = list(data.values())

    plt.plot(heads_counts, drop_percentages, color="blue")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.show()


if __name__ == "__main__":
    pass
