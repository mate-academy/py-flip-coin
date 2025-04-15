import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin(trials=10000) -> dict:
    result = {i: 0 for i in range(11)}

    for flip in range(trials):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        result[heads] += 1

    for key in result:
        result[key] = round((result[key] / trials) * 100, 2)

    return result


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_point = np.array(list(result.keys()))
    y_point = np.array(list(result.values()))
    plt.figure(figsize=(10, 5))
    plt.plot(x_point, y_point)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.ylim(0, 80)
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph()
