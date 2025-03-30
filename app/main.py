import random
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coins = {num: 0 for num in range(11)}
    for _ in range(10000):
        temp = 0
        for _ in range(10):
            if random.choice([True, False]):
                temp += 1
        coins[temp] += 1
    coins_res = {key: coins[key] / 100 for key in coins.keys()}
    return coins_res


"""
def draw_gaussian_distribution_graph(coins: dict) -> None:
    xarr = [num for num in coins.keys()]
    yarr = [num for num in coins.values()]

    plt.plot(xarr, yarr)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
"""
