import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    results = []
    for _ in range(10_000):
        coin_round = []
        for _ in range(10):
            coin_round.append(random.choice(coin))
        results.append(coin_round)

    result_dict = {}

    for i in range(0, 11):
        heads_count = 0
        for flip_round in results:
            if flip_round.count("heads") == i:
                heads_count += 1
        result_dict[i] = round((heads_count / len(results)) * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    x_axis = [x for x in range(11)]
    y_axis = [y for y in result_dict.values()]

    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of heads in 10 flips")

    plt.plot(x_axis, y_axis)
    plt.show()
