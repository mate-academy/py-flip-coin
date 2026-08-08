import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_of_throws = []
    for i in range(10_000):
        count_eagle = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                count_eagle += 1
        result_of_throws.append(count_eagle)

    return {
        i: round(result_of_throws.count(i) * 100 / 10_000, 2)
        for i in range(11)
    }


if __name__ == "__main__":
    data_for_the_graph = flip_coin()

    plt.plot(data_for_the_graph.keys(), data_for_the_graph.values())

    plt.show()
