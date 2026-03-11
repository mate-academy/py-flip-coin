import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    option_coin = ["crown", "coin"]
    result = {}
    crown = 0

    for i in range(10000):
        for count in range(10):
            result_of_tossing_coin = random.choice(option_coin)

            if result_of_tossing_coin == "crown":
                crown += 1

        result[crown] = result.get(crown, 0) + 1
        crown = 0

    result = {key: round(100 * (value / 10000), 2)
              for key, value in sorted(result.items())}

    return result


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.keys(), data.values())
    plt.show()
