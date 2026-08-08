import matplotlib.pyplot as plt
import random


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    count = {i: 0 for i in range(1, flips + 1)}
    for _ in range(trials):
        heads = 0
        for __ in range(flips):
            if random.random() < 0.5:
                heads += 1
        if heads not in count:
            count[heads] = 0
        count[heads] += 1
    for key in count:
        count[key] = round(count[key] / trials * 100, 2)
    return count


def draw_gaussian_distribution_graph(
        trials: int = 10000,
        flips: int = 10
) -> None:
    dist = flip_coin(trials=trials, flips=flips)
    xs = list(dist.keys())
    ys = list(dist.values())
    plt.bar(xs, ys)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title(f"Distribution of heads in {flips} coin flips ({trials} trials)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    result = flip_coin(trials=10000, flips=10)
    print(result)
    draw_gaussian_distribution_graph(trials=20000, flips=10)
