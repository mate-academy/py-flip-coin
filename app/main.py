import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    heads_cases = []
    coin_variants = ["heads", "tails"]
    result = {}
    for random_cases in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.choice(coin_variants) == "heads":
                heads_count += 1
        heads_cases.append(heads_count)

    for i in range(11):
        result[i] = round(heads_cases.count(i) / len(heads_cases) * 100, 2)
    return result


def graph_flip_coin() -> None:
    result = flip_coin()
    x_coord = list(result.keys())
    y_coord = list(result.values())

    plt.plot(x_coord, y_coord)
    plt.xlabel("Heads count")
    plt.ylabel("Drop Percentage %")

    plt.show()
