import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_cases = 10000

    heads_count = {i: 0 for i in range(11)}

    for _ in range(total_cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))

        heads_count[heads] += 1

    result = {}
    for key, count in heads_count.items():
        percentage = (count / total_cases) * 100
        result[key] = round(percentage, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_axis = list(data.keys())
    y_axis = list(data.values())

    plt.plot(x_axis, y_axis, marker="o", linestyle="-", color="b")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks(range(11))

    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
