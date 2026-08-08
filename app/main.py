import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    result = {i: 0.0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        result[heads] += 1

    for key in result:
        result[key] = round(result[key] / 10000 * 100, 2)
    return result


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    heads_counts = result.keys()
    percentages = result.values()
    plt.bar(heads_counts, percentages)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Coin flop distribution")
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
