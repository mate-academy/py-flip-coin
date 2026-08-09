import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    result = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(10))
        result[heads] += 1

    return {
        key: round(value / cases * 100, 2) for key, value in result.items()
    }


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())

    plt.bar(keys, values)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian Distribution")
    plt.show()


if __name__ == "__main__":
    data = flip_coin()
    draw_gaussian_distribution_graph(data)
