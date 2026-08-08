import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[float]:
    result = {i: 0 for i in range(11)}

    for el in range(10000):
        heads_per_ten_throws = (
            [random.randint(0, 1) for el in range(10)].count(1))
        result[heads_per_ten_throws] += 1

    for key, value in result.items():
        result[key] = value / 100

    return result


def raw_gaussian_distribution_graph() -> None:
    result_of_throws = flip_coin()
    plt.suptitle("Gaussian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.axis((0, 10, 0, 100))
    plt.plot(result_of_throws.keys(), result_of_throws.values())
    plt.show()
