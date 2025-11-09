import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10_000):
        heads = sum(random.choice([0, 1]) for x in range(10))
        result[heads] += 1

    for value in result:
        result[value] = round(result[value] / 10_000 * 100, 2)
    return result


def draw_distribution(data: dict) -> None:
    plt.plot(list(data.keys()), list(data.values()), marker=".")
    plt.title("Normal (Gaussian) distribution of coin flips")
    plt.xlabel("Amount of heads in 10 flips")
    plt.ylabel("Probability in 10 000 trials, %")
    plt.show()


if __name__ == "__main__":
    trials = flip_coin()
    print(trials)
    draw_distribution(trials)
