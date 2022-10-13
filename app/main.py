import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res = {i: 0 for i in range(11)}
    for _ in range(10000):
        number_of_goals = 0
        for _ in range(10):
            number_of_goals += random.randint(0, 1)
        res[number_of_goals] += 1

    return {index: value * 100 / 10000 for index, value in res.items()}


def draw_gaussian_distribution_graph(result: dict) -> None:
    plt.figure(figsize=(12, 7))
    x, y = zip(*sorted(result.items()))
    plt.plot(x, y, color="blue")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph(flip_coin())
