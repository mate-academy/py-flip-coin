from random import randint
import matplotlib.pyplot as plt


flips = 10
attempts = 10000


def flip_coin() -> dict:
    counts = [0] * (flips + 1)

    for _ in range(attempts):
        case = sum(randint(0, 1) for _ in range(flips))
        counts[case] += 1

    return {i: (c / attempts) * 100 for i, c in enumerate(counts)}


if __name__ == "__main__":
    data = flip_coin()

    x_data = list(data.keys())
    y_data = [v for v in data.values()]

    plt.figure(figsize=(7, 5))
    plt.plot(x_data, y_data)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))

    plt.show()
