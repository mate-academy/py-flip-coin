import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    table_statistic = {i: 0 for i in range(11)}
    for _ in range(10000):
        head_count = 0
        for _ in range(10):
            result = random.randint(0, 1)
            if result == 1:
                head_count += 1

        table_statistic[head_count] += 1

    percentages = {}
    for head_count, count in table_statistic.items():
        percentage = (count / 10000) * 100
        percentages[head_count] = percentage
    return percentages


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    list_x = list(result.keys())
    list_y = list(result.values())
    plt.bar(list_x, list_y)
    plt.xlabel("Heads count")
    plt.ylabel("Percentage")
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
