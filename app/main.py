import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float] | None:
    times = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(times):
        tails = sum(random.randint(0, 1) for _ in range(10))
        result[tails] += 1
    for key in result:
        result[key] = result[key] * 100 / times
    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.bar(data.keys(), data.values())
    plt.xlabel("Number of tails out of 10")
    plt.ylabel("Percent")
    plt.title("Distribution of tails")
    plt.show()

    print(flip_coin())
    draw_gaussian_distribution_graph()
