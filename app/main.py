import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_sum = 0
    cases = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for _ in range(10000):
        case = 0
        for _ in range(10):
            if random.choice([0, 1]) == 1:
                case += 1

        cases[case] += 1
        total_sum += 1
        case = 0

    for case in cases:
        cases[case] = (cases[case] / total_sum) * 100

    return cases


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values , color="blue")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
