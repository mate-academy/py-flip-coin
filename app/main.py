import random
import matplotlib


def flip_coin(n_trials: int = 10000, n_coins: int = 10) -> dict:
    result = {i: 0 for i in range(n_coins + 1)}
    for i in range(n_trials):
        count_heads = 0
        for _ in range(n_coins):
            flip = random.choice([1, 2])
            if flip == 1:
                count_heads += 1
        result[count_heads] += 1

    for key in result:
        result[key] = (result[key] / n_trials) * 100
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    matplotlib.plt.xlabel("Heads count")
    matplotlib.plt.ylabel("Drop percentage %")
    matplotlib.plt.bar(result.keys(), result.values())
