import random


def flip_coin() -> dict[int, float]:
    result_drops = []
    for i in range(10000):
        heads_count = 0
        for _ in range(10):
            flip = random.choice(["Heads", "Tails"])
            if flip == "Heads":
                heads_count += 1
        result_drops.append(heads_count)
    return {i: result_drops.count(i) / 10000 * 100 for i in range(11)}


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt

    results = flip_coin()
    x_points = list(results.keys())
    y_points = list(results.values())

    plt.ylim(0, 100)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(x_points, y_points)
    plt.show()
