import random
import matplotlib.pyplot as plt


def flip_coin() -> None:
    coin = [0, 1]
    results = {i: 0 for i in range(11)}
    case_number = 10000
    for _ in range(case_number):
        head_count = 0
        for _ in range(10):
            if random.choice(coin):
                head_count += 1
        results[head_count] += 1
    print(results)
    for occurence in range(11):
        results[occurence] = round(results[occurence] / case_number * 100, 2)
    return results


def draw_gaussian_distribution_graph(data: dict) -> None:
    xpoints = list(data.keys())
    ypoints = list(data.values())

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.plot(xpoints, ypoints)
    plt.show()


result = flip_coin()
print(result)
draw_gaussian_distribution_graph(result)
