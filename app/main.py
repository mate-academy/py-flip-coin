import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    results = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    plt.plot(list(data.keys()), list(data.values()), color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.axis([0, 10, 0, 100])
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
# write your code here
