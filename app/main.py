import random
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 100000) -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(num_trials):
        eagle = sum(random.random() < 0.5 for _ in range(10))
        result[eagle] += 1

    for key in result.keys():
        result[key] = round(result[key] / num_trials * 100, 2)
    return result


def draw_gaussian_distribution_graph() -> None:
    ypoint = []
    dic = flip_coin()
    for value in dic.keys():
        ypoint.append(dic[value])

    plt.plot(ypoint)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
