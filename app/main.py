import random
import matplotlib.pyplot as plt


def flip_coin(number_of_cases: int = 10000, toss_per_case: int = 10) -> dict:
    result = dict.fromkeys(range(toss_per_case + 1), 0)
    for _ in range(number_of_cases):
        heads = sum(random.randint(0, 1) for _ in range(toss_per_case))
        result[heads] += 1

    for key in result:
        result[key] = round(result[key] * 100 / number_of_cases, 2)
    return result


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.plot(list(data.keys()), list(data.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.show()
