import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads += 1

        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / cases * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_axis = list(data.keys())
    y_axis = list(data.values())

    plt.plot(x_axis, y_axis)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.title("Gaussian Distribution")
    plt.xticks(range(11))

    plt.show()


result = flip_coin()
print(result)
draw_gaussian_distribution_graph(result)
