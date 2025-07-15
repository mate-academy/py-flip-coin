import random
import matplotlib.pyplot as plt


def make_graph(data: dict[int, float]) -> None:
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xlim(0, 10)
    plt.xticks(range(0, 11))
    plt.plot(data.keys(), data.values(), color="green")
    plt.show()


def flip_coin() -> dict[int, float]:
    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for index in range(10_000):
        amount = 0
        for _ in range(10):
            amount += random.randint(0, 1)
        results[amount] += 1

    results = {key: value / 100 for key, value in results.items()}

    return results


make_graph(flip_coin())
