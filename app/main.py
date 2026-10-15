import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_dict = {}
    for cases in range(10000):
        heads_count = 0
        for flip in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1
        coin_dict[heads_count] = coin_dict.get(heads_count, 0) + 1
    total = sum(coin_dict.values())
    for key in coin_dict:
        coin_dict[key] = coin_dict[key] / total * 100

    return dict(sorted(coin_dict.items()))


def draw_gaussian_distribution_graph(coin_dict: dict) -> None:
    plt.title("Gaussian distribuition")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(list(coin_dict.keys()), list(coin_dict.values()))
    plt.show()
