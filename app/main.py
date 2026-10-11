import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        # Flip 10 coins, counting 1s as heads
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    # Convert the raw counts to percentages
    return {k: (v / trials) * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    plt.plot(list(data.keys()), list(data.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
