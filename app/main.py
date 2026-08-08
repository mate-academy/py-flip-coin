from random import getrandbits


def flip_coin() -> dict:

    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if bool(getrandbits(1)):
                heads_count += 1
        results[heads_count] += 1

    percentages = {key: (value / 10000 * 100)
                   for key, value in results.items()}

    return percentages


def draw_gaussian_distribution_graph(percentages: dict) -> None:
    import matplotlib.pyplot as plt
    plt.plot(percentages.keys(), percentages.values())
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")
    plt.show()
