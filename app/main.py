import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    results = {i: 0.0 for i in range(11)}

    for _ in range(cases):
        heads_dropped = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_dropped] += 1

    for key in results:
        results[key] = round((results[key] / cases) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_coord = list(data.keys())
    y_coord = list(data.values())

    plt.plot(x_coord, y_coord, color="blue")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
