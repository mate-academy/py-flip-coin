import random
import matplotlib.pyplot as plt

CASES_NUMBER = 10000
FLIP_BY_CASE = 10


# 1 - head, 0 - tail
def flip_coin() -> dict:
    report = {}
    results_heads = []
    for i in range(CASES_NUMBER):
        head_counter = 0
        for _ in range(FLIP_BY_CASE):
            flip_result = random.randint(0, 1)
            head_counter += flip_result

        results_heads.append(head_counter)

    for i in range(11):
        report[i] = round(results_heads.count(i) / CASES_NUMBER * 100, 2)

    return report


def draw_gaussian_distribution_graph(report: dict) -> None:
    x_values = []
    y_values = []

    for key, value in report.items():
        x_values.append(key)
        y_values.append(value)

    plt.plot(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))

    plt.show()


draw_gaussian_distribution_graph(flip_coin())
