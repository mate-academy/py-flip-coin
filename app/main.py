import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    results = {amount: 0 for amount in range(11)}
    coin = ["head", "tail"]

    for _ in range(10000):
        head = 0
        for _ in range(10):
            result = random.choices(coin)
            if result == "head":
                head += 1
        results[head] += 1

    statistics = {amount: round((results[amount] / 10000) * 100, 2)
                  for amount in results}

    x = list(statistics.keys())
    y = list(statistics.values())
    plt.plot(x, y)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()

    return statistics
