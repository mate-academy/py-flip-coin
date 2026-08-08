import matplotlib.pyplot as plt
import random
from collections import Counter


def flip_coin() -> dict:
    coin_list = ["Heads", "Tails"]
    generator_of_heads_occurrences = (
        [random.choice(coin_list) for _ in range(10)].count("Heads")
        for _ in range(10_000)
    )

    heads_occurrences_per_round = Counter(generator_of_heads_occurrences)
    heads_occurrences_per_round = dict(
        sorted(heads_occurrences_per_round.items()))
    heads_percentage_occurrences_per_round = {
        num_of_occur : heads_occurrences_per_round[num_of_occur] / 100
        for num_of_occur in heads_occurrences_per_round}

    return heads_percentage_occurrences_per_round


def draw_gaussian_distribution_graph(head_distribution: dict) -> None:
    x_axis = head_distribution.keys()
    y_axis = head_distribution.values()

    plt.plot(x_axis, y_axis)
    plt.show()


distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph(distribution)
