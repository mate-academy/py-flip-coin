import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number_of_iterations = 20_000
    probability = dict()

    for _ in range(number_of_iterations):
        flips = [random.choice([0, 1]) for _ in range(10)]
        if sum(flips) not in probability:
            probability[sum(flips)] = 1
        else:
            probability[sum(flips)] += 1

    return {
        k: round(v / number_of_iterations * 100, 2)
        for k, v in probability.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    coin_value = sorted(data.keys())
    probability = [data[k] for k in coin_value]

    plt.plot(coin_value, probability, color="blue")

    plt.title("Coin Flip Distribution")
    plt.xlabel("Number of Heads (out of 10)")
    plt.ylabel("Probability %")

    plt.xticks([x for x in range(1, 11)])

    plt.grid(True)

    plt.show()
