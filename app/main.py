import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {
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
    for _ in range(10000):
        coin_values = {"heads": 0, "tails": 0}
        for _ in range(10):
            value = random.choice(list(coin_values.keys()))
            if value == "heads":
                coin_values["heads"] += 1
        result[coin_values["heads"]] += 1
    for key in result.keys():
        result[key] /= 100
    return result


def draw_gaussian_distribution_grap(dictionary: dict) -> None:
    plt.plot(dictionary.keys(), dictionary.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11))
    plt.show()


draw_gaussian_distribution_grap(flip_coin())
